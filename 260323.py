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
