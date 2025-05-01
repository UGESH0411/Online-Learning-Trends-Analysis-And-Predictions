import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
#predit.py
def show_prediction(df):
# Page title
    st.title("📈 ML & Forecasting")
    st.subheader("📅 Predict Most Popular Courses by Subject (Any Year)")

    # Load dataset
    df = pd.read_csv(r"D:/python/PythonX/udemy_courses.csv")

    # Convert timestamps
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'], errors='coerce')
    df['published_timestamp'] = df['published_timestamp'].dt.tz_localize(None)

    # Feature Engineering
    current_date = pd.Timestamp.now()
    df['course_age_days'] = (current_date - df['published_timestamp']).dt.days
    df['engagement_score'] = df['num_reviews'] * df['num_lectures']
    df['review_rate'] = df['num_reviews'] / (df['num_subscribers'] + 1)
    df['lectures_per_day'] = df['num_lectures'] / (df['course_age_days'] + 1)

    # Load trained model and features
    model_path = r"D:/python/PythonX/model/random_forest_model.pkl"
    features_path = r"D:/python/PythonX/model/model_features.pkl"

    if not os.path.exists(model_path) or not os.path.exists(features_path):
        st.error("❌ Trained model or features not found. Please run `train_model.py` first.")
        st.stop()

    model = joblib.load(model_path)
    features = joblib.load(features_path)

    # Prepare model data
    df_model = df.dropna(subset=features + ['num_subscribers']).copy()
    X = df_model[features]
    y = df_model['num_subscribers']

    # Year input
    selected_year = st.number_input("Enter a year (past, current, or future):", value=current_date.year + 1, step=1)

    # Course selector
    course_titles = df['course_title'].dropna().unique()
    course_input = st.selectbox("🔍 Select a course for 5-year forecast (optional):", [""] + sorted(course_titles))

    # ----------- Part 1: Predict Most Popular Courses by Subject -----------

    st.subheader(f"🏆 Predicted Most Popular Courses in {selected_year} (By Subject)")

    valid_rows = []
    metadata = []

    for _, row in df.dropna(subset=features).iterrows():
        if pd.isna(row['published_timestamp']):
            continue

        future_age = (pd.Timestamp(f"{selected_year}-01-01") - row['published_timestamp']).days
        if future_age < 0:
            continue

        lectures_per_day = max(0.001, row['num_lectures'] / (future_age + 1))
        valid_rows.append({
            'price': row['price'],
            'num_reviews': row['num_reviews'],
            'num_lectures': row['num_lectures'],
            'course_age_days': future_age,
            'engagement_score': row['engagement_score'],
            'review_rate': row['review_rate'],
            'lectures_per_day': lectures_per_day
        })
        metadata.append((row['course_title'], row['subject']))

    if valid_rows:
        input_df = pd.DataFrame(valid_rows)
        preds = model.predict(input_df)
        pred_df = pd.DataFrame(metadata, columns=["Course Title", "Subject"])
        pred_df["Predicted Subscribers"] = preds.astype(int)

        st.write(f"### 📚 Top Courses by Subject in {selected_year}")
        for subject in df['subject'].unique():
            subject_df = pred_df[pred_df['Subject'] == subject]
            if not subject_df.empty:
                top_course = subject_df.sort_values('Predicted Subscribers', ascending=False).iloc[0]
                st.markdown(
                    f"**{subject}**: 🏆 *{top_course['Course Title']}* — `{top_course['Predicted Subscribers']:,}` predicted subscribers"
                )
    else:
        st.warning("No valid predictions could be made for the selected year.")

    # ----------- Part 2: Forecast for a Specific Course -----------

    if course_input:
        st.subheader(f"📈 5-Year Subscriber Forecast for '{course_input}'")

        matching = df[df['course_title'].str.lower() == course_input.lower().strip()]
        if matching.empty:
            st.error("❌ Course not found. Please check the title.")
        else:
            row = matching.iloc[0]
            future_years = list(range(selected_year, selected_year + 5))
            forecast_data = []

            for year in future_years:
                future_age = (pd.Timestamp(f"{year}-01-01") - row['published_timestamp']).days
                lectures_per_day = max(0.001, row['num_lectures'] / (future_age + 1))
                forecast_data.append({
                    'price': row['price'],
                    'num_reviews': row['num_reviews'],
                    'num_lectures': row['num_lectures'],
                    'course_age_days': future_age,
                    'engagement_score': row['engagement_score'],
                    'review_rate': row['review_rate'],
                    'lectures_per_day': lectures_per_day
                })

            forecast_df = pd.DataFrame(forecast_data)
            preds = model.predict(forecast_df).astype(int)
            result_df = pd.DataFrame({
                "Year": future_years,
                "Predicted Subscribers": preds
            })

            st.line_chart(result_df.set_index("Year"))
            st.dataframe(result_df)

    # ----------- Part 3: Model Performance -----------

    st.subheader("📊 Model Performance on Training Data")

    y_pred_train = model.predict(X)
    r2 = r2_score(y, y_pred_train)
    mae = mean_absolute_error(y, y_pred_train)
    rmse = np.sqrt(mean_squared_error(y, y_pred_train))

    st.write("### 📈 Evaluation Metrics")
    st.write(f"🔹 **R² Score**: {r2:.4f}")
    st.write(f"🔹 **Mean Absolute Error (MAE)**: {mae:,.2f}")
    st.write(f"🔹 **Root Mean Squared Error (RMSE)**: {rmse:,.2f}")
