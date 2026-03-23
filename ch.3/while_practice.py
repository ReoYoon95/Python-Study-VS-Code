# 여러줄 문자열 사용하기 """ """로 여러 줄 문자열을 만들 수 있다.
# 1. 메뉴판 디자인 (보이는 그대로 출력됨)
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0

# 2. 4번(Quit)을 누르기 전까지 무한 반복
while number != 4:
    print(prompt)  # 메뉴판을 화면에 뿌려줌
    number = int(input())  # 사용자에게 숫자를 입력받음

    # 입력받은 숫자에 따라 분기 처리 (나중에 채울 부분)
    if number == 1:
        print("데이터를 추가합니다.")
    elif number == 2:
        print("데이터를 삭제합니다.")
    elif number == 3:
        print("목록을 보여줍니다.")

print("안녕히 가세요!")
