from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup
'''
while True:
    d=input("대학교 입력: ")
    if d=='0':
        break
    d+="대학교"    
    d=parse.quote(d)

    url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="+d
    html=urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    htmlc=soup.find(class_='area_sub_info')
    htmlc=htmlc.get_text()
    print(htmlc.strip(), '\n')
'''

