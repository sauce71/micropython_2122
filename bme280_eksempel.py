import time
from machine import I2C, Pin
from BME280 import BME280

i2c = I2C(scl=Pin(22), sda=Pin(21))
bme = BME280(i2c=i2c)

qnh=1013.25
while True:
    temperature = bme.read_temperature() / 100
    pressure = bme.read_pressure() / 25600
    
    # Flyttalsverdiene
    print(temperature, pressure)
    # Strengveridene
    print(bme.temperature, bme.pressure)

    time.sleep(1)




