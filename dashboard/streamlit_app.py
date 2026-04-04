# import streamlit as st
# import pandas as pd

from pathlib import Path
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

@st.cache_data
def load_data():
    base_path = Path(__file__).parent.parent  # go to project root
    file_path = base_path / "data" / "sales.csv"
    return pd.read_csv(file_path)

engine = create_engine("sqlite:///sales.db")


df = load_data()

st.title("📊 Sales Analytics Dashboard")

import os

file_path = os.path.join(os.getcwd(), "data", "sales.csv")

if not os.path.exists(file_path):
    st.error(f"File not found: {file_path}")
    st.stop()

df = pd.read_csv(file_path)

st.subheader("Raw Data")
df = pd.read_csv("sales.csv")
st.dataframe(df)
# 
# Revenue by Region
st.subheader("Revenue by Region")
region_sales = df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)

# Profit by Category
st.subheader("Profit by Category")
category_profit = df.groupby("Category")["Profit"].sum()
st.bar_chart(category_profit)

@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM sales", engine)

df = load_data()


df = load_data()

st.dataframe(df)
