import time
import urllib2

weeks={'Mon':'week1',
       'Tue':'week2',
       'Wed':'week3',
       'Thu':'week4',
       'Fri':'week5',
       'Sat':'week6',
       'Sun':'week7',
    }

def jiexi():
    tod = time.ctime()[:3]
    f = file('~/pi/sh/mysite/%s' %weeks[tod],'r')
    alllines = f.readlines()
    f.close()
    for i in range[1440]:
        for eachline in alllines:
            starttime,endtime,command1,command2 = eachline.split('|')[1::2]
            #print starttime,endtime,command1,command2
            if time.ctime()[11:16] in starttime:
                #print 'kaishishijian'
                urllib2.urlopen('http://127.0.0.1:8185/light/2')
            elif time.ctime()[11:16] in endtime:
                #print 'jieshushijian'
                urllib2.urlopen('http://127.0.0.1:8185/light/2')
        time.sleep(60)
