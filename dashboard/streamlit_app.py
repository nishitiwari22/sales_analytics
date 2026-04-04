import streamlit as st
import pandas as pd
import os

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Analytics Dashboard")

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    file_path = os.path.join(os.getcwd(), "data", "sales.csv")

    if not os.path.exists(file_path):
        st.error(f"❌ File not found: {file_path}")
        st.stop()

    df = pd.read_csv(file_path)
    return df

df = load_data()

# -------------------------------
# RAW DATA
# -------------------------------
st.subheader("Raw Data")
st.dataframe(df)

# -------------------------------
# REVENUE BY REGION
# -------------------------------
st.subheader("Revenue by Region")
if "Region" in df.columns and "Sales" in df.columns:
    region_sales = df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)
else:
    st.warning("Columns 'Region' or 'Sales' not found.")

# -------------------------------
# PROFIT BY CATEGORY
# -------------------------------
st.subheader("Profit by Category")
if "Category" in df.columns and "Profit" in df.columns:
    category_profit = df.groupby("Category")["Profit"].sum()
    st.bar_chart(category_profit)
else:
    st.warning("Columns 'Category' or 'Profit' not found.")
