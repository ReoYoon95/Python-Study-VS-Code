import copy

#1번 문제
print("1번문제")
Hong_score = {"국어" : 80, "영어" : 75, "수학" : 55}
print(sum(Hong_score.values()) / len(Hong_score))

#2번 문제
print("2번문제")
a = 13
if a % 2 == 0:
    print("짝수")
else:
    print("홀수")

#3번 문제
print("3번문제")
Hong_pin = "881120-1068234"
front_num = Hong_pin[:6]
back_num = Hong_pin[7:]
print(front_num)
print(back_num)

#4번 문제
print("4번문제")
pin_num = "881120-1068234"
if pin_num[7] == "1" or pin_num[7] == "3":
    print("남자")
elif pin_num[7] == "2" or pin_num[7] == "4":
    print("여자")
else:
    print("잘못된 번호입니다.")

#5번 문제
print("5번문제")
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#6번 문제
print("6번문제")
a = [1, 3, 5, 4, 2]
print(sorted(a)) #sorted() 함수는 원본 리스트를 변경하지 않고 정렬된 새로운 리스트를 반환한다.
print(a)
a.sort() #sort() 메서드는 원본 리스트를 직접 변경하여 정렬한다.
a.reverse()
print(a)

#7번 문제
print("7번문제")
a = ['Life', 'is', 'too', 'short']
print(" ".join(a))

#8번 문제
print("8번문제")
a = (1, 2, 3)
b = (4,)
print(a + b)

#9번 문제 딕셔너리의 키
print("9번문제")
# >>> a = dict()
# >>> a
#a[[1]] = "python" #리스트는 변경 가능하지만 튜플은 변경 불가능하기 때문에 튜플의 요소를 변경하려고 하면 TypeError가 발생한다.

#10번 문제
print("10번문제")
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11번 문제
print("11번문제")
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
a_set = set(a)
print(list(a_set))

#12번 문제
print("12번문제")
a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)
# a와 b는 같은 리스트를 참조하기 때문에 a의 변경이 b에도 영향을 미친다.
# a와 b가 서로 다른 리스트를 참조하도록 하려면 a = [1, 2, 3]과 b = [1, 2, 3]으로 각각 새로운 리스트를 만들어야 한다.
a1 = [1, 2, 3]
b1 = a1[:]
#b = copy.copy(a) #copy 모듈의 copy() 함수를 사용하여 a의 얕은 복사본을 만들어 b에 할당할 수도 있다.
a1[1] = 4
print(a1)
print(b1)
