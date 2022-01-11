from machine import I2C, Pin

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
i2c_adresses = i2c.scan()

for address in i2c_adresses:
    print(address)

#print(i2c.scan())