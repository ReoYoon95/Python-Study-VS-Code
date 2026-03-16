print("Hello, World!")

name = "Reo"
print(f"My name is {name}")

introduce = f"hi, my name is {name}"

age = 20

x = int(input("나이를 입력하세요: "))

print("i am {0} and {1} years old". format(name, x))
print(f"i am {x:05d} years old")
print(f"i am {x:-<5d} years old")
print(f"i am {x:*^5d} years old\n")

name1 = "철수"
score1 = 95
# C 스타일: %s(문자열), %d(정수)
print("이름: %s, 점수: %d점" % (name1, score1))

pi = 3.141592653589793
print(f"{pi:.2f}")

print(f"pi : {pi:$<10.2f}")

