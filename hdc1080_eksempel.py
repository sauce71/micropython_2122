from hdc1080 import HDC1080
from machine import I2C, Pin
import time

i2c = I2C(scl=Pin(22), sda=Pin(21))
    # Adafruit sensor breakout has i2c addr: 90; Sparkfun: 91
    #s = CCS811.CCS811(i2c=i2c, addr=90)
s = HDC1080(i2c=i2c)

while True:
    print(s.read_temperature(celsius=True), s.read_humidity())
    time.sleep(1)
