import time
from machine import I2C, Pin
from bmp280 import *

i2c = I2C(scl=Pin(22), sda=Pin(21))

bmp = BMP280(i2c, use_case=BMP280_CASE_WEATHER)


bmp.use_case(BMP280_CASE_WEATHER)
bmp.oversample(BMP280_OS_HIGH)
bmp.power_mode = BMP280_POWER_FORCED

qnh=1013.25

while True:
    temperature = bmp.temperature
    pressure = bmp.pressure
    # Denne formelen er litt feil, hva er riktig
    altitude = ((pow((qnh / pressure), (1.0 / 5.257)) - 1) * (temperature + 273.15)) / 0.0065
    print(temperature, pressure, altitude)
    time.sleep(1)
