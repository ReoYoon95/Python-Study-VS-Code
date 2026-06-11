from typing import Any


class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        self.speed = 60
        print("주행중입니다.")

    def stop(self):
        self.speed = 0
        print("정지했습니다.")


myCar = Car(0, "white")

print(f"myCar color = {myCar.color}")
print(f"myCar speed = {myCar.speed}")

myCar.drive()
print(f"myCar speed = {myCar.speed}")
myCar.stop()
print(f"myCar speed = {myCar.speed}")
