from extra.models import vsdrhc,mklk

def fass(x,y):
	x1 = vsdrhc.object.get(wwvsdrhc=x)
	x1 = x1.vfvsdrhc
	y1 = mklk.object.get(wwvsdrhc=y)
	y1 = y1.vfmklk
    mklk = str(x1) + str(y1)
	
	f = file('/tmp/mklkfifo','w')
    f.write(mklk)
    f.close()