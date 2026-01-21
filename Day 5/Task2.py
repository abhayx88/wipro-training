# Parent class
class Calculator:
    def calculate(self, a, b):
        return a + b


# Child class demonstrating Method Overriding
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b


# Custom class for Operator Overloading
class Number:
    def __init__(self, value):
        self.value = value

    # Overloading + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


# --------- Demonstration ---------

# Method Overriding (Runtime Polymorphism)
calc = Calculator()
adv_calc = AdvancedCalculator()

print("Calculator Result:", calc.calculate(10, 5))        # Addition
print("AdvancedCalculator Result:", adv_calc.calculate(10, 5))  # Multiplication

# Operator Overloading
n1 = Number(20)
n2 = Number(30)
n3 = n1 + n2

print("Operator Overloading Result:", n3)

# Polymorphism using same method name
for obj in (calc, adv_calc):
    print("Polymorphic Call:", obj.calculate(4, 3))
