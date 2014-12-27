import json
import urllib2

def jiexi():
    html = urllib2.urlopen('http://localhost:8000/clock/dispjson').read()
    html = html.replace('&quot;','"')
    data = json.loads(html.decode('utf-8'))
    #print type(data),data
    #print data[0]['fields']


if __name__ == '__main__':
    jiexi()
