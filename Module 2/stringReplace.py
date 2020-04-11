s = "apple"
print(s[0])
print(s)

# s[0] = 'b     # error
print(s, id(s))
s = "bpple"   # allowed but a new string is created
print(s, id(s))

s = 'happy'
s.replace('p', 'z')     # Doesn't give an error, no changes saved
s2 = s.replace('p', 'z')
print(s.replace('p', 'z'))  # string isn't altered
print(s, id(s))
print(s2, id(s2))

