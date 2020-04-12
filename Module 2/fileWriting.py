# Preferably use try except block while handling files to avoid errors when file doesn't exist
try:
    file = open("output.txt", 'w')  # 'w' to writes on file erasing old content
    s = "Welcome to the world of Python\n"
    file.write(s)
    s1 = "This is the second line"
    file.write(s1)
    file.close()
except FileNotFoundError:
    print("File cannot be opened")

# file mode 'a' is used to append the new text onto the file retaining the old content
try:
    file = open("output.txt", 'a')
    s2 = "\nAll we ever hear from you is blah blah blah"
    file.write(s2)
    file.close()
except FileNotFoundError:
    print("File cannot be opened")
