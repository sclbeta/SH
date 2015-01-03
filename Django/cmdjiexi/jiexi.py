import os

if not os.path.exists('/tmp/mklkfifo'):
    os.mkfifo('/tmp/mklkfifo')

def main(vsdrhc,mklk):
    x = fvsdrhc(vsdrhc)
    y = fmklk(mklk)
    xpru(x,y)

def fvsdrhc(vsdrhc):
    f = file('vsdrhc',r)
    pass
    f.close()

def fmklk(mklk):
    f = file('mklk',r)
    pass
    f.close()

def xpru(x,y):
    mklk = x + y
    f = file('/tmp/mklkfifo',w)
    f.write()
    

