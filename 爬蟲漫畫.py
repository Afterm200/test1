

import requests

from bs4 import BeautifulSoup

#board_find = main.find_all('url', class_="comic-contain")

#target_url = "https://www.webmota.com/comic/chapter/woduzishengji-duburedicestudio_ar/0_12.html"
#r = requests.get(url=target_url)
#bs = BeautifulSoup(r.text, 'lxml')
#list_con_li = bs.find('src', class_="comic-contain")
#print(list_con_li)


hotpage = requests.get("https://www.webmota.com/comic/chapter/woduzishengji-duburedicestudio_ar/0_12.html")
main = BeautifulSoup(hotpage.text, 'html.parser')
print(main.text) #這裡可以print看看已抓取到除標籤外的文字
type(main.text)


T=list(main.text.split(" "))



l=[]

for i in T:
    if ".jpg" in i:
        print(i)
        l.append(i)

characters = "\" }"
    
l2=[]

for i in range(len(l)):
    h=l[i]
    for x in range(len(characters)):
        h = h.replace(characters[x],"")
    l2.append(h)

l2[0]

for i in range(len(l2)):
    res = requests.get(l2[i])
    with open('test'+str(i)+'.jpg', 'wb') as f:
        f.write(res.content)
    
    
    
    

#res = requests.get(l2[0])
#with open('test.jpg', 'wb') as f:
#    f.write(res.content)
    
    
    
    
    
    
    
    
    
    

