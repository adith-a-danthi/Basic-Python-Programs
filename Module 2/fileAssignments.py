# User enters file name. Read and print the contents of the file
# fileStr = input("Enter file name : ")

# file = open(input("Enter file name : "))    # file = open(fileStr)
# print(file.read())
# file.close()


# Count the total number of character in the file
file = open("input.txt")
print("Number of characters in file :", len(file.read()))

# Combining into single line
print("Number of characters in file :", len(open("input.txt").read()))


'''
file = open("input.txt")
count = 0
for line in file:
    count += len(line)
print("Number of characters in file :", count)
'''

# Copy the contents of one file to another
file1 = open("input.txt")
content = file1.read()
file2 = open("output.txt", 'w')
file2.write(content)

# Compressed above code into single line (Not recommended)
open("output.txt", 'w').write(open("input.txt").read())

# Taking file input from user
try:
    open(input("Enter output file : "), 'w').write(open(input("Enter input file name : ")).read())
except FileNotFoundError:
    print("File not found")

# Print first 'n' lines of the file
n = int(input("Enter the number of lines : "))
file = open("input.txt")
count = 0
for line in file:
    if count < n:
        count += 1
        print(line.rstrip())
    else:
        break
