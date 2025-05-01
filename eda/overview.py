# Overview module
import streamlit as st

def show_overview(df):
    st.title("📊 Dataset Overview")
    st.subheader("🔹 Preview of Dataset")
    st.dataframe(df.head())

    st.subheader("🔹 Shape and Columns")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")
    st.write("Columns:", list(df.columns))

    st.subheader("🔹 Missing Values")
    st.write(df.isnull().sum())

    st.subheader("🔹 Data Types")
    st.write(df.dtypes)
