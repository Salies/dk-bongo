import serial
import pydirectinput as dinput
from threading import Timer

ser = serial.Serial('COM3', 9600, timeout = 1)

mp = False
mp_time = 0.05
def mp_timeout(key, expected):
    global mp
    if(mp == expected):
        mp = -1 # prevent double input afterwards
        dinput.hotkey(key, expected)
        return
    elif(mp == -1):
        return
    print(key)
    dinput.keyDown(key)
    dinput.keyUp(key)

while True:
    if ser.in_waiting:
        msg = ser.read()
        if(msg == b'L'):
            mp = 'L'
            Timer(mp_time, mp_timeout, ['L', 'R']).start()
        elif(msg == b'R'):
            mp = 'R'
            Timer(mp_time, mp_timeout, ['R', 'L']).start()