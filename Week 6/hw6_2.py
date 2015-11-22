import urllib
import json
import ssl

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?'

address = raw_input('Enter location: ')
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data

# Pretty print the JSON
# print json.dumps(js, indent=4)

# Retrieve and print the Place ID
placeID = js['results'][0]['place_id']
print 'Place id: ', placeID