# creating sets:
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # Duplicates not allowed

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #True and 1 is considered the same value

thisset = {"apple", "banana", "cherry",
 False, True, 0}
print(thisset) #False and 0 is considered the same value

# Access items:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
print("banana" in thisset) # Check if "banana" is present in the set
print("banana" not in thisset) # Check if "banana" is NOT present in the set

# add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add elements from tropical into thisset, use the update() method:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# by using discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear() # clear empties the set
print(thisset)

# pop()
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)

# remove()
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #Return a set that contains the items that only exist in set x, and not in set y
print(z)

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
myset = a - b
print(myset)

# union
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) #Remove the items that is not present in both x and y
print(x)

# isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) # Return True if no items in set x is present in set y
print(z)

# issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) # Return True if all items in set x are present in set y
print(z)

# issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) #Return True if all items set y are present in set 
print(z)

