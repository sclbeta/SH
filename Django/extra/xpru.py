import os
from time import sleep

if not os.path.exists('/tmp/mklkfifo'):
    os.system('mkfifo /tmp/mklkfifo')

def fass(mklk):
    f = file('mklkfifo','w')
    f.write(str(x))
    f.close()
