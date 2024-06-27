# Python Inheritance

# Creating a parent class
class ParentClass:
    #parent class methods and attributes
    def prent_nethod(self):
        print("This parent method")

# Creating a child class
class ChildClass(ParentClass):
    #child class attributes and methods and parent class attributes and functions
    def child_method(self):
        print("This is child method")

# Inheritance Example
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Creating instances
generic_animal = Animal("Generic Animal")
dog = Dog("Buddy")

# MRO(Method Resolution Order)
# Calling methods
generic_animal.speak()  # Output: Generic Animal makes a sound
dog.speak()             # Output: Buddy barks

class Animal:
    pass

class Canine:
    pass

class Dog(Animal, Canine):
    pass

# Print the MRO of class Dog
print(Dog.__mro__)  # Output: (<class '__main__.Dog'>, <class '__main__.Animal'>, <class '__main__.Canine'>, <class 'object'>)
print(Dog.mro())    # Output: [<class '__main__.Dog'>, <class '__main__.Animal'>, <class '__main__.Canine'>, <class 'object'>]

# Types of Inheritance

# Single Inheritance 
# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

# Child class
class Student(Person):
    def introduce(self):
        print(f"Hello, I am {self.name} and I am a student")

# Creating an instance of Student
student = Student("Shivam")
student.introduce()  # Output: Hello, I am Shivam and I am a student

# Multiple Inheritance
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.method_a()  # Output: Method A
c.method_b()  # Output: Method B

# Multilevel Inheritance

# Parent class A
class A:
    def method_A(self):
        print("Method A from class A")

# Child class B, inherits from A
class B(A):
    def method_B(self):
        print("Method B from class B")

# Grandchild class C, inherits from B
class C(B):
    def method_C(self):
        print("Method C from class C")

# Creating instances of each class
obj_A = A()
obj_B = B()
obj_C = C()

# Calling methods from each instance
obj_A.method_A()  # Output: Method A from class A
obj_B.method_A()  # Output: Method A from class A (inherited from A)
obj_B.method_B()  # Output: Method B from class B
obj_C.method_A()  # Output: Method A from class A (inherited from B)
obj_C.method_B()  # Output: Method B from class B (inherited from B)
obj_C.method_C()  # Output: Method C from class C

# Hierarchical Innheritance 

# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class 1
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Creating instances of each child class
dog = Dog()
cat = Cat()

# Calling methods from each instance
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks
cat.speak()  # Output: Animal speaks
cat.meow()   # Output: Cat meows

# Hybrid Inheritance

# Parent class A
class A:
    def method_A(self):
        print("Method A from class A")

# Child class B, inherits from A
class B(A):
    def method_B(self):
        print("Method B from class B")

# Child class C, inherits from A
class C(A):
    def method_C(self):
        print("Method C from class C")

# Grandchild class D, inherits from both B and C
class D(B, C):
    def method_D(self):
        print("Method D from class D")

# Creating an instance of class D
obj_D = D()

# Calling methods from the instance
obj_D.method_A()  # Output: Method A from class A (inherited from A)
obj_D.method_B()  # Output: Method B from class B
obj_D.method_C()  # Output: Method C from class C
obj_D.method_D()  # Output: Method D from class D

# Exception Handling

'''When an error occurs, or exception as we call it, 
Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:'''

# Try
try:
  print(x)         # In vscode it's shows an error of "X" is not defined. so we can try on another platform like Juypter for proper output.
except:
  print("An exception occurred")  # output : An exception occured
 
# Many Exceptions 
try:
  print(x)       
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")  # output : Variable X is not defined

# ELse
try:
  print("Hello")
except:
  print("Something went wrong") 
else:                               # output : Hello
  print("Nothing went wrong")       #          Nothing went wrong

# Finally 
try:
  print(x)
except:
  print("Something went wrong")
finally:                                   # output : Something went wrong
  print("The 'try except' is finished")    #          The 'try except' is finished

try:
  f = open("demofile.txt")
  try:
    f.write("Shivam")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  # output : Something went wrong when opening the file

# Raise an Exception

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")    # output -- Exceotion : Sorry, no numbers below zero

# Raise a TypeError
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")     # output -- TypeError: Only integers are allowed

# Indentation Error
try:
    # Code with incorrect indentation
    def my_function():
        print("Inside function")
         print("This line is incorrectly indented")  # Extra space
except IndentationError:
    print("IndentationError occurred")  # Output :  IndentationError

 # Value Error
 try:
    # Code that passes an invalid value to a function
    int("hello")  # The string "hello" cannot be converted to an integer
except ValueError:
    print("ValueError occurred")  # output : ValueError occured
     
