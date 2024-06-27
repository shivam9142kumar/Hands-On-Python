 # LISTS

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # allows duplicates

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #list length

# list data types.
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# list Methods
# append - to add an element
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# Clear - to remove all the elements
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# copy - returns the copy
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

# count- no. of items in the list
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# extend - adding the elements of the different lists
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# index - returns the position
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# insert - add an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# pop - removes element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# remove - method removes the first occurrence of the element with the specified value.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# reverse - reverse the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# sort - sort the list in ascending by defalut
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# reverse=true - sort in descending order
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

# sort a/c to length of element
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

