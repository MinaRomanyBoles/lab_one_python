# Problem 1: Vehicle Rental System (OOP - Beginner)

class Vehicle:
    total_vehicles = 0
    def __init__(self,vehicle_id , brand , model , rental_price_per_day , is_rented):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_rented = is_rented
        Vehicle.total_vehicles += 1
        
    def rent(self): # - Mark vehicle as rented:
        self.is_rented = True

    def return_vehicle(self): # - Mark vehicle as available
        self.is_rented = False
    
    def calculate_rental_cost(self, days):# - Calculate total cost
        return self.rental_price_per_day * days
    
    def get_details(self): #- Return vehicle information
        print(f"ID: {self.vehicle_id}, Brand: {self.brand}, Model: {self.model}, Price/Day: {self.rental_price_per_day}, Rented: {self.is_rented}")

class Car(Vehicle):
    def __init__(self, vehicle_id , brand , model , rental_price_per_day , num_doors):
        super().__init__(vehicle_id , brand , model , rental_price_per_day , False)
        self.num_doors = num_doors
        self.rental_price_per_day

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id , brand , model , rental_price_per_day , engine_cc):
        super().__init__(vehicle_id , brand , model , rental_price_per_day , False)
        self.engine_cc = engine_cc
        self.rental_price_per_day *= 0.7

class Truck(Vehicle):
    def __init__(self, vehicle_id , brand , model , rental_price_per_day , cargo_capacity_tons):
        super().__init__(vehicle_id , brand , model , rental_price_per_day , False)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.rental_price_per_day *= 1.5

car1 = Car("V001", "Toyota", "Camry", 50, 4)
motorcycle1 = Motorcycle("V002", "Harley", "Street 750", 40, 750)
truck1 = Truck("V003", "Ford", "F-150", 80, 2.5)
print(car1.rent())
car1.get_details()
motorcycle1.get_details()
truck1.get_details()
