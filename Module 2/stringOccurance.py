# Program to count the occurrence of 'a'  in a string
count = 0
s = input("Print a string : ")
for j in range(len(s)):
    if 'a' is s[j]:
        count += 1
print('Number of occurrence of \'a\' in string is :', count)

'''
to run for loop in reverse

for i in range(12,1,-1):


for char in "Hello":
    print("Hi",char)
'''

# Simpler method
'''
for ch in s:
    if 'a' is s[j]:
        count += 1
'''