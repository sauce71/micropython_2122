from machine import PWM, Pin

p_red=PWM(Pin(15),1000)
p_green=PWM(Pin(2),1000)
p_blue=PWM(Pin(0),1000)

def set_rgb(r, g, b):
    p_red.duty((1024//255)*r)
    p_green.duty((1024//255)*g)
    p_blue.duty((1024//255)*b)

while True:
    for r in range(256):
        for g in range(256):
            for b in range(256):
                set_rgb(r,g,b)


