## self의 정체는 무엇인가?

self는 '이 메서드를 호출한 객체 자신'을 가리키는 파이썬의 약속된 기호입니다.  
설계도(클래스) 안에서 "나중에 이 설계도로 만들어질 미래의 객체야, 네 안에 있는 변수에 접근해라"라고 말할 때 self.변수명 구조를 사용합니다.    

1. self의 개념과 역할"
    - self는 클래스 내부에서 **메소드를 호출한 '객체 자신'**을 가리키는 파이썬의 약속된 기호입니다. 설계도(클래스)를 작성할 때, 미래에 생성될 객체의 고유 변수(멤버 변수)나 메소드에 접근하기 위해 self.변수명, self.메소드명() 구조로 사용합니다."  

2. 메소드와 함수의 관계"
    - 메소드와 함수는 근본적으로 동일한 개념(이야기)입니다. 단지 클래스 외부에서 독립적으로 정의되어 사용되면 **'함수'**라 부르고, 클래스 내부에 종속되어 객체를 통해 호출되는 함수를 **'메소드'**라고 부르는 위치상의 차이만 존재합니다."  

    ___

## 클래스의 선언법.

- 속성값  
속성값이 있을때는 __init__을 필 수로 써야하지만, 속성값이 없을때는 생략가능.
파라미터로 self는 필수
```
class Cal:  
def __init__(self, num1, num2, sign):  
    self.num1 = num1  
    self.num2 = num2  
    self.sign = sign  
```

- 메서드(함수)
작동하는 함수임. 객체에 연동 되어있기에 호출해서 사용할 수 있음.
```
    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")

    def sub(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")

    def multi(self):
        print(f"{self.num1} * {self.num2} = {self.num1 * self.num2}")

    def div(self):
        print(f"{self.num1} / {self.num2} = {self.num1 / self.num2}")

    def solveProblem(self):
        match self.sign:
            case "+":
                self.add()
            case "-":
                self.sub()
            case "*":
                self.multi()
            case "/":
                self.div()
```

위의 코드를 이용해서 작동하는 코드.  
우선 cal이라는 객체를 생성해서 함수를 호출.
```
questionCal = Cal(3, 1, "+")  
questionCal.solveProblem()
```
