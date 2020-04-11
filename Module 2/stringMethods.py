s = "hEllo"
print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.count('l'))
print(s.title())

s = "Hello Fellow"
index = s.find('l')
print(index)
print(s.find('lo'))  # prints only the first occurrence of the pattern
print(s.find('lo', 4))  # same as above; 4 mentions the starting index for search

s1 = "  Good  morning  "
print(s1.strip())   # Removes only leading & trailing whitespaces but not in middle i.e., prints "Good  morning"
print(s1)   # Original string doesn't change

s2 = "Good morning"
if s2.startswith("Good"):   # Case sensitive
    print("match found")
else:
    print("match not found")

print(s2.startswith("Good"))    # startswith method returns a boolean value

s3 = "  Good morning  "
s4 = "how are you"
s5 = s1 + s3
print(s5)
s6 = s1.strip() + s4    # removes leading and trailing whitespaces of s1 and then concatenates the strings
print(s6)

st = "--Hi-how--are-you?-- "
print(st.strip('-'))    # Removes mentioned delimiter in the leading and trailing; default is ' '
