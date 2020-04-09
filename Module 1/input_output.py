print("Welcome")
print('Hello Python')
s = str(input("Enter your name : "))

print("Welcome", s)
# + operator is used to append
print("Welcome" + s)

print("Enter two integers")
a = int(input())
b = int(input())
print("Sum = ", a + b)

# while using + only strings can be appended
# print("Sum = " + (a+b))  error
print("Sum = " + str(a + b))

c = str(input("Enter your name"))
print(c)
