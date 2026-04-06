# # 연습3
# # 실수를 입력받아 학점을 표시하시오
# # a+ 100~95
# # a 94~90
# # b+ 89~85
# # b 84 80
# # f 79 ~전부
# # 조건
# #   입력은실수값입력
# #   중첩 if문 사용
# #   논리연산사용

score = int(input("점수를 입력하시오: "))

if score >= 95 and score <= 100:
    print("A+")
else:
    if 94 >= score >= 90:
        print("A")
    else:
        if 89 >= score >= 85:
            print("B+")
        else:
            if 84 >= score >= 80:
                print("B")
            else:
                print("F")
