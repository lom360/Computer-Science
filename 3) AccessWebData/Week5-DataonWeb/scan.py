import urllib.request
import urllib.parse
import urllib.error
from xml.etree import ElementTree as ET
import ssl

def parse_website(new_url):
    print('Retrieving url', new_url)
    uh = urllib.request.urlopen(new_url, context=ctx)
    return uh.read()

def create_tree(new_data) :
    print('Retrieved', len(new_data), 'characters')
    print(new_data.decode())
    return ET.fromstring(new_data)

def find_total(tmp_tree) :
    count = 0
    new_sum = 0
    results = tmp_tree.findall('.//count')
    for result in results :
        new_sum = new_sum + int(result.text)
        count += 1
    print("Count:", count)
    return new_sum

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

while True:
    url = input('Enter url: ')
    if len(url) < 1:
        break
    data = parse_website(url)
    tree = create_tree(data)
    total = find_total(tree)
    print("Sum", total)