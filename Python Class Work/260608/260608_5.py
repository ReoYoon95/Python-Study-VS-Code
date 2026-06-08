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

car1 = Car(
    0, "red", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
)
car2 = Car(
    0, "blue", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차2.gif"
)
car3 = Car(
    0, "blue", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차2.gif"
)
car4 = Car(
    0, "blue", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차2.gif"
)
car5 = Car(
    0, "blue", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차2.gif"
)
car6 = Car(
    0, "red", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
)
car7 = Car(
    0, "red", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
)
car8 = Car(
    0, "red", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
)
car9 = Car(
    0, "red", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
)
car10 = Car(
    0, "red", "D:\\VS Code File\\python Study\\Python Class Work\\260608\\자동차.gif"
)

for i in range(4):
    car1.move(300, 90)
    car2.move(100, 60)
    car3.move(150, 30)
    car4.move(170, 65)
    car5.move(40, 69)
    car6.move(150, 10)
    car7.move(130, 30)
    car8.move(70, 60)
    car9.move(77, 60)
    car10.move(105, 40)
