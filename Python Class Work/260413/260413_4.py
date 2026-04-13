def food():
    response = "아니"

    while response == "아니":
        response = input("엄마, 다 됬어?")
    print("먹자")


def countChk():
    cnt = 0

    while True:
        cnt += 1
        print(cnt)
        if cnt == 200:
            break


def lightChk():
    while True:
        light = input("신호등 색상을 입력하시오.: ")
        if light == "blue":
            break
    print("전진")
