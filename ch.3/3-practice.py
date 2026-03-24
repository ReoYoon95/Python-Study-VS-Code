# 실습문제 1

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")
# #여기서 참인 것은 shirt 와 need, 그러나 shirt가 먼저이기에 shirt만 출력됌.

# 실습문제2
# whiel문 이용 1~1000까지의 자연수중 3의배수의 합

i = 1
result = 0
while i <= 1000:
    if i % 3 == 0:
        result += i
        i += 1
    else:
        i += 1
print(result)

# for문으로 한다면??

result = 0
for i in range(3, 1001, 3):
    result += i
print(result)

# sum()사용 한다면??

print(sum(range(3, 1001, 3)))


# 실습문제 3
# 와일문을 사용하여 아래의 그림을 만들어라.
# *
# **
# ***
# ****
# *****

i = 1
lv = 1
while i == lv and lv < 6:
    print(f"*" * i)
    i += 1
    lv += 1


# #for 문 사용하여 만들기

for i in range(1, 6):
    print("*" * i)
