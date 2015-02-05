from extra.models import vsdrhc,mklk
from switch.models import Switch
from django.shortcuts import render,get_object_or_404

'''
def fass(x):  #get sqlte3's object and write the data to mklkfifo,then the 'ser' function can read
    x1 = vsdrhc.object.get(wwvsdrhc=x)
    x1 = x1.vfvsdrhc
    y1 = mklk.object.get(wwvsdrhc=y)
    y1 = y1.vfmklk
    mklk = str(x1) + str(y1)
    '''

def jpuz(nwrs):#get the data from 'ser' function and judge what to do
    x = nwrs.encode('hex')
    mklk = {
        'f2':['\xfe',1,1],
        'f1':['\xfd',2,1],
        'f8':['\x01',1,0],
        'f4':['\x02',2,0],
        }

    try:
        xpru(mklk[x][0])
        l = get_object_or_404(Switch,pk = mklk[x][1])
        l.status = mklk[x][2]
        l.save()
    except:
        print x

def xpru(mklk):
    f = file('/tmp/mklkfifo','w')
    f.write(mklk)
    f.close()
