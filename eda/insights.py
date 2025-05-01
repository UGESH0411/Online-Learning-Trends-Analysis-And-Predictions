# Insights module
import streamlit as st
import pandas as pd
def show_insights(df):
    st.title("📈 Course Insights")

    # Preprocessing: Convert timestamp and create derived metrics
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'], errors='coerce')
    df['engagement_score'] = df['num_reviews'] * df['num_lectures']
    df['review_rate'] = df['num_reviews'] / (df['num_subscribers'] + 1)

    # Top 10 Most Subscribed Courses
    st.subheader("🌟 Top 10 Most Subscribed Courses")
    top_subs = df.sort_values("num_subscribers", ascending=False).head(10)
    st.dataframe(top_subs[["course_title", "subject", "num_subscribers", "price", "level"]])

    # Top 10 Most Reviewed Courses
    st.subheader("💬 Top 10 Most Reviewed Courses")
    top_reviews = df.sort_values("num_reviews", ascending=False).head(10)
    st.dataframe(top_reviews[["course_title", "subject", "num_reviews", "price", "level"]])

    # Top 10 Most Engaging Courses
    st.subheader("🔥 Top 10 Most Engaging Courses")
    top_engagement = df.sort_values("engagement_score", ascending=False).head(10)
    st.dataframe(top_engagement[["course_title", "subject", "engagement_score", "num_reviews", "num_lectures"]])

    # Top 10 Courses with Highest Review Rate
    st.subheader("📈 Top 10 Courses with Highest Review Rate")
    top_review_rate = df.sort_values("review_rate", ascending=False).head(10)
    st.dataframe(top_review_rate[["course_title", "subject", "review_rate", "num_reviews", "num_subscribers"]])

    # Top 10 Longest Courses (in Hours)
    st.subheader("⏱️ Top 10 Longest Courses (in Hours)")
    top_duration = df.sort_values("content_duration", ascending=False).head(10)
    st.dataframe(top_duration[["course_title", "subject", "content_duration", "num_lectures", "price"]])

    # 10 Most Recently Published Courses
    st.subheader("🆕 10 Most Recently Published Courses")
    recent_courses = df.sort_values("published_timestamp", ascending=False).head(10)
    st.dataframe(recent_courses[["course_title", "subject", "published_timestamp", "price", "level"]])

    # Top 10 Courses with Most Lectures
    st.subheader("📚 Top 10 Courses with Most Lectures")
    top_lectures = df.sort_values("num_lectures", ascending=False).head(10)
    st.dataframe(top_lectures[["course_title", "subject", "num_lectures", "content_duration", "price"]])

    # Top 10 Most Subscribed Free Courses
    st.subheader("🆓 Top 10 Most Subscribed Free Courses")
    free_courses = df[df["is_paid"] == False]
    top_free = free_courses.sort_values("num_subscribers", ascending=False).head(10)
    st.dataframe(top_free[["course_title", "subject", "num_subscribers", "level"]])


    st.subheader("🔍 Compare Two Courses Side-by-Side")

    col1, col2 = st.columns(2)

    with col1:
        course1 = st.selectbox("Select First Course", df['course_title'].dropna().unique(), key="course1")
        data1 = df[df['course_title'] == course1].sort_values("published_timestamp", ascending=False).iloc[0]

    with col2:
        course2 = st.selectbox("Select Second Course", df['course_title'].dropna().unique(), key="course2")
        data2 = df[df['course_title'] == course2].sort_values("published_timestamp", ascending=False).iloc[0]

    st.markdown("### 📊 Comparison")

    comp_df = pd.DataFrame({
        'Metric': [
            'Subject', 'Level', 'Price', 'Subscribers', 'Reviews',
            'Lectures', 'Content Duration (min)', 'Engagement Score'
        ],
        course1: [
            data1['subject'], data1['level'], data1['price'], data1['num_subscribers'],
            data1['num_reviews'], data1['num_lectures'], data1['content_duration'],
            data1['num_reviews'] * data1['num_lectures']
        ],
        course2: [
            data2['subject'], data2['level'], data2['price'], data2['num_subscribers'],
            data2['num_reviews'], data2['num_lectures'], data2['content_duration'],
            data2['num_reviews'] * data2['num_lectures']
        ]
    })

    st.dataframe(comp_df.set_index('Metric'))
