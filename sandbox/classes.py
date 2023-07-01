class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase


user = Person(25, 80, 177, "Jon", "Snow", "You know nothing, Jon Snow")

# print(user.catch_phrase)


class Employee:
    # class variable, something you would want applied to all employees
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        # Each time you instatiate a new employee, the number will increment. 
        Employee.num_of_emps += 1

    # need to pass an instance, self, otherwise the methods will not work
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amount)

    # This method will take the class as an instace. 
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # You can use class methods as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # Static methods do not even pass in self. They are like functions.

    @staticmethod
    def is_workday(day):
        # weekday is a method that prints 0-4 for mon-fri and 5 & 6 for sat & sun
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    pass

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1.fullname())
# can alternatively do this with the class itself. pass in the emp_1 as the instance that gets passed into the method
# print(Employee.fullname(emp_2))

# Below, all three will yield the same number. You can get it from the class itself, or from the instance of the class.

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Now, notice what happens when you change the raise amount for just one employee.

# emp_1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Now, you can set the raise amount for all. 

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)

import datetime
my_date = datetime.date(2016, 7, 10) # This is a sunday, so false. 

print(Employee.is_workday(my_date))