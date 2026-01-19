class Car:
    def __init__(self, make, model, body, mileage, price, year, country, condition, fuel_type, fuel_consumption, drivetrain, gearbox, power_hp, seats, doors, full_service_history, non_smoker_vehicle, previous_owners, seller, image_url):
        self.make = make
        self.model = model
        self.body = body
        self.mileage = mileage
        self.price = price
        self.year = year
        self.country = country
        self.condition = condition
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
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
        info = f"Make: {self.make}\nModel: {self.model}\nBody: {self.body}\nMileage: {self.mileage}\nPrice: {self.price}\nYear: {self.year}\nCountry: {self.country}\nCondition: {self.condition}\nFuel Type: {self.fuel_type}\nFuel Consumption: {self.fuel_consumption}\nDrivetrain: {self.drivetrain}\nGearbox: {self.gearbox}\nPower (HP): {self.power_hp}\nSeats: {self.seats}\nDoors: {self.doors}\nFull Service History: {self.full_service_history}\nNon-Smoker Vehicle: {self.non_smoker_vehicle}\nPrevious Owners: {self.previous_owners}\nSeller: {self.seller}\nImage URL: {self.image_url}"
        return info
