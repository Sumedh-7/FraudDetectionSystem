import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    df = pd.read_csv("../data/train_transaction.csv")
    return df

df = load_data()

# =========================
# LOAD MODEL
# =========================

try:
    model = joblib.load("model.pkl")
except:
    model = None

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Fraud Dashboard")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Overview",
        "Transaction Explorer",
        "Risk Analysis"
    ]
)

# =========================
# OVERVIEW PAGE
# =========================

if page == "Overview":

    st.title("Real-Time Fraud Detection Dashboard")

    st.markdown("---")

    # Metrics

    total_transactions = len(df)

    fraud_count = int(df['isFraud'].sum())

    fraud_rate = round(
        (fraud_count / total_transactions) * 100,
        2
    )

    avg_transaction = round(
        df['TransactionAmt'].mean(),
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Transactions",
        f"{total_transactions:,}"
    )

    col2.metric(
        "Fraud Transactions",
        f"{fraud_count:,}"
    )

    col3.metric(
        "Fraud Rate %",
        fraud_rate
    )

    col4.metric(
        "Average Amount",
        avg_transaction
    )

    st.markdown("---")

    # Fraud Distribution

    st.subheader("Fraud Distribution")

    fraud_chart = px.histogram(
        df.sample(10000),
        x="TransactionAmt",
        color="isFraud",
        nbins=50,
        title="Transaction Amount Distribution"
    )

    st.plotly_chart(
        fraud_chart,
        use_container_width=True
    )

    # Fraud Count Pie Chart

    st.subheader("Fraud vs Non-Fraud")

    fraud_counts = df['isFraud'].value_counts()

    pie_chart = px.pie(
        names=["Non-Fraud", "Fraud"],
        values=fraud_counts.values,
        title="Fraud Percentage"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

# =========================
# TRANSACTION EXPLORER
# =========================

elif page == "Transaction Explorer":

    st.title("Transaction Explorer")

    st.markdown("---")

    # Search Transaction

    transaction_id = st.number_input(
        "Enter TransactionID",
        min_value=int(df['TransactionID'].min()),
        max_value=int(df['TransactionID'].max()),
        value=int(df['TransactionID'].min())
    )

    filtered_df = df[
        df['TransactionID'] == transaction_id
    ]

    st.subheader("Transaction Details")

    st.dataframe(filtered_df)

    st.markdown("---")

    st.subheader("Dataset Sample")

    st.dataframe(
        df.sample(100)
    )

# =========================
# RISK ANALYSIS
# =========================

elif page == "Risk Analysis":

    st.title("Risk Analysis")

    st.markdown("---")

    sample_df = df.sample(5000)

    # Scatter Plot

    scatter_fig = px.scatter(
        sample_df,
        x='TransactionAmt',
        y='TransactionDT',
        color='isFraud',
        title='Transaction Risk Scatter Plot'
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

    # Hour Analysis

    st.subheader("Hourly Fraud Pattern")

    sample_df['Hour'] = (
        sample_df['TransactionDT'] / 3600
    ) % 24

    hour_chart = px.histogram(
        sample_df,
        x='Hour',
        color='isFraud',
        nbins=24,
        title='Fraud by Hour'
    )

    st.plotly_chart(
        hour_chart,
        use_container_width=True
    )

    # Correlation Heatmap

    st.subheader("Correlation Heatmap")

    numeric_df = sample_df.select_dtypes(
        include=np.number
    )

    corr = numeric_df[
        ['TransactionAmt', 'TransactionDT', 'isFraud']
    ].corr()

    st.dataframe(corr)

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Real-Time Fraud Detection System using Machine Learning & Explainable AI"
)