from signal import signal
from urllib.request import urlopen
from bs4 import BeautifulSoup
from infi.systray import SysTrayIcon
from plyer import notification
import plyer.platforms.win.notification
import os.path
import schedule
import time
import sys
import pkg_resources
import signal

def exit_program(systray):
    os.kill(os.getpid(), signal.SIGTERM)

def update():
    f=open('4c.txt',"w+",encoding='UTF-8')
    html=urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    html_class=soup.find_all(class_='td-subject')
    htmls=soup.find_all('tr',{'class':'notice'})
    aa=len(htmls)
    del html_class[0:aa]
    elelist=[]
    cnt=0
    for tit in html_class:
        element_t = str(tit.find("strong"))
        indexe=element_t.index('/')
        ni=indexe-39    
        element_t = element_t[22:ni]+"\n"
        elelist.append(element_t)
        f.write(str(element_t))
        cnt=cnt+1
        ele=elelist[0].strip("\n"".")

    if (not os.path.isfile('5c.txt')):
        print("no file")
        f2 = open('5c.txt', 'w+', encoding="UTF-8")
        f2.close()
    f2=open('5c.txt',"r", encoding='UTF-8')
    firsts=f2.readline()

    print("5c.txt head:", firsts)
    print("examin:", str(ele))

    if(firsts!=ele):
        f2=open('5c.txt','w',encoding='UTF-8')
        print("공지 업데이트됨: ")
        f2.write(str(ele))
        notification.notify("Hansung Notice",str(ele))
        f2.close()
    else:
        print("업데이트되지 않음")
    f.close()
    
job = schedule.every(5).minutes.do(update)
systray = SysTrayIcon('', "Hansung Notice", on_quit=exit_program)
systray.start()
url="https://www.hansung.ac.kr/hansung/8385/subview.do?"
update()
while True:
    schedule.run_pending()
    time.sleep(1)

f.close()
f2.close()
