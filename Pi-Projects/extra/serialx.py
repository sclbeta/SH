import serial
import time

ser = serial.Serial(4,9600)
f = file('/tmp/mklkfifo','r')

def main():
    while 1:
        xp = f.read()
        if xp:
            ser.write(xp)
            ser.flushinput()

        uz = ser.inwaiting()
        if uz:
            nwrs = ser.read(uz)
            print nwrs
        
        time.sleep(0.1)


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
            f.close()
