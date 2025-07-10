# utils/charts.py
import streamlit as st
import streamlit_shadcn_ui as ui
import plotly.graph_objects as go

def overview_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close Price', mode='lines'))
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], name='Volume', yaxis='y2', opacity=0.3))
    fig.update_layout(
        title="Stock Price & Volume Overview",
        yaxis=dict(title="Price"),
        yaxis2=dict(overlaying='y', side='right', title='Volume', showgrid=False),
        xaxis_title="Date",
        legend=dict(x=0, y=1.1, orientation='h')
    )
    return fig

def analysis_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], name='RSI', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MACD'], name='MACD', line=dict(color='blue')))
    fig.update_layout(title="Technical Indicators: RSI & MACD", xaxis_title="Date", yaxis_title="Value")
    return fig

def reports_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close Price'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Bollinger_Upper'], name='Upper Band', line=dict(dash='dot')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Bollinger_Lower'], name='Lower Band', line=dict(dash='dot')))
    fig.update_layout(title="Price with Bollinger Bands", xaxis_title="Date", yaxis_title="Price")
    return fig

def notifications_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Sentiment_Score'], name='Sentiment Score', mode='lines+markers'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Inflation_Rate'], name='Inflation Rate', yaxis='y2'))
    fig.update_layout(
        title="Sentiment vs Inflation",
        yaxis=dict(title='Sentiment'),
        yaxis2=dict(overlaying='y', side='right', title='Inflation Rate'),
        xaxis_title='Date'
    )
    return fig
