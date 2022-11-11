import serial
import pydirectinput

ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    if ser.in_waiting:
        msg = ser.read().decode('utf-8')
        if(msg == "A"):
            print("yamete")
            pydirectinput.press("shift")