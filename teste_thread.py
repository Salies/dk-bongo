import threading

a = 0

def tt():
    global a
    a += 1

threading.Timer(1.0, tt).start()

while True:
    print(a)