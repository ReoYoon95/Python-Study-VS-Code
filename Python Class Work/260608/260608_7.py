class Cal:
    def __init__(self, num1, num2, sign):
        self.num1 = num1
        self.num2 = num2
        self.sign = sign

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


questionCal = Cal(3, 1, "+")
questionCal.solveProblem()
