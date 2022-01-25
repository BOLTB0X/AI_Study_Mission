class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels

#상속이용
class Bike(Car):
    def __init__(self, fuel, wheels, size):
        super().__init__(fuel, wheels) #부모 객체 사용
        self.fuel = fuel
        self.wheels = wheels
        self.size = size

bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)