class Calculator:
    def __init__(self):
     self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.result /= num

    def clear(self):
        self.result = 0

calc = Calculator()
calc.add(5)
print(calc.result)

calc.subtract(2)
print(calc.result)

calc.multiply(8)
print(calc.result)

calc.divide(6)
print(int(calc.result))