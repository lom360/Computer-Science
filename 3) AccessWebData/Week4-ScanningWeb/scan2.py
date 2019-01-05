# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import urllib.request

# This will load url page and store contents within an array.
def Find_Link(new_url) :
    html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    return soup('a')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
# This will be how many times we'll repeat selecting links.
count = int(input("Enter count: "))
# Subtract 1 to account for index starting at 0.
position = int(input("Enter position: ")) - 1

# For the sake of easy testing. If incorrect url was entered. 
# Then correct url will automatically be set by if statement.
if url != "http://py4e-data.dr-chuck.net/known_by_Aleese.html":
    url = "http://py4e-data.dr-chuck.net/known_by_Aleese.html"
print("Retrieving:", url)

tags = Find_Link(url)

while count > 0 :
    print("Retrieving:", tags[position].get('href', None))
    url = tags[position].get('href', None)
    tags = Find_Link(url) # Function call to obtain new link file document.
    count = count - 1

# for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    # print(tag.contents[0])