test_list = ["one", "two", "three"]
for i in test_list:
    print(i)


a = [(1, 2), (3, 4), (5, 6)]
for first, last in a:
    print(first + last)


marks = [90, 25, 67, 45, 80]  # 학생들의 시험 점수 리스트

number = 0  # 학생에게 붙여 줄 번호
for mark in marks:  # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


# 리스트 컴프리헨션
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

# 리스트 컴프리헨션을 사용하면 위의 코드를 한 줄로 표현할 수 있다.
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
# num이 a의 요소를 순서대로 num에 대입하여 num * 3을 result 리스트에 추가한다. 단, num이 짝수인 경우에만 추가한다.
print(result)


# enumerate() 함수는 리스트와 같은 순회 가능한(iterable) 객체를 입력으로 받아 인덱스와 요소를 튜플 형태로 반환하는 함수이다.

fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 0: apple
# 1: banana
# 2: orange
# enumerate는 0부터 시작하는 인덱스 번호를 자동으로 생성해 준다. 시작 번호를 변경하고 싶다면 다음과 같이 사용할 수 있다.

fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits, 1):  # 1부터 시작
    print(f"{i}: {fruit}")

# 1: apple
# 2: banana
# 3: orange


# zip 함수를 사용하여 두 개 이상의 리스트를 동시에 순회한다.

names = ["홍길동", "김철수", "이영희"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# 홍길동: 85점
# 김철수: 92점
# 이영희: 78점


# 세 개 이상의 리스트도 함께 순회할 수 있다.

names = ["홍길동", "김철수", "이영희"]
korean = [85, 92, 78]
english = [90, 88, 95]
for name, kor, eng in zip(names, korean, english):
    print(f"{name}: 국어 {kor}점, 영어 {eng}점")

# 홍길동: 국어 85점, 영어 90점
# 김철수: 국어 92점, 영어 88점
# 이영희: 국어 78점, 영어 95점
