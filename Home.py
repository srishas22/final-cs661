import streamlit as st
import streamlit_shadcn_ui as ui
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch
import base64
from datasets import names
from utils.loader import load_data, filter_by_time_range
from utils.charts import overview_chart, analysis_chart, reports_chart, notifications_chart


# ----------------- CONFIG -----------------
st.set_page_config(
    page_title="StocksViz",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------- BACKGROUND IMAGE AS BASE64 -----------------
img_path = "C:/Users/srish/.vscode/.vscode/final cs661/assets/background.jpg"
with open(img_path, "rb") as f:
    img_data = base64.b64encode(f.read()).decode()

# ----------------- CUSTOM CSS -----------------
st.markdown(f"""
    <style>
    /* Full width hero section */
    .full-bg {{
        position: relative;
        width: 100vw;
        margin-left: -3.5vw;
        margin-top: -4vh;
        height: 420px;
        background-image: url("data:image/png;base64,{img_data}");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 0;
    }}
    .overlay {{
        background-color: rgba(0, 0, 0, 0.75);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        max-width: 1000px;
        margin: 0 auto;
    }}
    .overlay h1 {{
        font-size: 3rem;
        margin-bottom: 1rem;
    }}
    .overlay p {{
        font-size: 1.2rem;
        line-height: 1.6;
    }}

    </style>

    <div class="full-bg">
        <div class="overlay">
            <h1><strong>StocksViz</strong></h1>
            <p>
                Markets move for a reason – sometimes it’s the economy, sometimes it’s emotion.
                We bring those pieces together, helping you explore how stocks react to shifts in sentiment,
                major events, and macro trends. With interactive visuals and clean design,
                we make market stories easier to see and understand.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# ----------------- METRIC CARDS -----------------
st.markdown("### ")  # Spacer after hero

cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="NIFTY 50", content="", description="+20.1% from last month", key="card1")
with cols[1]:
    ui.metric_card(title="SENSEX", content="", description="+20.1% from last month", key="card2")
with cols[2]:
    ui.metric_card(title="Market Mood", content="",description="Greed Zone", key="card3")

# Start a container to group tabs + chart
with st.container():
    # Inject opening div with our class
    st.markdown('<div class="rounded-box">', unsafe_allow_html=True)
# Inject CSS to reduce spacing between tabs and chart
st.markdown("""
    <style>
    /* Remove margin/padding below tab groups */
    .element-container:has(.ui-tabs) + div {
        margin-top: -30px !important;
    }

    /* Optional: shrink space below columns if needed */
    .element-container:has(.stColumns) + div {
        margin-top: -20px !important;
    }
    </style>
""", unsafe_allow_html=True)
    # ---- Tabs Row ----
col1, col2 = st.columns([2, 1])
with col1:
    selected_tab = ui.tabs(
        options=["Overview", "Analysis", "Reports", "Notifications"],
        default_value="Overview",
        key="kanaries_tab"
    )
with col2:
    time_range = ui.tabs(
        options=["1 Week", "1 Month", "3 Months", "All"],
        default_value="1 Week",
        key="kanaries_time"
    )

    # ---- Load & Filter Data ----
df = load_data()
filtered_df = filter_by_time_range(df, time_range)

    # ---- Display Chart Based on Tab ----
if selected_tab == "Overview":
    st.plotly_chart(overview_chart(filtered_df), use_container_width=True)
elif selected_tab == "Analysis":
    st.plotly_chart(analysis_chart(filtered_df), use_container_width=True)
elif selected_tab == "Reports":
    st.plotly_chart(reports_chart(filtered_df), use_container_width=True)
elif selected_tab == "Notifications":
    st.plotly_chart(notifications_chart(filtered_df), use_container_width=True)

# ----------------- FOOTER -----------------
st.markdown("""
    <style>
    .footer {
        text-align: center;
        padding: 1rem;
        color: #888;
        font-size: 0.9rem;
    }
    </style>
    <div class="footer">
        © 2025 StocksViz | Built with Streamlit and ❤️
    </div>
""", unsafe_allow_html=True)