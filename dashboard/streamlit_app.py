# import streamlit as st
# import pandas as pd

from pathlib import Path
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

import os

@st.cache_data
def load_data():
    file_path = os.path.join(os.getcwd(), "data", "sales.csv")

    if not os.path.exists(file_path):
        st.error(f"❌ File not found: {file_path}")
        st.stop()

    df = pd.read_csv(file_path)
    return df

df = load_data()

engine = create_engine("sqlite:///sales.db")


df = load_data()

st.title("📊 Sales Analytics Dashboard")

import os
from sqlalchemy import create_engine

db_path = os.path.join(os.getcwd(), "sales.db")
engine = create_engine(f"sqlite:///{db_path}")

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
