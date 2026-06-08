from turtle import *


class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape(
            "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
        )

    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

    def move(self, num):
        for i in range(num):
            self.drive()
            self.left_turn()


register_shape("D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif")
myCar = Car(200, "red", "E-Class")
myCar.move(100)
