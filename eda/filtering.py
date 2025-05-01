# Filtering module
import streamlit as st

def show_filtering(df):
    st.title("🔍 Filter Courses")

    subjects = st.multiselect("Select Subject(s)", options=df["subject"].unique(), default=df["subject"].unique())
    levels = st.multiselect("Select Course Level(s)", options=df["level"].unique(), default=df["level"].unique())
    price_type = st.radio("Select Price Type", ["All", "Free", "Paid"])

    filtered_df = df[df["subject"].isin(subjects) & df["level"].isin(levels)]

    if price_type == "Free":
        filtered_df = filtered_df[filtered_df["price"] == 0]
    elif price_type == "Paid":
        filtered_df = filtered_df[filtered_df["price"] != 0]

    st.write(f"📄 {filtered_df.shape[0]} Courses Found")
    st.dataframe(filtered_df)
