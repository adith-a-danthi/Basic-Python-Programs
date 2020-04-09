s = "Welcome"

print(s)
print(s[0])

ch = s[1]
print(ch)

# error - Strings are immutable (characters in a string cannot be changed)
# s[0] = 'J'

# Slicing - prints part of the string
print(s[1:4])  # prints characters from 1 to 4th index of the string (includes 1 but not 5)

st = "good morning"
print(st[1:5])  # includes 1 but not 5
print(st[1:])  # from 1 to end of string
print(st[:8])  # prints from start of string upto 8th index
print(st[0:8])  # same as above
print(st[0:8:1])  # same as above
print(st[0:8:2])  # prints every 2nd character from 0 upto 8th character
print(st[9:1])  # error
print(st[9:1:-1])  # prints in reverse order from 9th character to 2nd (including 9 and excluding 1)
print(st[9:1:-3])  # prints every 3rd character in reverse from 9th to 2nd character of the string
print(st[9::-3])  # prints every 3rd character in reverse order from 9th character to start of string

s1 = "Hello"
s2 = s1[1:4]
print(s1)
print(s2)

s = "Good morning"
print(s[-7:-2])  # prints the 7th character from the end until the 2nd character from the end
# 'g' 'o' 'o' 'd' ' ' 'm' 'o' 'r' 'n' 'i' 'n' 'g'
# -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

#  Write a code to reverse string
s1 = input("Enter a string : ")
print("The reverse string is :", s1[::-1])  # Prints reverse of string

# --------------------------------

s1 = "Welcome"
print(s1, id(s1))
s1 = "Hello"            # a different string is used (the old string is removed/destroyed and a new one is created)
print(s1, id(s1))
