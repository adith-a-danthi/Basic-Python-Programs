
l1 = [10, 20, 30, 40]
print(l1)               # Prints the entire list with braces
print(l1[2])            # Prints the list element at index 2

# Lists are mutable
l1[2] = 60
print(l1[2])

# Lists can contain elements of multiple data types as python treats all as an object
l2 = [10, "Hello", 23.3, '!']
print(l2)

print(l2[2])
l2[2] = "World"
print(l2[2])

# There can be lists inside a list
l3 = [10, 20, ["Hello", "World"], [5.8, 6.5]]
print(l3)