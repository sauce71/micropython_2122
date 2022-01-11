from machine import Pin
import neopixel
import time
pin = Pin(2, Pin.OUT)
np = neopixel.NeoPixel(pin, 8)
np[4] = (10,0,0)
np.write()

'''
while True:
    for i in range(8):
        for z in range(8): np[z] = (50,0,0)
        # np[i] = (10,0,0)
        np.write()
        time.sleep(0.5)
'''   