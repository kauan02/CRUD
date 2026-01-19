from fuzzywuzzy import fuzz
from src.models import Car

def search_cars(df):
    filtered_df = df.copy()

    while True:
        print(f"\nCars currently found: {len(filtered_df)}")
        
        filter_opt = int(input("\nChoose your filter:\n1 - Make\n2 - Model\n3 - Body\n4 - Mileage (Max)\n5 - Price (Max)\n6 - Year (Min)\n7 - Country\n8 - Condition\n9 - Full Service History\n10 - Non Smoker Vehicle\n0 - SHOW RESULTS AND EXIT\n\nYour choice: "))
        
        if filter_opt == 0:
            print('Generating car list...')
            break
            
        elif filter_opt == 1:
            val = input("Enter Make: ").lower()
            filtered_df = filtered_df[filtered_df['make'].str.lower() == val]            
            
        elif filter_opt == 2:
            val = input("Enter Model: ").lower()
            filtered_df = filtered_df[filtered_df['model'].str.lower().str.contains(val)]
            
        elif filter_opt == 3:
            val = input("Enter Body type: ").lower()
            filtered_df = filtered_df[filtered_df['body'].str.lower() == val]
            
        elif filter_opt == 4:
            val = int(input("Enter MAXIMUM Mileage: "))
            filtered_df = filtered_df[filtered_df['mileage_km'] <= val]
            
        elif filter_opt == 5:
            val = int(input("Enter MAXIMUM Price: "))
            filtered_df = filtered_df[filtered_df['price'] <= val]
            
        elif filter_opt == 6:
            val = int(input("Enter MINIMUM Year: "))
            filtered_df = filtered_df[filtered_df['year'] >= val]
            
        elif filter_opt == 7:
            val = input("Enter Country: ").lower()
            filtered_df = filtered_df[filtered_df['country'].str.lower() == val]
            
        elif filter_opt == 8:
            val = input("Enter Condition: ").lower()
            filtered_df = filtered_df[filtered_df['condition'].str.lower() == val]
            
        elif filter_opt == 9:
            val = input("Full Service History? (yes/no): ").lower()
            filtered_df = filtered_df[filtered_df['full_service_history'].astype(str).str.lower() == val]
            
        elif filter_opt == 10:
            val = input("Non-Smoker Vehicle? (yes/no): ").lower()
            filtered_df = filtered_df[filtered_df['non_smoker_vehicle'].astype(str).str.lower() == val]
            
        else:
            print("Invalid option.")
            
        if filtered_df.empty:
            print("\nNo cars found with these filters!")
            return

    cars = []
    
    for _, row in filtered_df.iterrows():
        car = Car(
            make=row['make'],
            model=row['model'],
            body=row['body'],
            mileage=row['mileage_km'],
            price=row['price'],
            year=row['year'],
            country=row['country'],
            condition=row['condition'],
            fuel_type=row['fuel_type'],
            fuel_consumption=row['fuel_consumption_l'],
            drivetrain=row['drivetrain'],
            gearbox=row['gearbox'],
            power_hp=row['power_hp'],
            seats=row['seats'],
            doors=row['doors'],
            full_service_history=row['full_service_history'],
            non_smoker_vehicle=row['non_smoker_vehicle'],
            previous_owners=row['previous_owners'],
            seller=row['seller'],
            image_url=row['image_url']
        )
        cars.append(car)
        print("-" * 50)
        print(car.display_info()) 
    
    print("-" * 50)