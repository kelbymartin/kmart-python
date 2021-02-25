class Car():

    wheels = 4
    doors = True

    def __init__(self, color, make, year, hpp):
        self.color = color
        self.make = make
        self.year = year
        self.hpp = hpp

    def start_car(self):
        print("Vrooooom")

    #Defines what print(car) will do
    def __str__(self):
        return self.make

    #Defines how comparison will act
    def __gt__(self, other):
        return self.hpp > other.hpp

my_car = Car("Blue", "Ford", 2020, 150)
your_car = Car("Red", "Tesla", 2020, 200)

my_car.start_car()

print(my_car > your_car)