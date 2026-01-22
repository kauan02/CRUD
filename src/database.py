import pandas as pd
import os

def load_car_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Database file not found at: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.lower()
        return df.dropna(subset=['make', 'model', 'price'])
    except Exception as e:
        raise Exception(f"Error loading CSV: {e}")