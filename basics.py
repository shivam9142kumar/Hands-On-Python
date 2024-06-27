# BASICS

print("Hello World")
print("Shivam")
print("Python")

# VARIABLES

x = 10  
y = 3.14  
name = "Shivam"

# INPUT AND OUTPUT.

your_name = input("Enter your name : ") #Input: "Shivam Kumar" 
your_age = int(input("Enter your age : ")) #Input: "21"

print("Hello, My name is ", +your_name+ " My age is ", +your_age) #Output: "Hello, My name is Shivam Kumar, My age is 21

# DATA TYPES

a = 5
print("Type of a: ", type(a))    # Type of a:  <class 'int'>

b = 5.0
print("\nType of b: ", type(b))  # Type of b:  <class 'float'>

c = 2 + 4j
print("\nType of c: ", type(c))  # Type of c:  <class 'complex'>

# ARITHMATIC OPERATORS

a = 9
b = 4

add = a + b
sub = a - b
mul = a * b
mod = a % b
div = a / b 
p = a ** b

print(add) # 13
print(sub) # 5
print(mul) # 36
print(mod) # 1
print(div) # 2.25
print(p)   # 6561

# COMPARISON OPERATORS

print(a == b) #Output: False
print(a != b) #Output: True
print(a > b) #Ouput: True
print(a < b) #Output: False
print(a >= b) #Output: True
print(a <= b) #Output: False

# LOGICAL OPERATORS
print(a > 5 and b > 5) #Outout: True
print(a > 10 or b > 10) #Output: False
print(not(a > 5 and b > 5)) #Output: False

# LIST 
# Creating a List
List = []                       # output :  Blank List: []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]             # Output : List of numbers: [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Tit", "For", "Tat"] 
print("\nList Items: ")
print(List[0])                 # output : Tit
print(List[2])                 # output : Tat

# TUPLES

# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Give', 'Up')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Good')
print("\nTuple with the use of function: ")
print(Tuple1)

''' 
Initial empty Tuple: 
()

Tuple with the use of String: 
('Geeks', 'For')

Tuple using List: 
(1, 2, 4, 5, 6)

Tuple with the use of function: 
('G', 'e', 'e', 'k', 's') 
'''

# Conditional Statements
age = 10

if age >= 18:
    print("He is Adult")
elif 12 <= age < 18:
    print("He is a Teenager")
else:
    print("He is a kid")

# LOOPING STATEMENTS

# Iterating over a String ( For Loop)
print("String Iteration")

s = "Shivam"
for i in s:
    print(i)

# Loop with range
for i in range(0, 10, 2):
    print(i)

# range()
for i in range(5):
    print(i)       # Output: 0 1 2 3 4


# Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# While Loop

count = 0
while count < 5:
    print(count)
    count += 1

# Special Functions

cars = ["Mercedes", "BMW", "Audi"]

# len()
print(len(cars))  # Output: 3

# id()
print(id(cars))  # Output: Unique ID of the list object

