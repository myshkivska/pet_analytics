import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def load_data(path: str):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    if "math score" in df.columns and "reading score" in df.columns and "writing score" in df.columns:
        df["total_score"] = df["math score"] + df["reading score"] + df["writing score"]
        df["mean_score"] = df["total_score"] / 3
    return df

