from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://www.hansung.ac.kr/hansung/8385/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaGFuc3VuZyUyRjE0MyUyRmFydGNsTGlzdC5kbyUzRmJic0NsU2VxJTNEMjg2JTI2YmJzT3BlbldyZFNlcSUzRCUyNmlzVmlld01pbmUlM0RmYWxzZSUyNnNyY2hDb2x1bW4lM0RzaiUyNnNyY2hXcmQlM0QlMjY%3D"

html=urlopen(url).read()


soup=BeautifulSoup(html,'html.parser')


html_class=soup.find_all(class_='td-subject')

for tit in html_class:
    title=tit.text.strip()
    print(title)
print('------------')
first_found=soup.find(class_='td-subject')
print(first_found.text)
print("a")