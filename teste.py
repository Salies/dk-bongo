import serial
from time import sleep
#import pydirectinput

ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    if ser.in_waiting and not trigger:
        msg = ser.read().decode('utf-8')
        print(msg)
        #if(msg == "A"):
            #pydirectinput.press("space")
        #    print("space!")