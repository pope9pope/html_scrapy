import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.autohome.com.cn/news/')
response.encoding = 'gbk'
soup = BeautifulSoup(response.text,"html.parser")
div =soup.find(name='div',id='auto-channel-lazyload-article')
li_list = div.find_all(name='li')
for li in li_list:
    h3 = li.find(name='h3')
    a = li.find(name='a')
    p =li.find(name='p')
                    
    if not h3:
        continue
    print(h3.text)
    print(a.attrs['href'])
    print(p.text)
    print('======================')
        
        
