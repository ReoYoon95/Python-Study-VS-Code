import turtle
import random

score = 0

screen = turtle.Screen()
screen.tracer(0)  # 화면 업데이트 수동 설정
screen.addshape("d:\\VS Code File\\python Study\\Python Class Work\\260504\\rabbit.gif")


# 2. 플레이어(강아지) 설정
player = turtle.Turtle()
player.shape("d:\\VS Code File\\python Study\\Python Class Work\\260504\\rabbit.gif")


player.goto(-200, 200)
player.down()
player.goto(200, 200)
player.goto(200, -200)
player.goto(-200, -200)
player.goto(-200, 200)
player.up()
player.goto(0, 0)

# 3. 점수 표시용 터틀 설정
display = turtle.Turtle()
display.hideturtle()
display.penup()
display.goto(-210, 210)
display.write(f"점수={score}", font=("Arial", 20, "italic"))

# 4. 먹이(빵) 설정
bread = turtle.Turtle()
bread.shape("circle")
bread.color("brown")  # 빵 느낌을 위해 색상 추가
bread.penup()
x = random.randint(-180, 180)
y = random.randint(-180, 180)
bread.goto(x, y)


# 5. 이동 함수 정의
def moveRight():
    player.setheading(0)
    player.forward(15)


def moveLeft():
    player.setheading(180)
    player.forward(15)


def moveUp():
    player.setheading(90)
    player.forward(15)


def moveDown():
    player.setheading(270)
    player.forward(15)


# 6. 이벤트 연결
screen.listen()
screen.onkeypress(moveRight, "Right")
screen.onkeypress(moveLeft, "Left")
screen.onkeypress(moveUp, "Up")
screen.onkeypress(moveDown, "Down")

# 7. 메인 게임 루프
while True:
    # 충돌 감지 (강아지가 빵을 먹었을 때)
    if player.distance(bread) < 30:
        # 빵 위치 초기화
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        bread.goto(x, y)

        # 점수 업데이트
        score = score + 1
        display.clear()
        display.write(f"점수={score}", font=("Arial", 20, "italic"))

    screen.update()  # 화면을 업데이트한다.
