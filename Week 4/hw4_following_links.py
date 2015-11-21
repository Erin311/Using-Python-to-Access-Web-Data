# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

# Input prompts
url = raw_input('Enter URL: ')
print(url)
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position)

# repeat count number of times
for i in range(0, count+1):

    #read in url and soup it
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    if i < count:
        print "Retrieving: ", url
    else:
        print 'Last Url: ', url
        break

    # Retrieve all of the anchor tags
    tags = soup('a')

    # loop through tags and find the tag at position
    pos = 0
    for tag in tags:
        if pos == position-1:
            url = str(tag.get('href', None))
            break
        pos += 1