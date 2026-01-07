import pandas as pd

fullGas = 'data/fullGas.csv'
df = pd.read_csv(fullGas)
df.columns = df.columns.str.lower()

class Car:
    def __init__(self, make, model, body, miliage, price, year, country, condition, fuel_type, fuel_consumption, drivetrain, gearbox, power_hp, seats, doors, full_service_history, non_smoker_vehicle, previous_owners, seller, image_url):
        self.make = make
        self.model = model
        self.body = body
        self.miliage = miliage
        self.price = price
        self.year = year
        self.country = country
        self.condition = condition
        self.fuel_type = fuel_type
        self.consumo = fuel_consumption
        self.drivetrain = drivetrain
        self.gearbox = gearbox
        self.power_hp = power_hp
        self.seats = seats
        self.doors = doors
        self.full_service_history = full_service_history
        self.non_smoker_vehicle = non_smoker_vehicle
        self.previous_owners = previous_owners
        self.seller = seller
        self.image_url = image_url
        
    def display_info(self):
        info = f"Make: {self.make}\nModel: {self.model}\nBody: {self.body}\nMiliage: {self.miliage}\nPrice: {self.price}\nYear: {self.year}\nCountry: {self.country}\nCondition: {self.condition}\nFuel Type: {self.fuel_type}\nFuel Consumption: {self.consumo}\nDrivetrain: {self.drivetrain}\nGearbox: {self.gearbox}\nPower (HP): {self.power_hp}\nSeats: {self.seats}\nDoors: {self.doors}\nFull Service History: {self.full_service_history}\nNon-Smoker Vehicle: {self.non_smoker_vehicle}\nPrevious Owners: {self.previous_owners}\nSeller: {self.seller}\nImage URL: {self.image_url}"
        return info
    
def search_cars_by_make(df):
    while True:
        filter = int(input("Choose your filter\n\nOptions:\n\n1 - Make\n2 - Model\n3 - Body\n4 - Mileage\n5 - Price\n6 - Year\n7 - Country\n8 - Condition\n9 - Full Service History\n10 - Non Smoker Vehicle\n\nEnter your choice (1-10) or zero to skip filtering: "))
        if filter >= 1 and filter <=10:
            if filter == 1:
                make = input("Enter the car make: ").lower()
            elif filter == 2:
                model = input("Enter the car model: ").lower()
            elif filter == 3:
                body = input("Enter the car body type: ").lower()
            elif filter == 4:
                mileage = int(input("Enter the maximum mileage (km): "))
            elif filter == 5:
                price = int(input("Enter the maximum price: "))
            elif filter == 6:
                year = int(input("Enter the minimum year: "))
            elif filter == 7:
                country = input("Enter the country: ").lower()
            elif filter == 8:
                condition = input("Enter the car condition: ").lower()
            elif filter == 9:
                full_service_history = input("Does the car have a full service history? (yes/no): ").lower()
            elif filter == 10:
                non_smoker_vehicle = input("Is the car a non-smoker vehicle? (yes/no): ").lower()
        else:
            print('Researching cars...')
            break
    
    filtered_df = df[df['make'].str.lower() == make]
    cars = []
    for _, row in filtered_df.iterrows():
        car = Car(
            make=row['make'],
            model=row['model'],
            body=row['body'],
            miliage=row['mileage_km'],
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
        print(car.display_info()) 
        print("-" * 160)
        

search_cars_by_make(df)