# -*- coding: utf-8 -*-

import urllib2
import re
import sqlite3 as lite
import json
from time import sleep,ctime

def main(title,link):
    if re.search('\r|\n',link):
        link = link[:-1]
    content = urllib2.urlopen(link).read()
    name=re.findall(title,content)
    title = max(name)
    print title
    if not _check(title):
        pass
    
def _check(title):
    #print title
    con = lite.connect('0.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Things(Name TEXT, Href TEXT)")
    with con:
        cur.execute("SELECT Name FROM Things WHERE Name='%s'" %title)
        x=cur.fetchone()
    if con:
        con.close()
    return x

def jiexi(link):
    pass