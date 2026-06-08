from turtle import *


class Car:
    def __init__(self, speed, color, fname):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)

    def drive(self, distance):
        self.turtle.forward(distance)

    def left_turn(self, degree):
        self.turtle.left(degree)

    def move(self, distance, degree):
        self.drive(distance)
        self.left_turn(degree)


register_shape("D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif")
register_shape("D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차2.gif")

myCar = Car(
    0, "red", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
)
yourCar = Car(
    0, "blue", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차2.gif"
)

for i in range(4):
    myCar.move(300, 90)
    yourCar.move(100, 60)
