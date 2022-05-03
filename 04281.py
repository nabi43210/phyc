from urllib.request import urlopen
from bs4 import BeautifulSoup

f=open('4c.txt',"w+")

'''
#실제 사용시
newfile=input("새 텍스트파일: ")+".txt"
f3=open(newfile,"w+")
'''

url="https://www.hansung.ac.kr/hansung/8385/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaGFuc3VuZyUyRjE0MyUyRmFydGNsTGlzdC5kbyUzRmJic0NsU2VxJTNEMjg2JTI2YmJzT3BlbldyZFNlcSUzRCUyNmlzVmlld01pbmUlM0RmYWxzZSUyNnNyY2hDb2x1bW4lM0RzaiUyNnNyY2hXcmQlM0QlMjY%3D"

html=urlopen(url).read()


soup=BeautifulSoup(html,'html.parser')
html_class=soup.find_all(class_='td-subject')
htmls=soup.find_all('tr',{'class':'notice'})
aa=len(htmls)
print(aa)
print(htmls[1])






print('---*--*--*--*--*-')

print("html_class num: ",len(html_class))

del html_class[0:aa]
elelist=[]
cnt=0
for tit in html_class:
    
    #tit==html_class[0]
    #tit==html_class[1]
    #tit==html_class[2]
    
    element_t = str(tit.find("strong"))
    indexe=element_t.index('/')
    ni=indexe-39
    #element_t는 공지문자!
    
    element_t = element_t[22:ni]+"\n"


    elelist.append(element_t)    
    f.write(str(element_t))
    cnt=cnt+1
print('------------')


#비교시작

f2=open('5c.txt',"r", encoding='UTF-8')
firsts=f2.readline()
print(firsts)

print(elelist[0])

if(firsts!=elelist[0]):
    print("공지 업데이트됨")
else:
    print("업데이트되지 않음")

f.close
f2.close
