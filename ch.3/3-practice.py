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

