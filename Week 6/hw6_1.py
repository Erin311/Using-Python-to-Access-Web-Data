import urllib
import json

# Read in JSON from the URL
url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()

# Print how many characters in the JSON
print 'Retrieved',len(data),'characters'

# load the JSON into a dictionary
js = json.loads(str(data))
#print json.dumps(js, indent=4)
print 'Count :', len(js["comments"])


# Total all of the counts
total = 0
for item in js["comments"]:
    #print item["count"]
    total += item["count"]

print 'Sum: ', total