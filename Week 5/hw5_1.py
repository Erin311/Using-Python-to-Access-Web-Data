import urllib
import xml.etree.ElementTree as ET

# Read in XML from the URL
url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()

# Convert the XML to a tree
tree = ET.fromstring(data)

# Priunt how many characters in the XML
print 'Retrieved',len(data),'characters'

# Get all of the count values
counts = tree.findall('.//count')

# Total all of the counts
total = 0
for item in counts:
    total += int(item.text)

print total