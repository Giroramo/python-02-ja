# ここにコードを書いてください

from abc import ABC, abstractmethod

# 抽象基底クラスの定義
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def get_details(self):
        pass

# Carクラスの定義
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def get_details(self):
        return f"Car: {self.year} {self.make} {self.model}"

# Truckクラスの定義
class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_details(self):
        return f"Truck: {self.year} {self.make} {self.model}, Towing Capacity: {self.towing_capacity}"

# display_vehicle_details関数の定義
def display_vehicle_details(vehicle):
    print(vehicle.get_details())

# 使用例
car = Car(make="Toyota", model="Corolla", year=2021)
truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)

print(car.get_details())  # Car: 2021 Toyota Corolla
print(truck.get_details())  # Truck: 2020 Ford F-150, Towing Capacity: 5000

display_vehicle_details(car)  # Car: 2021 Toyota Corolla
display_vehicle_details(truck)  # Truck: 2020 Ford F-150, Towing Capacity: 5000


def get_vehicle_details(vehicle):
    # ここにコードを書いてください
    pass
