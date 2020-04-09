var1 = 10
var2 = "Hello"

# Everything in python is an object including variables, functions, list, etc
print(type(var1))
print(type(var2))
print()

# dir gives the available functions for the object (variables are also objects in python)
# example var2.count()
print(dir(var1))
print(dir(var2))
print()

# IDs are same as they point to different objects
print(id(var1))
print(id(var2))
print()

# if the value is the same it links to the same object hence the IDs of the variables are the same
a = 30
b = 30
print(id(a))
print(id(b))
print()

b = 40
print(id(a))
print(id(b))
print()

# c stores a decimal value
a = 10
b = 3
c = a / b
print(c)

# truncate division
c = a // b
print(c)

# c = 1.5
c = 3.0 / 2
print(c)

# c = 1.0
c = 3.0 // 2
print(c)

# exponent
f = 2 ** 3
print(f)

# remainder | Modulus is used only on integers
r = 11 % 9
print(r)

r = 11.5 % 9
print(r)

# Modulus number is added to numerator until it becomes positive
c = -11 % 9
print(c)

# 
c = (200 - 70) * 10 / 5
print(c)

c = 5 * 1 ** 2
print(c)

# boolean : True False
c = True
d = not False
print(c, d)
print(not c, not d)

p = "True"
print(p)
q = "true"
print(q)

# "True" is considered to be some value hence there is a value, the not of it will be false. i.e, it does.t have a value
r = not "True"
print(r)

# False - Boolean  value false ; "False" - string False
s = "False"
print(s, not s)
t = not "False"
print(t)
# Any string is taken as true. Hence not of any string is false
u = not "hello"
print(u)

# Brackets, Exponential, Division, Multiplication, Addition, Subtraction
a = 1 / 2 + 3 // 3 + 4 ** 2
print(a)

x = 2 / 4
y = 4 / x
print(y, x)
