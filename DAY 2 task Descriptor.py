# Descriptor for name
class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        instance._name = value


# Descriptor for salary
class SalaryDescriptor:
    def __get__(self, instance, owner):
        return instance._salary

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be positive")
        instance._salary = value


# Employee class using descriptors
class Employee:
    name = NameDescriptor()
    salary = SalaryDescriptor()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Testing
emp = Employee("Abhay", 50000)
print(emp.name)
print(emp.salary)

