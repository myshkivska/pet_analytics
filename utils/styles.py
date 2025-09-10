import streamlit as st
import matplotlib as mpl

DEFAULT_FIGSIZE = (7, 4)
DEFAULT_DPI = 120

def apply_styles():
    mpl.rcParams.update({
        "figure.figsize": DEFAULT_FIGSIZE,
        "figure.dpi": DEFAULT_DPI,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "axes.grid": True,
        "grid.alpha": 0.25,
    })
    st.markdown(
        """
        <style>
            .main {padding: 1.5rem 2rem;}
            .stMetric, .stAlert {border-radius: 16px;}
            div[data-testid="stPlotlyChart"] {height: 430px;}
            div[data-testid="stVegaLiteChart"] {height: 430px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
