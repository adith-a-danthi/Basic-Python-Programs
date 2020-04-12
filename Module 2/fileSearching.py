file = open("input.txt")
s = input("Enter the starting word : ")
print("Lines starting with", s, ": ")
for line in file:
    if line.startswith(s):
        print(line)                     # print(line.rstrip()) - removes additional new line character
# leaves a line gap between the output lines as it prints the '\n' at the end of the line in the file
# followed by another line by print
# to remove the new line character use rstrip() function


file = open("input.txt")
key = input("Enter the search string : ")
print("Lines containing", key)
for line in file:
    if key in line:             # if line.find(key) != -1:
        print(line)

file = open("input.txt")
key = input("Enter the search string : ")
print("Lines not containing", key)
for line in file:
    if key not in line:
        print(line)
