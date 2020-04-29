"""

Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop
to find the most prolific committer.

"""

name = input("Enter file:")
handle = open(name)

counts = dict()  # creating a dictionary
for name in handle:
    name = name.rstrip()
    if name.startswith('From '):
        splitIt = name.split()
        counts[splitIt[1]] = counts.get(splitIt[1], 0) + 1

maxCount = None
maxWord = None
for word, count in counts.items():
    if maxCount is None or count > maxCount:
        maxWord = word
        maxCount = count
print(maxWord, maxCount)