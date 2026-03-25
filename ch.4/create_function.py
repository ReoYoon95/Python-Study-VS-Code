def sub(a, b):
    return a - b


a = sub(3, 1)
print(a)


def sub1(a, b):
    return a - b


result = sub(b=3, a=1)
print(result)


# *args : 함수의 매개변수로 입력받는 값의 개수가 정해지지 않았을 때 사용한다. 입력받은 값들은 튜플 형태로 저장된다.
def add_many(*args):
    result = 0
    for i in args:
        result = result + i  # *args에 입력받은 모든 값을 더한다
    return result


add_many(1, 2, 3, 4, 5)
print(add_many(1, 2, 3, 4, 5))


# **kwargs : 함수의 매개변수로 입력받는 값의 개수가 정해지지 않았을 때 사용한다. 입력받은 값들은 딕셔너리 형태로 저장된다.
def print_kwargs(**kwargs):
    print(kwargs)
    print(kwargs["a"])


print_kwargs(a=1, b=2, c=3)


# return 값은 하나만 반환할 수 있지만, 튜플 형태로 여러 값을 반환할 수 있다.
def add_and_mul(a, b):
    return a + b, a * b


a, b = add_and_mul(3, 4)

print(a)
print(b)
print(add_and_mul(3, 4))


# return 으로 함수를 끝내고 싶을떄
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)


# 3번쨰 파라미터는 트루이므로 이에 해당하면 기본값에 적용되어 입력하지 않아도 됌.
def say_myself(name, age, man=True):
    # 기본값이 지정된 매개변수는 항상 뒤에 위치해야 한다.
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("김철수", 20)
say_myself("김영희", 25, False)


# 지역변수와 전역변수

a = 1


def vartest(a):
    return a + 1  # or global a 후에 a = a + 1


a = vartest(a)  # 함수가 던져준 2를 다시 전역 변수 a에 대입!
print(a)  # 결과: 2


b = [1, 2, 3]


def vartest2(b: list):  # 아래 어팬드를 인식못해서 리스트형이다라고 써준 것.
    b.append(4)  # 상자 주소를 알고 있으므로, 직접 가서 4를 집어넣음!


vartest2(b)
print(b)  # 결과: [1, 2, 3, 4] (상자 내용물이 바뀌어 있음)


# 패션코딩 lambda : 함수를 간단히 표현할 수 있는 방법. 일반적으로 한 줄로 표현되는 간단한 함수를 만들 때 사용한다.


def add(a, b):
    return a + b


add = lambda a, b: a + b
result = add(3, 4)
print(result)

a = [lambda a, b: a + b, lambda a, b: a * b]
print(a[0](3, 4))  # 덧셈 결과 출력
print(a[1](3, 4))  # 곱셈 결과 출력
