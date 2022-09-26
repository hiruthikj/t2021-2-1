class Calculator:
    def __init__(self, num1:int, num2:int, op:str) -> None:
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def compute(self):
        if self.op == "+":
            return self.num1 + self.num2
        elif self.op == "-":
            return self.num1 - self.num2
        elif self.op == "*":
            return self.num1 * self.num2
        elif self.op == "/":
            return self.num1 / self.num2


def main():
    a, b = map(int, input("Enter numbers: ").split())
    op = input("Enter operation: ")

    calc = Calculator(a,b,op)
    result = calc.compute()
    print(result)

main()