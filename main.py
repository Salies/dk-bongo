import serial
import pydirectinput
from threading import Timer

mp_timing = 0.5 # multipress timeout
mp = False
# temporizers for simultaneous pressing detection
def mp_timeout():
    global mp
    mp = False

ser = serial.Serial('COM3', 9600, timeout = 1)

while True:
    if ser.in_waiting:
        msg = ser.read().decode('utf-8')
        if msg == "L":
            if(mp == "R"):
                pydirectinput.keyDown("shift")
                pydirectinput.press("alt")
                pydirectinput.keyUp("shift")
                mp = False
            else:
                pydirectinput.press("alt")
                mp = "L"
                Timer(mp_timing, mp_timeout).start()
        elif msg == "R":
            if(mp == "L"):
                pydirectinput.keyDown("alt")
                pydirectinput.press("shift")
                pydirectinput.keyUp("alt")
                mp = False
            else:
                pydirectinput.press("shift")
                mp = "R"
                Timer(mp_timing, mp_timeout).start()  

# TODO: prevent double input on multipress