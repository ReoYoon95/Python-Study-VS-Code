print("Hello, World!")

name = "Reo"
print(f"My name is {name}")

introduce = f"hi, my name is {name}"

age = 20

print(f"i am {age:05d} years old") # 5자리로 출력, 빈칸은 0으로 채움. age가 20이므로 00020으로 출력됨
print(f"i am {age:-<5d} years old") # 왼쪽 정렬, 총 5자리, 빈칸은 -로 채움
print(f"i am {age:*^5d} years old\n") # 가운데 정렬, 총 5자리, 빈칸은 *로 채움

name1 = "철수"
score1 = 95
# C 스타일: %s(문자열), %d(정수)
print("이름: %s, 점수: %d점" % (name1, score1))

pi = 3.141592653589793
print(f"{pi:.2f}") # 소수점 아래 2자리까지 출력, 반올림하여 3.14로 표시

print(f"pi : {pi:$<10.2f}") # 왼쪽 정렬, 총 10자리, 소수점 아래 2자리, 빈칸은 $로 채움