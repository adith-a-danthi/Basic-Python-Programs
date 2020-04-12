fhand = open("input.txt")   # Default mode is read mode
content = fhand.read()      # Reads the entire file
print(content)

fhand = open("input.txt")
count = 0
for line in fhand:          # Iterates as many times as the number of lines
    count += 1
    print(line)
print(count)

# Write python code to print the first 10 characters present in the file
fhand = open("input.txt")
characters = fhand.read()
print("First 10 characters of the file : ", characters[:10])

# Print the contents of the file in reverse order
print("The contents of the file in reverse : ")
print(characters[::-1])

# Print lines in odd position
print("Lines at odd numbers")
fhand = open("input.txt")
count = 1
for line in fhand:
    if count % 2 is 1:
        print(line)
    count += 1
