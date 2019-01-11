import urllib.request, urllib.parse, urllib.error
import json

def char_count(file) :
    temp = json.dumps(file)
    print("Retrieved", len(temp), " characters")

# read() turns file into a string.
# decode() wile turn the file into an object

url = input("Enter location: ")
json_url = urllib.request.urlopen(url)

# Storing the object gained from the url and store in data as a dictionary.
print("Retrieving", url)
data = json.loads(json_url.read().decode())
comments = data["comments"]

# Counts number of characters in file.
char_count(data)

total = 0
count = 0
for comment in comments :
    total = total + comment['count']
    count += 1

print("Count:", count)
print("Sum:", total)