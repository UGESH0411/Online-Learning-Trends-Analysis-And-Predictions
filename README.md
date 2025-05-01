# 📊 Online Learning Trends Analysis and Predictions

This project is a comprehensive data-driven web application that analyzes and predicts trends in online learning platforms using machine learning and interactive visualizations. Built with **Streamlit**, it allows users to explore course data, gain insights, visualize patterns, and forecast trends in online education.

---

## 🚀 Features

- 📈 **Data Overview** – Summarizes key statistics like course count, categories, and price distribution.
- 🔍 **Filtering Module** – Enables dynamic filtering by category, price, level, and more.
- 💡 **Insight Generator** – Provides actionable insights based on data trends.
- 📊 **Visualizations** – Interactive graphs for category distribution, ratings, enrollments, etc.
- 🤖 **Machine Learning** – Predicts course success using Random Forest models.
- 🔮 **Forecasting** – Time-series trend forecasting for enrollment and popularity.
- 📚 **Learning Curve** – Shows model training performance over time.

---

## 🧪 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly
- **Machine Learning**: Random Forest, Train/Test split
- **Model Deployment**: Pretrained model with `.pkl` integration

---

## 📁 Project Structure

```bash
├── app.py                     # Main Streamlit application
├── createstruct.py            # App layout structure
├── eda/
│   ├── overview.py            # Dataset overview
│   ├── filtering.py           # Course filtering logic
│   ├── insights.py            # Key insights
│   └── visualization.py       # Plots and visualizations
├── ml/
│   ├── train_model.py         # Model training script
│   ├── predict.py             # Model prediction logic
├── preprocessing/
│   └── preprocess.py          # Data cleaning and processing
├── model/
│   ├── random_forest_model.pkl    # Trained ML model
│   └── model_features.pkl         # Feature mapping
├── udemy_courses.csv          # Dataset file
├── requirements.txt           # Required Python packages
└── README.md
