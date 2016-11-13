import requests

from bs4 import BeautifulSoup

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

imgs = soup.findAll(name='img')
for img in soup.findAll('img'):
    if "https" in img['src']:
        img['src'] = "https://scontent.fdet1-1.fna.fbcdn.net/t31.0-8/12186612_10156160900535532_9076012322738849483_o.jpg"
    else:
        img['src'] = "https://github.com/rhong0330/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true"


str_soup = str(soup)
str_soup = str_soup.replace("student", "AMAZING student")
f = open('bshw3.html','w')
message = str_soup
f.write(message)
f.close()
