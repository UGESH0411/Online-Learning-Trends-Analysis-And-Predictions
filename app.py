import streamlit as st
import pandas as pd

from preprocessing import preprocess
from eda import overview, filtering, insights, visualization
from ml import predict

# Set page configuration
st.set_page_config(
    page_title="Online Learning Course Trend Analysis & Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("📊 Online Learning Course Trend Analysis & Prediction")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("udemy_courses.csv")
    return df

df = load_data()

# Sidebar navigation
st.sidebar.title("🔎 Navigation")
option = st.sidebar.radio("Go to", [
    "Dataset Overview",
    "Course Filtering",
    "Course Insights",
    "Visualizations",
    "ML Prediction",
])

# Load appropriate module
if option == "Dataset Overview":
    overview.show_overview(df)

elif option == "Course Filtering":
    filtering.show_filtering(df)

elif option == "Course Insights":
    insights.show_insights(df)

elif option == "Visualizations":
    visualization.show_visualizations(df)

elif option == "ML Prediction":
    predict.show_prediction(df)
