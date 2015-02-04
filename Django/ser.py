import os
from time import sleep
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
f = file('/tmp/mklkfifo','r')


def mainx():
    while 1:
        xp = f.read()        #read mklkfifo and send the data
        if xp:
            ser.write(xp)
            ser.flushInput()

        uz = ser.inWaiting() #get the data
        if uz:
            nwrs = ser.read(uz)
            main.jpuz(nwrs)    #call the function
        sleep(0.01)             #stay for while,let the cpu handle other things

if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from extra import main

    try:
        mainx()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
            f.close()
