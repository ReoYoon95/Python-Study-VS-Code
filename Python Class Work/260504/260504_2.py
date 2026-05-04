import turtle
import math
import random

player = turtle.Turtle()
player.shape("turtle")
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)  # 화면의 크기를 800×600으로 한다.
player.color("yellow")

player.goto(-300, 0)
velocity = 70  # 초기속도 70픽셀/sec
player.left(45)


def turnleft():
    player.left(5)


def turnright():
    player.right(5)


def turnup():
    global velocity
    velocity += 10


def turndown():
    global velocity
    velocity -= 10


def fire():
    x = -300
    y = 0
    player.color(random.random(), random.random(), random.random())
    player.goto(x, y)
    angle = player.heading()
    vx = velocity * math.cos(angle * 3.14 / 180.0)
    vy = velocity * math.sin(angle * 3.14 / 180.0)

    while player.ycor() >= 0:
        vx = vx
        vy = vy - 10
        x = x + vx
        y = y + vy
        player.goto(x, y)
        player.stamp()


screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(turnup, "Up")
screen.onkeypress(turndown, "Down")
screen.onkeypress(fire, "space")

screen.listen()
turtle.mainloop()
