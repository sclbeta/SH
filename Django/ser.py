import serial

def send(x):
    serx = serial.Serial(4,9600)
    serx.write(x)
    serx.close()