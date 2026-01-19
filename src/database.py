import pandas as pd    

def load_car_data():
    fullGas = 'data/fullGas.csv'
    df = pd.read_csv(fullGas)
    df = df.dropna()
    df.columns = df.columns.str.strip().str.lower()
    return df