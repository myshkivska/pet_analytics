import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from utils.plotting import labelize, annotate_n, finalize

CATEGORICALS = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]
METRICS = ["math score", "reading score", "writing score", "mean_score"]

def cohen_d(x, y):
    nx, ny = len(x), len(y)
    vx, vy = np.var(x, ddof=1), np.var(y, ddof=1)
    pooled = ((nx - 1) * vx + (ny - 1) * vy) / (nx + ny - 2)
    return (np.mean(x) - np.mean(y)) / np.sqrt(pooled) if pooled > 0 else 0.0

def run_ab_test(df: pd.DataFrame):
    st.subheader("A/B Testing — Compare two groups")
    col1, col2 = st.columns(2)
    with col1:
        group_col = st.selectbox("Grouping variable", CATEGORICALS, index=4)
    with col2:
        metric = st.selectbox("Metric", METRICS, index=3)

    categories = df[group_col].value_counts().index.tolist()
    if len(categories) < 2:
        st.warning("Selected column has less than 2 categories.")
        return

    c1, c2 = st.columns(2)
    with c1:
        A = st.selectbox("Group A", categories, index=0)
    with c2:
        B = st.selectbox("Group B", categories, index=1 if len(categories) > 1 else 0)

    group_A = df[df[group_col] == A][metric].dropna()
    group_B = df[df[group_col] == B][metric].dropna()

    t_stat, p_t = stats.ttest_ind(group_A, group_B, equal_var=False)
    u_stat, p_u = stats.mannwhitneyu(group_A, group_B, alternative="two-sided")
    d = cohen_d(group_A.values, group_B.values)

    st.markdown(f"**Welch t-test**: t = {t_stat:.3f}, p = {p_t:.4f}")
    st.markdown(f"**Mann–Whitney U**: U = {u_stat:.3f}, p = {p_u:.4f}")
    st.markdown(f"**Effect size (Cohen's d)**: {d:.3f}")

    st.markdown("#### Distributions")
    fig, ax = plt.subplots()
    sns.kdeplot(group_A, fill=True, alpha=0.4, label=f"{A}", ax=ax)
    sns.kdeplot(group_B, fill=True, alpha=0.4, label=f"{B}", ax=ax)
    labelize(ax, title=f"Density — {metric.title()} ({A} vs {B})", xlabel=metric.title(), ylabel="Density")
    annotate_n(ax, n=len(group_A)+len(group_B))
    ax.legend(title=group_col)
    finalize(fig)
    st.pyplot(fig)
    st.caption("Kernel density estimate for each group; areas integrate to 1.")

    st.markdown("#### Boxplot")
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=pd.DataFrame({metric: pd.concat([group_A, group_B], ignore_index=True),
                                   group_col: [A]*len(group_A) + [B]*len(group_B)}),
                x=group_col, y=metric, ax=ax2)
    labelize(ax2, title=f"{metric.title()} — {A} vs {B}", xlabel=group_col, ylabel=metric.title())
    finalize(fig2)
    st.pyplot(fig2)
    st.caption("Boxplot compares central tendency and spread between groups.")
