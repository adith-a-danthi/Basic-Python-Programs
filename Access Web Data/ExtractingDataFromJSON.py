"""
Write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a 
URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
compute the sum of the numbers in the file and enter the sum below: We provide two files for this assignment.
Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_353540.json (Sum ends with 71)

Data Format:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

Sample Execution:

Enter location: http://python-data.dr-chuck.net/comments_42.json
Retrieving http://python-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2482
"""

import urllib.request as ur
import json

json_url = input("Enter Location: ")
print("Retrieving", json_url)

data = ur.urlopen(json_url).read()
print("Retrieved", len(data), "characters")

json_obj = json.loads(data)

total = 0
count = 0

for comment in json_obj["comments"]:
    total += int(comment["count"])
    count += 1

print("Count:", count)
print("Sum:", total)
