import requests
from bs4 import BeautifulSoup

response=requests.get('http://google.com/')

soup=BeautifulSoup(response.text,'lxml')
#soup=str(soup)

# with open('textFile.html','w') as f:
#     f.write(soup)


buttons=soup.findAll('input')
#print(buttons)

for button in buttons :
    print(button)
