def example1():
    myList = ["우유", "사과", "두부", "소고기"]
    myList[1] = "커피"

    print(myList)


def example2():
    myList = ["우유", "사과", "두부", "소고기"]
    print(myList)
    myList.insert(3, "커피")
    print(myList)


def example3():
    myList = ["우유", "사과", "두부", "소고기"]
    print(myList)
    myList.remove("소고기")
    print(myList)


def example4():
    myList = ["우유", "사과", "두부", "소고기"]
    if "소고기" in myList:
        myList.remove("소고기")
    print(myList)

    # 아래코드는 오류가뜸 오렌지가 마이리스트에 없기에.  따라서 위처럼 써야함
    myList = ["우유", "사과", "두부", "소고기"]
    print(myList)
    myList.remove("오렌지")
    print(myList)


def example5():
    myList = ["우유", "사과", "두부", "소고기"]
    if "소고기" in myList:
        i = myList.index("소고기")
        print(i)


def example6():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(min(numbers))  # 최소값은?
    print(max(numbers))  # 최대값은?
    print(sum(numbers))  # 총합은?


def example7():
    numbers = [9, 6, 7, 1, 8, 4, 5, 3, 2]
    numbers.sort()
    print(numbers)


# .sort 는 변수 자체를 바꾸는 거고 sorted()는 변수를 바꾸지말고 정렬한 상태로 나타내는 것이다.
def example8():
    numbers = [9, 6, 7, 1, 8, 4, 5, 3, 2]
    print(numbers)
    new_list = sorted(numbers)
    print(f"numbers : {numbers}")
    print(f"new_list : {new_list}")


def example9():
    phone_book = {"홍길동": "1234", "이순신": "1263", "강감찬": "3255"}
    print(phone_book)
    print(phone_book["이순신"])
    phone_book["이순신"] = "1111"
    print(phone_book)


def example10():

    phone_book = {}
    phone_book["이순신"] = "1234"
    phone_book["홍길동"] = "21222324"
    phone_book["강감찬"] = "55555"
    print(phone_book)
    print(phone_book.keys())
    print(phone_book.values())
    print(phone_book.items())
    for key, value in enumerate(sorted(phone_book)):
        print(f"key = {key}, value = {value}")
    phone_book.pop("홍길동")
    print(phone_book)
    phone_book.clear()
    print(phone_book)


# example1()
# example2()
# example3()
# example4()
# example5()
# example6()
# example7()
# example8()
# example9()
example10()
