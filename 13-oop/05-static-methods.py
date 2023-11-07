class Calculator:
    def sum(self, a=0, b=0):
        return a + b


calculator = Calculator()
calculator.sum(2, 3)  # ?

Calculator.sum(None, 2, 3)  # ?


class Calculator:
    @staticmethod
    def sum(a=0, b=0):
        return a + b


# Calculator.sum = staticmethod(Calculator.sum)

Calculator.sum(2, 3)  # ?

calculator = Calculator()
# calculator.sum(2, 3)  # ?


class Calculator:
    instance = None

    @staticmethod
    def get_instance():
        if Calculator.instance is None:
            Calculator.instance = Calculator()
        return Calculator.instance

    def sum(self, a=0, b=0):
        return a + b


calculator1 = Calculator.get_instance()  # ?
calculator2 = Calculator.get_instance()  # ?
print(calculator1 is calculator2)


class Math:
    def __init__(self, computer):
        self.computer = computer

    def sum(self, a, b):
        return self.computer.sum(a, b)


class Noop:
    def sum(self, a, b):
        pass

# Dependency Injection


calculator = Calculator()
noop = Noop()
math = Math(noop)
math.sum(2, 3)  # ?
