from extra.models import vsdrhc,mklk

'''
def fass(x):  #get sqlte3's object and write the data to mklkfifo,then the 'ser' function can read
    x1 = vsdrhc.object.get(wwvsdrhc=x)
    x1 = x1.vfvsdrhc
    y1 = mklk.object.get(wwvsdrhc=y)
    y1 = y1.vfmklk
    mklk = str(x1) + str(y1)
    '''

def jpuz(nwrs):#get the data from 'ser' function and judge what to do
    mklk = {
        'fe':'\xfe',
        'fd':'\xfd',
        'fb':'\x01',
        'f7':'\x02',
        }
    xpru(mklk[nwrs.encode('hex')])

def xpru(mklk):
    f = file('/tmp/mklkfifo','w')
    f.write(mklk)
    f.close()
