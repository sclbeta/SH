#!/usr/bin/env python
import os
import sys
import threading

ser = serial.Serial('/dev/ttyAMA0',9600)

def irkz():
    while 1:
        xp = f.read()        #read mklkfifo and send the data
        if xp:
            ser.write(xp)
            ser.flushinput()

        uz = ser.inWaiting() #get the data
        if uz:
            nwrs = ser.read(uz)
            extra.jpuz(nwrs)    #call the function
        sleep(0.01)             #stay for while,let the cpu handle other things

def main():
    threads = []
    threads.append(threading.Thread(target = irkz,args = ''))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for thread in threads:
        if not thread.isAlive():
            thread.start()

if __name__ == "__main__":
    if not os.path.exists('/tmp/mklkfifo'):
        os.system('mkfifo /tmp/mklkfifo')
    f = file('/tmp/mklkfifo','r')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    main()
