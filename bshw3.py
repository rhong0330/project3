import requests
from bs4 import BeautifulSoup

#set up soup
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

#find all imgs
imgs = soup.findAll(name='img')
for img in soup.findAll('img'):
    #change mainfile pic
    if "https" in img['src']:
        img['src'] = "https://scontent.fdet1-1.fna.fbcdn.net/t31.0-8/12186612_10156160900535532_9076012322738849483_o.jpg"
    #change logos to given logo
    #used url of the logo instead
    #works the same
    #without the local file
    else:
        img['src'] = "https://github.com/rhong0330/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true"

#replace student to AMAZING student
str_soup = str(soup)
str_soup = str_soup.replace("student", "AMAZING student")

#save to an html file
f = open('bshw3.html','w')
message = str_soup
f.write(message)
f.close()
