def addition(a, b):
    return a + b

def subtraction(a, b):
    return int(a) - int(b)

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def squaring(a):
    return a**2

def squarerooting(a):
    return a**.5

def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def squareroot(self, a):
        self.result = squarerooting(a)
        return self.result

class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass