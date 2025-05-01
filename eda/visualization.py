# Visualization module
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
def show_visualizations(df):
    st.title("📊 Visual Explorations")

    st.subheader("🔹 Subject Distribution")
    fig1, ax1 = plt.subplots()
    df["subject"].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax1)
    ax1.axis("equal")
    st.pyplot(fig1)

    st.subheader("🔹 Average Subscribers per Subject")
    avg_subs = df.groupby("subject")["num_subscribers"].mean().sort_values()
    fig2, ax2 = plt.subplots()
    sns.barplot(x=avg_subs.values, y=avg_subs.index, palette="viridis", ax=ax2)
    ax2.set_xlabel("Average Subscribers")
    ax2.set_ylabel("Subject")
    st.pyplot(fig2)

    st.subheader("🔹 Subscribers vs Reviews")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x="num_reviews", y="num_subscribers", hue="price", alpha=0.6, ax=ax3)
    ax3.set_title("Subscribers vs Reviews")
    st.pyplot(fig3)

    st.subheader("🔹 Course Price Distribution")
    fig4, ax4 = plt.subplots()
    sns.histplot(df['price'], bins=30, kde=True, ax=ax4, color="teal")
    ax4.set_title("Distribution of Course Prices")
    st.pyplot(fig4)

    st.subheader("🔹 Level-wise Average Subscribers")
    avg_subs_level = df.groupby("level")["num_subscribers"].mean().sort_values(ascending=False)
    fig5, ax5 = plt.subplots()
    sns.barplot(x=avg_subs_level.index, y=avg_subs_level.values, palette="magma", ax=ax5)
    ax5.set_ylabel("Avg Subscribers")
    ax5.set_title("Average Subscribers by Course Level")
    st.pyplot(fig5)

    st.subheader("🔹 Correlation Heatmap")
    numeric_df = df.select_dtypes(include=[np.number])
    fig6, ax6 = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax6)
    ax6.set_title("Correlation Between Numeric Features")
    st.pyplot(fig6)

    st.subheader("🔹 Course Duration Distribution")
    fig7, ax7 = plt.subplots()
    sns.histplot(df['content_duration'], bins=30, kde=True, color="purple", ax=ax7)
    ax7.set_title("Distribution of Content Duration (in hours)")
    st.pyplot(fig7)

    st.subheader("🔹 Subscribers by Subject (Box Plot)")
    fig8, ax8 = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x="subject", y="num_subscribers", palette="pastel", ax=ax8)
    ax8.set_yscale("log")
    ax8.set_title("Subscribers by Subject (Log Scale)")
    st.pyplot(fig8)

    # ----------------- Additional Visualizations -----------------
    st.subheader("🔹 Course Publishing Trend Over Time")
    df["published_timestamp"] = pd.to_datetime(df["published_timestamp"])
    df["published_year"] = df["published_timestamp"].dt.year
    yearly_counts = df["published_year"].value_counts().sort_index()
    fig9, ax9 = plt.subplots()
    sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker="o", ax=ax9)
    ax9.set_title("Courses Published per Year")
    ax9.set_xlabel("Year")
    ax9.set_ylabel("Number of Courses")
    st.pyplot(fig9)

    st.subheader("🔹 Review Rate Distribution (Reviews / Subscribers)")
    df["review_rate"] = df["num_reviews"] / df["num_subscribers"]
    df["review_rate"] = df["review_rate"].replace([np.inf, -np.inf], np.nan).fillna(0)
    fig10, ax10 = plt.subplots()
    sns.histplot(df["review_rate"], bins=50, kde=True, ax=ax10, color="coral")
    ax10.set_title("Review Rate Distribution")
    st.pyplot(fig10)

    st.subheader("🔹 Free vs Paid: Avg Subscribers")
    df["is_paid"] = df["is_paid"].astype(str)
    paid_avg = df.groupby("is_paid")["num_subscribers"].mean()
    fig11, ax11 = plt.subplots()
    sns.barplot(x=paid_avg.index, y=paid_avg.values, palette="Set2", ax=ax11)
    ax11.set_title("Average Subscribers: Free vs Paid Courses")
    ax11.set_ylabel("Avg Subscribers")
    ax11.set_xlabel("Is Paid?")
    st.pyplot(fig11)

    st.subheader("🔹 Lectures vs Subscribers")
    fig12, ax12 = plt.subplots()
    sns.scatterplot(data=df, x="num_lectures", y="num_subscribers", alpha=0.5, ax=ax12)
    ax12.set_title("Lectures vs Subscribers")
    st.pyplot(fig12)

    st.subheader("🔹 Duration vs Subscribers (Colored by Level)")
    fig13, ax13 = plt.subplots()
    sns.scatterplot(data=df, x="content_duration", y="num_subscribers", hue="level", alpha=0.6, ax=ax13)
    ax13.set_title("Course Duration vs Subscribers by Level")
    st.pyplot(fig13)
