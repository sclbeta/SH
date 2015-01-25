from extra.models import vsdrhc,mklk

def fass(x,y):  #get sqlte3's object and write the data to mklkfifo,then the 'ser' function can read
    x1 = vsdrhc.object.get(wwvsdrhc=x)
    x1 = x1.vfvsdrhc
    y1 = mklk.object.get(wwvsdrhc=y)
    y1 = y1.vfmklk
    mklk = str(x1) + str(y1)

    f = file('/tmp/mklkfifo','w')
    f.write(mklk)
    f.close()

def jpuz(nwrs):#get the data from 'ser' function and judge what to do
    pass
