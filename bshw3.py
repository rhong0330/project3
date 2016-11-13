import operator
import requests

import re
import os.path

from bs4 import BeautifulSoup
from os.path import basename, splitext

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
#
# findtoure = soup.find_all(text = re.compile('Gnegneri Toure Yaya'))
# for comment in findtoure:
#     fixed_text = unicode(comment).replace('Gnegneri Toure Yaya', 'Yaya Toure')
#     comment.replace_with(fixed_text)

imgs = soup.findAll(name='img')
for img in soup.findAll('img'):
    if "https" in img['src']:
        img['src'] = "https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/14713720_10157528435315532_1991388337609244455_n.jpg?oh=e45337bde4a11ce08fe04ba8d7f011f5&oe=58958B93"
    else:
        img['src'] = "https://github.com/rhong0330/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true"


str_soup = str(soup)
print (str_soup.replace("student", "AMAZING student"))
f = open('bshw3.html','w')
message = str_soup
f.write(message)
f.close()

# i = 0;
# while True:
#     try:
#         print(soup.findAll('student')[i])
#     except:
#         break
#     i += 1
# f = open('helloworld.html','w')
#
# message = """<html>
# <head></head>
# <body><p>Hello World!</p></body>
# </html>"""
#
# f.write(message)
# f.close()