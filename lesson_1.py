import requests
res = resquests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')

#check the return type
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') 
print(type(res))


#check the connect status
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') 
print(res.status_code)

#get the picture
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
pic = res.content
photo = open('ppt.jpg','wb')
photo.write(pic)
photo.close()

#get the novel and save
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
novel= res.text
print(novel[:800])
k = open('novel.txt','a+')
k.write(novel)
k.close()

#encode
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res.encoding='uft-8'
novel= res.text
print(novel[:800])

#exercise1
import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
roborts = res.text
#print(roborts)
b = open('Roborts','a+')
b.write(roborts)
b.close()

