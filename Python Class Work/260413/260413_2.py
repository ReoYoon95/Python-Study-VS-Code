sum = 0


def sumAll():
    listA = [1, 2, 3, 4, 5]
    for i in listA:
        print(f"{i}를 더하는 중")
        sum += i
    print(f"합계는 : {sum}")


def sumOddEven():
    listA = [1, 2, 3, 4, 5]
    for i in listA:
        if (i % 2) == 1:
            print(f"{i}를 더하는 중")
            sumOdd = 0
            sumOdd += i
        else:
            sumEven = 0
            sumEven += i
    print(f"홀수합계는 : {sumOdd} 짝수합계는 : {sumEven}")
