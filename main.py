import sys
from src.database import load_car_data
from src.interface import search_cars

def main():
    DATA_PATH = 'data/fullGas.csv'
    
    try:
        df = load_car_data(DATA_PATH)
        search_cars(df)
    except FileNotFoundError as e:
        print(f"Critical Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()