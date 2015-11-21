# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_200933.html').read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('td')

total = 0
for tag in tags:
    # Look at the parts of a tag
    line = str(tag)
    x = re.findall('[0-9]+',line)
    if len(x) > 0:
        for item in x:
            total += int(item)

print(total)