import os

if not os.path.exists('/tmp/mklkfifo'):
    os.system('mkfifo /tmp/mklkfifo')

def duqu(wfjmmk,ww):
    temp = {}
    f = file(wfjmmk,'r')
    alllines = f.readlines()
    for eachline in alllines:
        x,y = eachline.split(':')
        temp[x] = y
    f.close()
    return temp[ww]


def fass(wwvsdrhc,wwmklk):
    x = duqu('vsdrhc',wwvsdrhc)
    y = duqu('mklk',wwmklk)
    mklk = x + y
    f = file('mklkfifo','w')
    f.write(mklk)
    f.close()
