import serial
#import pydirectinput

ser = serial.Serial('COM4', 9600, timeout=1)

while True:
    if ser.in_waiting:
        msg = ser.read().decode('utf-8')
        print(msg)
        #if(msg == "A"):
            #pydirectinput.press("space")
        #    print("space!")