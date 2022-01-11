from machine import Pin, disable_irq, enable_irq
import time
import neopixel
pin = Pin(15, Pin.OUT)
np = neopixel.NeoPixel(pin, 9, bpp=4)

button = Pin(12, Pin.IN, Pin.PULL_DOWN)


button_pressed = False

def handle_button(b):
    global button_pressed
    #state = disable_irq()
  
    time.sleep_ms(20)
    if button.value():
        button_pressed = True
    #enable_irq(state)
    

button.irq(handle_button, Pin.IRQ_RISING)

direction = 0
pos = 0

def clear(neo):
    for i in range(len(neo)):
        neo[i] = (0,0,0)
    neo.write()

while True:
    np[0] = (127,0,0, 127)
    np.write()
    """
    for i in range(len(np)):
        if button_pressed:
            direction *= -1
            button_pressed = False
            clear(np)
            break
        clear(np)
        np[i] = (0,0,127)
        np.write()
        time.sleep_ms(200)
        #pos += direction
    """