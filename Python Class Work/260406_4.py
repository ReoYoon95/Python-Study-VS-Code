print("오렌지주스:0\t커피:1\t콜라:2\t탄산수:3\t")

num = int(input("음료를 선택하시오: "))

if num == 0:
    print("오렌지주스")

elif num == 1:
    print("커피")

elif num == 2:
    print("콜라")

elif num == 3:
    print("탄산수")

else:
    print("음료가 없습니다.")
