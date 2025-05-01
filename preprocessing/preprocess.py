# Preprocess module
import pandas as pd

def load_and_preprocess_data():
    df = pd.read_csv("udemy_courses.csv")
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df