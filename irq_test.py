from machine import Pin, disable_irq, enable_irq
import time

button = Pin(12, Pin.IN, Pin.PULL_DOWN)

button_pressed = False

# Bruker en IRQ håndterer for å endre en variable når knappe er trykket.
# Slipper da å holde knappen inne for å vente til koden faktisk sjekker at knappen er trykket
def handle_button(b):
    global button_pressed
    state = disable_irq() # Forhindrer at andre irq kjører mens denne pågår
  
    time.sleep_ms(20)
    if b.value():
        button_pressed = True
    enable_irq(state)

# Binder irq til pinne, bruker "risning edge". Kan også bruke "falling edge"
button.irq(handle_button, Pin.IRQ_RISING)


while True:
    if button_pressed:
        print('Button pressed')
        button_pressed = False
        


