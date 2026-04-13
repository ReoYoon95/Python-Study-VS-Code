# 구구단출력

# 리스트에 10개의 단을 입력
# 키보드로 부터 입력한 단이 리스트에 있고 2단부터 5단사이에 이면 입력된 단의 구구단 출력
# 출력 없으면 원하는단은 메세지 출력
# q입력시 프로그램 종료


def gugudan():
    response = input('원하는 단을 "x단" 이렇게 입력하시오.')
    while response != "q":

        if response in guguList:
            if (
                response == "2단"
                or response == "3단"
                or response == "4단"
                or response == "5단"
            ):
                for i in range(1, 10):
                    print(f"{response[0]} * {i} = {int(response[0]) * i}")
                # gugudan()
            else:
                print("2~5단이 아닙니다.")
                # break
        response = input('원하는 단을 "x단" 이렇게 입력하시오.')


guguList = []

for i in range(1, 11):
    guguList.append(f"{i}단")
    for j in range(1, 10):
        guguList.append(f"{i} * {j} = {i * j}")

gugudan()
