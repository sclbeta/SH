#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2,re
from smtplib import SMTP as smtp
import os

def sendip(oip):    
    try:
        content = urllib2.urlopen("http://ddns.oray.com/checkip").read()
        ip = re.search('\d+\.\d+\.\d+\.\d+',content).group(0)
    except:
        ip = False

    if ip == oip:
        pass
    elif ip:
        oip = ip
        os.system('curl http://username:password@ddns.oray.com/ph/update?hostname=vvaa00.xicp.net&myip=%s' %ip)
        os.system("curl -X POST https://dnsapi.cn/Record.Modify -d 'login_email=****@163.com&login_password=******&format=json&domain_id=16806793&record_id=68470074&sub_domain=www&value=%s&record_type=A&record_line=默认'" %ip)
        orighdrs = ['From:*******@163.com', 'To:******@163.com','Subject:IP' ]
        origbody = [ip]
        origmsg = '\r\n\r\n'.join(['\r\n'.join(orighdrs),'\r\n'.join(origbody)]) 
        try:
            s = smtp('smtp.163.com')
            s.login('***@163.com','******')
            errs = s.sendmail('****@163.com',('****@163.com'),origmsg)
            s.quit()
        except:
            pass
    return ip
