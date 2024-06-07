# Creating a function
def my_function():
  print("Hello Shivam")

my_function()

# Arguments
def my_function(fname):
  print(fname + " Kumar ")
my_function("Shivam")
my_function("Rahul")
my_function("Raj")

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Shivam", "Kumar")

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Raj", "Ram", "Rahul")

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Shivam", lname = "Kumar")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Sam", child2 = "Mohan", child3 = "Jay")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a list
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Positional-Only-Arguments
def my_function(x, /):
  print(x)
my_function(3)

def my_function(x):
  print(x)
my_function(x = 3)

# Keyboard-Only-Arguments
def my_function(*, x):
  print(x)
my_function(x = 4)

def my_function(x):
  print(x)
my_function(4)

# Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

#  LAMBDA FUNCTION

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n 
mydoubler = myfunc(2)   # doubles every number
print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)  # triples every number
print(mytripler(11))

# both the function in one program
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

