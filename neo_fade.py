from machine import Pin
import neopixel
import time
pin = Pin(15, Pin.OUT)
np = neopixel.NeoPixel(pin, 9)

def clear():
    for i in range(9):
        np[i] = [0,0,0]
    np.write()

while True:
    for i in range(9):
        #clear()
        np[i] = [255,0,0]
        for r in range(i-1, -1, -1):
            rt = list(np[r])
            rt[0] = rt[0] - 30
            np[r] = rt
            print(r, rt)

        np.write()
        time.sleep_ms(200)
        
