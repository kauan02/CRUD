from src.database import load_car_data
from src.interface import search_cars

if __name__ == "__main__":
    df = load_car_data()
    
    search_cars(df)