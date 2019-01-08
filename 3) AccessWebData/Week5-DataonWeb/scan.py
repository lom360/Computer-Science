import urllib.request
import urllib.parse
import urllib.error
from xml.etree import ElementTree as ET
import ssl

def parse_website(new_url) :
    print('Retrieving url', new_url)
    uh = urllib.request.urlopen(new_url, context=ctx)
    return uh.read()

def create_tree(new_data) :
    print('Retrieved', len(new_data), 'characters')
    print(new_data.decode())
    return ET.fromstring(new_data)

def find_total(comments) :
    results = comments.findall('comments')
    print(results[0].text)
    return 1

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
    print(total)
    


# while True:
#     address = input('Enter location: ')
#     if len(address) < 1:
#         break

#     parms = dict()
#     parms['address'] = address
#     if api_key is not False:
#         parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)

#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print('lat', lat, 'lng', lng)
#     print(location)
