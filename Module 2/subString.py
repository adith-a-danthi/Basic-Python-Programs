# program to print the substring between @ & #

s = "Go#od@morning#have a nice day"

start = s.find('@')
end = s.find('#', start)
print(s[start+1:end])

# Assume a list of email ids
s1 = "abc@gmail.com;mail@gmail.com;test@gmail.com"


# Without split function
start = 0
end = s1.find(';')
while end != -1:
    print(s1[start:end])
    start = end + 1
    end = s1.find(';', start)


a = s1.split(';')
for email in a:
    print(email)
