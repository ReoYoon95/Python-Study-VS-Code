# A, B = map(int, input().split())
# print(f"나눗셈의 몫 = {A//B}")
# print(f"나눗셈의 나머지 = {A % B}")


# num = int(input("정수를 입력하시오: "))
# print(f"{num % 2}")


# sec = int(input("초를 입력하시오: "))
# min = sec // 60
# sec = sec % 60
# print(f"입력하신 시간은 {min}분 {sec}초 입니다.")


# print(2**7)
# print(16**0.5)
# print(pow(2,7))


# pow(a, b, c)
# (2의 7승)을 10으로 나눈 나머지는?
# print(pow(2, 7, 10))  # 결과: 8 (128 % 10)


# money = 10000000
# rate = 0.06
# n = 5
# print(f"5년 후의 원리금 합계 = {int(money*(1+rate)**n):,}")
# 특정값 다음에 :,를 붙이면 천 단위 구분 기호가 추가됨. 10000000이 10,000,000으로 출력됨


# x = 1000
# print(f"초기값 x = {x}")

# x += 2
# print(f"x += 2의 결과 = {x}")

# x -= 2
# print(f"x -= 2의 결과 = {x}")


# x, y, z = map(int, input("세 개의 정수를 한칸식 띄어서 입력하시오 : (예시 4 5 6) :").split())
# avr = (x + y + z) / 3
# print(f"세 정수의 평균은 {avr:.2f}입니다.")


# ==================================================
# 매출 단순 계산기

americano = 0
latte = 0
cappuccino = 0
part_time = 0

price_americano = 2000
price_latte = 3000
price_cappuccino = 2500
pay_part_time = 11000

americano, latte, cappuccino, part_time = map(
    int,
    input(
        "아메리카노, 라떼, 카푸치노, 아르바이트 시간을 한칸씩 띄어서 입력하시오 : (예시 3 4 5 6) :"
    ).split(),
)

income = (
    (americano * price_americano)
    + (latte * price_latte)
    + (cappuccino * price_cappuccino)
    - (part_time * pay_part_time)
)

print(f"총 매출은 {income:,}원입니다.")


# ==================================================
# 딕셔너리를 이용한 방법

# 1. 메뉴와 가격을 딕셔너리로 묶기 (Key: Value)
prices = {"americano": 2000, "latte": 3000, "cappuccino": 2500, "pay_part_time": 11000}

# 2. 입력 받기 (언패킹 활용)
a_cnt, l_cnt, c_cnt, p_time = map(
    int, input("아메리카노, 라떼, 카푸치노, 알바시간 입력 (예: 3 4 5 6): ").split()
)

# 3. 계산 (딕셔너리에서 값을 꺼내와서 계산)
income = (
    (a_cnt * prices["americano"])
    + (l_cnt * prices["latte"])
    + (c_cnt * prices["cappuccino"])
    - (p_time * prices["pay_part_time"])
)

print(f"총 매출은 {income:,}원입니다.")


# ==================================================
# 튜플과 zip 함수를 활용한 고급 기술 (C언어의 병렬 배열 처리)

# 1. 가격 뭉치 (튜플)
prices = (2000, 3000, 2500, -11000)  # 시급은 빼야 하니까 마이너스로!

# 2. 입력받은 개수 뭉치 (리스트)
counts = list(map(int, input("아메리카노, 라떼, 카푸치노, 알바시간 입력: ").split()))

# 3. zip으로 묶어서 한 번에 계산
total_income = 0
for p, c in zip(prices, counts):
    total_income += p * c

print(f"최종 수익: {total_income:,}원")


# zip 과 enumerate를 활용한 고급 기술 (C언어의 병렬 배열 처리)

prices = [2000, 3000, 2500]
counts = [3, 4, 5]

# zip으로 묶은 덩어리를 enumerate가 다시 번호를 매깁니다.
for i, (p, c) in enumerate(zip(prices, counts)):
    print(f"상품 {i+1}: {p}원 x {c}개 = {p*c}원")
