import os
import serial
from time import sleep
from extra import extra

if not os.path.exists('/tmp/mklkfifo'):
    os.system('mkfifo /tmp/mklkfifo')

f = file('/tmp/mklkfifo','r')

#open the serial
ser = serial.Serial(4,9600)

def main():
    while 1:
        xp = f.read()        #read mklkfifo and send the data
        if xp:
            ser.write(xp)
            ser.flushinput()
            
        uz = ser.inwaiting() #get the data
        if uz:
            nwrs = ser.read(uz)
            extra.jpuz(nwrs)    #call the function
        sleep(0.01)             #stay for while,let the cpu handle other things

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
            f.close()
            

        


