import serial
import time

ser = serial.Serial(4,9600)

def main():

    while 1:
        x = '\x01'
        ser.write(x)
        time.sleep(1)


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
