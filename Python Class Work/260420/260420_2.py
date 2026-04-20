# 로또 번호 생성함수

# 로또 번호를 생성하는 함수를 작성하여 사용해보자. 로또 번호는 1부터 45까지 숫자 6개로 이루어진다. 따라서 6개의 난수를 생성하여야 한다.
# 번호는 중복되면 안 된다.
# 조건
# main 함수를 만든 후 main 함수에서 로또 번호 생성 함수 호출
# main 함수에서만 input 사용
#     키보드로 부터 로또 구매수량입력
#     입력한 수량만큼 로또 생성(5~10사이만 생성-논리연산사용)
#     "q"을 입력 하면 프로그램 종료


import random


def lottoCreate(n):
    if 5 <= n <= 10:
        print(f"로또 {n}장을 출력합니다.")
        for _ in range(n):
            lottoNum = sorted(random.sample(range(1, 46), 6))
            print(lottoNum)
    else:
        print("5장~10장사이로 구매할 수 있습니다.")


while True:
    n = input("구매수량을 입력하시오: ")
    if n == "q":
        break

    elif n.isdigit():
        n = int(n)

    else:
        continue

    lottoCreate(n)
