"""
Conditional Statements
"""

print("Enter 3 integers : ")
'''
a = int(input())
b = int(input())
c = int(input())
'''
# Strings can also be compared. ASCII value is considered
a = input()
b = input()
c = input()
# for comparison && is same as and; || same as or
if (a > b) and (a > c):
    print("a is the greatest")
elif b > c:
    print("b is greatest")
else:
    print("c is greatest")


if 0:                   # 0 considered as false
    print("Hello 0")
if 1:                   # positive numbers considered as true
    print("Hello 1")
if -10:                 # negative numbers treated as true
    print("Hello -10")
