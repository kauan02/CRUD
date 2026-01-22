class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.body = kwargs.get('body')
        self.mileage = kwargs.get('mileage_km')
        self.price = kwargs.get('price')
        self.year = kwargs.get('year')
        self.country = kwargs.get('country')
        self.condition = kwargs.get('condition')
        self.fuel_type = kwargs.get('fuel_type')
        self.fuel_consumption = kwargs.get('fuel_consumption_l')
        self.drivetrain = kwargs.get('drivetrain')
        self.gearbox = kwargs.get('gearbox')
        self.power_hp = kwargs.get('power_hp')
        self.seats = kwargs.get('seats')
        self.doors = kwargs.get('doors')
        self.full_service_history = kwargs.get('full_service_history')
        self.non_smoker_vehicle = kwargs.get('non_smoker_vehicle')
        self.previous_owners = kwargs.get('previous_owners')
        self.seller = kwargs.get('seller')
        self.image_url = kwargs.get('image_url')

    def __str__(self):
        details = [f"{k.replace('_', ' ').title()}: {v}" for k, v in vars(self).items()]
        return "\n".join(details)