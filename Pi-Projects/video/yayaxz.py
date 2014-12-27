# -*- coding: utf-8 -*-

import urllib2
import re
import sqlite3 as lite
from time import sleep

rulen = 'ed2k.+'

def main(title,link):
    if re.search('\r|\n',link):
        link = link[:-1]
    try:
        content = urllib2.urlopen(link,timeout=60).read()
    except:
        print 'Get content error'
        return None
    sleep(0.1)
    rulename = '%s.S\d\dE\d\d' %title
    name=re.findall(rulename,content)
    title = max(name)

    if not _check(title):
        rulelink = 'thunderhref=.+%s.+\d\d\d\dX\d\d\d.+mkv.+\|/' %title
        tbbt = re.findall(rulelink,content)
        if tbbt:
            tbbtlink = re.findall(rulen,tbbt[0])[0]
            print tbbtlink
            _add(title,tbbtlink)

def _check(title):
    print title
    con = lite.connect('0.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Things(Name TEXT, Href TEXT)")

    with con:
        cur.execute("SELECT Name FROM Things WHERE Name='%s'" %title)
        x=cur.fetchone()

    if con:
        con.close()

    return x

def _add(title,hreflink):
    download(hreflink)

    hreflink = hreflink.decode('utf-8')

    con = lite.connect('0.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Things(Name TEXT, Href TEXT)")
    with con:
        cur.execute("INSERT INTO Things VALUES(?,?)",(title,hreflink))
    if con:
        con.close()

def download(link):
    from telnetlib import Telnet
    tn = Telnet('127.0.0.1',4000)
    sleep(1)
    tn.write('dllink %s \r\n' %link)
    tn.close()
    


