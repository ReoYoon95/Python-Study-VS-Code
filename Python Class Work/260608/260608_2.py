class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        self.speed = 60
        print(f"주행중입니다.")

    def checkInfo(self, speed, color):
        print(f"{self} speed = {self.speed}")
        print(f"{self} color = {self.color}")


myCar = Car(60, "green")
print(f"myCar speed = {myCar.speed}")
print(f"myCar color = {myCar.color}")
myCar.checkInfo(myCar.speed, myCar.color)

momCar = Car(70, "silver")
print(f"momCar speed = {momCar.speed}")
print(f"momCar color = {momCar.color}")

dadCar = Car(30, "yellow")
print(f"dadCar speed = {dadCar.speed}")
print(f"dadCar color = {dadCar.color}")

myCar.drive()
print(f"myCar speed = {myCar.speed}")
momCar.drive()
print(f"myCar speed = {momCar.speed}")
dadCar.drive()
print(f"myCar speed = {dadCar.speed}")
