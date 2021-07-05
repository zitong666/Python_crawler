import requests
from bs4 import BeautifulSoup

#analysis data
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
print(type(soup))
print(soup)

#pickup data
url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
item = soup.find('div')
itemAll = soup.find_all('div')
print(type(item))
print(type(itemAll))
print(item)
print(itemAll)

#exercise_1
url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
items = soup.find_all(class_='books')
for item in items:
    kind = item.find('h2')
    title = item.find(class_='title')
    brief = item.find(class_='info')
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text,'\n')
    print(type(kind),type(title),type(brief))
#print(type(items))
#print(items)

