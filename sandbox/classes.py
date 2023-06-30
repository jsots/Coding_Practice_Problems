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
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    # need to pass an instance, self, otherwise the methods will not work
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)


print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

# can alternatively do this with the class itself. pass in the emp_1 as the instance that gets passed into the method
print(Employee.fullname(emp_2))