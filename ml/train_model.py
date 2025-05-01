# train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
#train_model.py
# Load data
df = pd.read_csv(r"D:/python/PythonX/udemy_courses.csv")
df['published_timestamp'] = pd.to_datetime(df['published_timestamp'], errors='coerce')
df['published_timestamp'] = df['published_timestamp'].dt.tz_localize(None)

# Feature Engineering
current_date = pd.Timestamp.now()
df['course_age_days'] = (current_date - df['published_timestamp']).dt.days
df['engagement_score'] = df['num_reviews'] * df['num_lectures']
df['review_rate'] = df['num_reviews'] / (df['num_subscribers'] + 1)
df['lectures_per_day'] = df['num_lectures'] / (df['course_age_days'] + 1)

# Select features
features = ['price', 'num_reviews', 'num_lectures', 'course_age_days',
            'engagement_score', 'review_rate', 'lectures_per_day']

df_model = df.dropna(subset=features + ['num_subscribers']).copy()
X = df_model[features]
y = df_model['num_subscribers']

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X, y)

# Save the model and column names
# Ensure the model directory exists
import os

# Set model save path
model_dir = r"D:\python\PythonX\model"
os.makedirs(model_dir, exist_ok=True)

# Save the model and column names
joblib.dump(model, os.path.join(model_dir, "random_forest_model.pkl"))
joblib.dump(features, os.path.join(model_dir, "model_features.pkl"))

print(f"✅ Model trained and saved to '{model_dir}\\random_forest_model.pkl'")