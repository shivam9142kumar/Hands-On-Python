# Creating a class.
'''
class class_name:
    #This is a docstring. I have created a new class
    <statement 1>
    <statement 2>
'''

'''
Create object of a class
<object-name> = <class-name>(<arguments>)
'''

# Create object of a class

class Person:
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)

# create object of a class
a = Person('Shivam', 'Male', 'AI Engineer')

# call methods
a.show()
a.work()

# CLass Attributes
'''Instance Variables'''
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
s1 = Student("Shivam", 20)

# access instance variable

print('Name:', s1.name)
print('Age:', s1.age)

'''CLass Variables'''

class Student:
    # Class variable
    school_name = 'ABC School '
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create object
s1 = Student('Raj', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

'''Static Method'''
class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employee('Rahul', 12000, 'ABC Project')
emp.work()

class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()

# Encapsulation in Python

class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project
    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Rahul', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()

# Polymorphism in Python 
'''Polymorphism in Built-in function len()'''
students = ['Rahul', 'Raj', 'Kamal']
school = 'ABC School'
# calculate count
print(len(students))
print(len(school))

'''With Shapes'''
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# List of different shapes
shapes = [Rectangle(2, 3), Circle(5), Triangle(4, 6)]

# Calculating areas using polymorphism
for shape in shapes:
    print(f"The area of the shape is: {shape.area()}")

# Outputs:
# The area of the shape is: 6
# The area of the shape is: 78.5
# The area of the shape is: 12.0
