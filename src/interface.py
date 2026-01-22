from rapidfuzz import process, utils
from src.models import Car

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def apply_fuzzy_filter(df, column, query, threshold=80):
    choices = df[column].unique().tolist()
    match = process.extractOne(query, choices, processor=utils.default_process)
    
    if match and match[1] >= threshold:
        corrected_value = match[0]
        return df[df[column].str.lower() == corrected_value.lower()]
    return df[df[column].str.lower().str.contains(query.lower())]

def search_cars(df):
    filtered_df = df.copy()

    while True:
        print(f"\nResults found: {len(filtered_df)}")
        print("\n0 - EXIT & SHOW\n1 - Make\n2 - Model\n3 - Max Price\n4 - Min Year")
        
        choice = input("\nSelect filter: ")

        if choice == '0':
            break
        
        elif choice == '1':
            val = input("Enter Make: ")
            filtered_df = apply_fuzzy_filter(filtered_df, 'make', val)
            
        elif choice == '2':
            val = input("Enter Model: ")
            filtered_df = filtered_df[filtered_df['model'].str.contains(val, case=False)]

        elif choice == '3':
            val = get_valid_int("Max Price: ")
            filtered_df = filtered_df[filtered_df['price'] <= val]

        elif choice == '4':
            val = get_valid_int("Min Year: ")
            filtered_df = filtered_df[filtered_df['year'] >= val]

        if filtered_df.empty:
            print("No cars match these criteria. Resetting...")
            filtered_df = df.copy()

    for _, row in filtered_df.iterrows():
        car = Car(**row.to_dict())
        print("-" * 30)
        print(car)