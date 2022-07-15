class Car:
    def __init__(self, color, year):
        self.color = color
        self.year = year
        self.mileage = 0

    def is_we_need_tech(self):
        if self.mileage >= 10000:
            print("Срочно нужно то!")
        elif self.mileage > 7000:
            print(f"ТО через {10000 - self.mileage} км")
        else:
            print("все ок")

    def trip(self, distance):
        self.mileage += distance


car1 = Car("GREEN", 2022)

for i in range(12):
    car1.trip(1000)
    car1.is_we_need_tech()
