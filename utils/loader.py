# utils/loader.py
import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from datetime import timedelta

def load_data():
    df = pd.read_csv('./datasets/data/stock_data.csv')
    start_date = pd.Timestamp.today() - pd.Timedelta(days=len(df) - 1)
    df['Date'] = pd.date_range(start=start_date, periods=len(df), freq='D')
    return df


def filter_by_time_range(df, selection):
    if selection == "1 Week":
        return df[df['Date'] >= pd.Timestamp.today() - pd.Timedelta(weeks=1)]
    elif selection == "1 Month":
        return df[df['Date'] >= pd.Timestamp.today() - pd.DateOffset(months=1)]
    elif selection == "3 Months":
        return df[df['Date'] >= pd.Timestamp.today() - pd.DateOffset(months=3)]
    else:
        return df
