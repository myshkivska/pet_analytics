import streamlit as st
from modules.data_loader import load_data
from modules.overview import overview_dashboard
from modules.ab_test import run_ab_test
from modules.modeling import modeling_dashboard
from utils.styles import apply_styles

st.set_page_config(page_title="Student Performance — Analytics", layout="wide")
apply_styles()

st.title("Dashboard")

DATA_PATH = "data/marketing_cleaned.csv"
df = load_data(DATA_PATH)

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "A/B Testing", "Modeling"], index=0)

if page == "Overview":
    overview_dashboard(df)
elif page == "A/B Testing":
    run_ab_test(df)
elif page == "Modeling":
    modeling_dashboard(df)
