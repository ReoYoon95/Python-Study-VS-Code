class Cal:
    def __init__(self, num1, num2, sign):
        self.num1 = num1
        self.num2 = num2
        self.sign = sign

    def add(self, num1, num2):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")

    def sub(self, num1, num2):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")

    def multi(self, num1, num2):
        print(f"{self.num1} * {self.num2} = {self.num1 * self.num2}")

    def div(self, num1, num2):
        print(f"{self.num1} / {self.num2} = {self.num1 / self.num2}")

    def solveProblem(self, num1, num2, sign):
        match sign:
            case "+":
                self.add(num1, num2)
            case "-":
                self.sub(num1, num2)
            case "*":
                self.multi(num1, num2)
            case "/":
                self.div(num1, num2)


questionCal = Cal(3, 1, "+")
questionCal.solveProblem(3, 1, "+")
