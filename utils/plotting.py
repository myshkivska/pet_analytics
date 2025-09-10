from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

DEFAULT_TITLE_KW = dict(loc="left", pad=12, fontweight="bold")

def fmt_num(x, pos=None):
    if abs(x) >= 1000:
        return f"{x:,.0f}"
    if float(x).is_integer():
        return f"{int(x)}"
    return f"{x:.2f}"

def fmt_pct(x, pos=None):
    return f"{x*100:.0f}%"

def apply_number_formatter(ax, axis="y", percent=False):
    fmt = FuncFormatter(fmt_pct if percent else fmt_num)
    if axis == "y":
        ax.yaxis.set_major_formatter(fmt)
    else:
        ax.xaxis.set_major_formatter(fmt)

def labelize(ax, *, title:str=None, xlabel:str=None, ylabel:str=None):
    if title:
        ax.set_title(title, **DEFAULT_TITLE_KW)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return ax

def annotate_n(ax, *, n:int, loc="upper right"):
    txt = f"n = {n:,}"
    x, y = 0.98, 0.98
    if loc == "upper left":
        x, y = 0.02, 0.98
    elif loc == "lower left":
        x, y = 0.02, 0.02
    elif loc == "lower right":
        x, y = 0.98, 0.02
    ax.annotate(txt, xy=(x, y), xycoords="axes fraction",
                ha="right" if "right" in loc else "left",
                va="top" if "upper" in loc else "bottom",
                fontsize=9, alpha=0.8)
    return ax

def finalize(fig):
    fig.tight_layout()
    return fig
