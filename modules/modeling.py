import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from utils.plotting import labelize, finalize

CATEGORICALS = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]

def modeling_dashboard(df: pd.DataFrame):
    st.subheader("Predictive Modeling — Estimate average score")
    target = "mean_score"
    if target not in df.columns:
        df[target] = (df["math score"] + df["reading score"] + df["writing score"]) / 3

    num_features = ["math score", "reading score", "writing score"]
    cat_features = [c for c in CATEGORICALS if c in df.columns]

    X = df[num_features + cat_features]
    y = df[target]

    test_size = st.slider("Test size", 0.1, 0.4, 0.2, 0.05)
    random_state = 42

    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)],
        remainder="passthrough",
    )
    model = Pipeline([("prep", preprocessor), ("lr", LinearRegression())])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5  # sqrt(MSE) = RMSE

    c1, c2, c3 = st.columns(3)
    c1.metric("R²", f"{r2:.3f}")
    c2.metric("MAE", f"{mae:.2f}")
    c3.metric("RMSE", f"{rmse:.2f}")

    st.markdown("#### Predicted vs Actual")
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, alpha=0.6)
    lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
    ax.plot(lims, lims, linestyle="--")
    labelize(ax, title="Predicted vs Actual — Mean Score", xlabel="Actual", ylabel="Predicted")
    finalize(fig)
    st.pyplot(fig)
    st.caption("Diagonal line is perfect fit; points closer to it indicate better predictions.")
