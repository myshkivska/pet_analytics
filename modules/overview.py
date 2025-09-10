import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils.plotting import labelize, annotate_n, apply_number_formatter, finalize

CATEGORICALS = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]
METRICS = ["math score", "reading score", "writing score", "mean_score"]


def overview_dashboard(df: pd.DataFrame):
    st.subheader("Overview & Distributions")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Students", f"{len(df):,}")
    c2.metric("Avg Math", f"{df['math score'].mean():.1f}")
    c3.metric("Avg Reading", f"{df['reading score'].mean():.1f}")
    c4.metric("Avg Writing", f"{df['writing score'].mean():.1f}")

    st.markdown("#### Score Distributions")
    mcol = st.selectbox("Metric", METRICS, index=3, key="dist_metric")
    fig, ax = plt.subplots()
    sns.histplot(df[mcol], kde=True, ax=ax)
    labelize(ax, title=f"Distribution — {mcol.title()}", xlabel=mcol.title(), ylabel="Count")
    annotate_n(ax, n=df[mcol].dropna().shape[0])
    finalize(fig)
    st.pyplot(fig)
    st.caption("Histogram with KDE; counts shown on Y-axis. Sample size displayed as n.")

    st.markdown("#### Group Averages")
    gcol = st.selectbox("Group by", CATEGORICALS, index=0, key="group_by")
    fig2, ax2 = plt.subplots()
    grp = df.groupby(gcol)[METRICS].mean().sort_values("mean_score" if "mean_score" in df else "math score")
    grp.plot(kind="bar", ax=ax2)
    labelize(ax2, title=f"Average Scores by {gcol}", ylabel="Average Score", xlabel=gcol)
    apply_number_formatter(ax2, axis="y", percent=False)
    ax2.legend(title="Metric", bbox_to_anchor=(1.02, 1), loc="upper left")
    finalize(fig2)
    st.pyplot(fig2)
    st.caption("Bar chart of mean scores per category; error bars not shown.")

    st.markdown("#### Spread by Group")
    fig3, ax3 = plt.subplots()
    sns.boxplot(data=df, x=gcol, y=mcol, ax=ax3)
    labelize(ax3, title=f"{mcol.title()} by {gcol}", xlabel=gcol, ylabel=mcol.title())
    plt.setp(ax3.get_xticklabels(), rotation=20, ha="right")
    finalize(fig3)
    st.pyplot(fig3)
    st.caption("Box shows IQR, line is median; whiskers extend to 1.5×IQR.")
