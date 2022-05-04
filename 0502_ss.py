from urllib.request import urlopen
from bs4 import BeautifulSoup

f=open('4c.txt',"w+")
url="https://www.hansung.ac.kr/hansung/8385/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaGFuc3VuZyUyRjE0MyUyRmFydGNsTGlzdC5kbyUzRmJic0NsU2VxJTNEMTY2JTI2YmJzT3BlbldyZFNlcSUzRCUyNmlzVmlld01pbmUlM0RmYWxzZSUyNnNyY2hDb2x1bW4lM0RzaiUyNnNyY2hXcmQlM0QlMjY%3D"

html=urlopen(url).read()


soup=BeautifulSoup(html,'html.parser')


html_class=soup.find_all(class_='td-subject')
#print(html_class)




print('------------')
'''
element_t = str(html_class[3].find("strong"))
indexe=element_t.index('/')
print(indexe)
ni=indexe-39
element_t = element_t[22:ni]
print(element_t)
'''
for tit in html_class:
    '''
    tit==html_class[0]
    tit==html_class[1]
    tit==html_class[2]
    '''
    element_t = str(tit.find("strong"))
    indexe=element_t.index('/')
    print(indexe)
    ni=indexe-39
    
    element_t = element_t[22:ni]
    print(element_t)

    '''title=tit.text.strip()
    #print(tit)
    #print(title)
    str_tit = str(tit)
    #print(str_tit)
    index = len(str_tit)
    
    for i in range(index):
        #print(str_tit[i])
        print(html_class[i].find("strong"))
        
  
    data=f.readlines()
    #print(data)
    #repr(title)
    f.write(str(data))
    #data=f.read()
    #print(data)
'''
print('------------')

#first_found=soup.find(class_='td-subject')
#print(first_found.text)
#print("a")
f.close()

