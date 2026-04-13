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

# =====================================

guguList1 = [f"{i}단" for i in range(1, 11)]


def gugudan1():
    print("--- 구구단 프로그램 (종료하려면 'q'를 입력하세요) ---")

    while True:
        # 키보드로부터 단 입력 받기
        response = input('원하는 단을 "x단" 형식으로 입력하시오: ')

        # q 입력 시 프로그램 종료
        if response == "q":
            print("프로그램을 종료합니다.")
            break

        # 입력한 단이 리스트에 있는지 확인
        if response in guguList1:
            # 2단부터 5단 사이인지 확인
            # (문자열에서 숫자만 쏙 빼서 비교합니다)
            dan_num = int(response.replace("단", ""))

            if 2 <= dan_num <= 5:
                print(f"\n[ {response} 출력 ]")
                for i in range(1, 10):
                    print(f"{dan_num} * {i} = {dan_num * i}")
                print()  # 가독성을 위해 한 줄 띄움
            else:
                # 리스트에는 있지만 2~5단이 아닌 경우
                print("2단부터 5단 사이의 단만 출력 가능합니다.\n")
        else:
            # 리스트에 아예 없는 단을 입력한 경우
            print("원하는 단은 리스트에 없습니다. 다시 입력해주세요.\n")


# =============================

gugulist2 = [f"{i}단" for i in range(1, 10)]


def gugudan2():
    print("구구단을 종료하려면 'q'를 입력하시오.")

    while True:
        response = input(f'원하는 단을 "x"단 형식으로 입력하시오')

        if response == "q":
            print("프로그램을 종료합니다.")
            break

        if response in gugulist2:
            dan_num = int(response.replace("단", ""))

            if 2 <= dan_num <= 5:
                print(f"\n[ {response} 출력 ]")
                for i in range(1, 10):
                    print(f"{dan_num} * {i} = {dan_num * i}")
                print()  # 가독성을 위해 한 줄 띄움
            else:
                # 리스트에는 있지만 2~5단이 아닌 경우
                print("2단부터 5단 사이의 단만 출력 가능합니다.\n")
        else:
            # 리스트에 아예 없는 단을 입력한 경우
            print("원하는 단은 리스트에 없습니다. 다시 입력해주세요.\n")
