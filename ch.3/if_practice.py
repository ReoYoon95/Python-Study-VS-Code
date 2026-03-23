# 조건부 표현식

score = 85
if score >= 60:
    result = "합격"
else:
    result = "불합격"
print(result)


# 이런 간단한 조건 분기는 파이썬의 조건부 표현식을 사용하면 한 줄로 표현할 수 있다.

score = 85
result = "합격" if score >= 60 else "불합격"
print(result)


# match-case 문
grade = "B"
match grade:
    case "A":
        print("탁월한 성적입니다.")
    case "B":
        print("우수한 성적입니다.")
    case "C":
        print("보통입니다.")
    case _:
        print("노력이 필요합니다.")


# 여러패턴을 하나에 case로 묶을 수 있다.
grade = "B"
match grade:
    case "A" | "B" | "C":
        print("합격입니다.")
    case _:
        print("불합격입니다.")
