# -*- coding: utf-8 -*-

from time import ctime,sleep
import threading

title = None
link = None

def video():
    from video import yayaxz,sohu
    things = {'yayaxz':yayaxz,'sohu':sohu}
    while True:
        f = file('tvs.txt','r')
        alllines = f.readlines()
        f.close
        for eachline in alllines:
            tag,title,link = eachline.split('|')
            tag = tag[-6:]
            #print tag
            #print things[tag]
            things[tag].main(title,link)
        print ctime()
        sleep(7200)
        
def faip():
    from extra import faip
    ip = None
    while True:
        ip = faip.sendip(ip)
        sleep(3600)

def timeexe():
    from extra import timeexe
    while True:
        timeexe.jiexi()

def chuankou():
    pass

def main():
    threads = []
    '''
    threadsname = ['faip','video','timeexe','chuankou']
    for temp in threadsname:
    '''
    threads.append(threading.Thread(target = faip,args = ''))
    threads.append(threading.Thread(target = video,args = ''))
    threads.append(threading.Thread(target = timeexe,args = ''))
    threads.append(threading.Thread(target = chuankou,args = ''))
        
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()

    for thread in threads:
        if not thread.isAlive():
            thread.start()
        
if __name__ == '__main__':
    #print 'os'
    main()
