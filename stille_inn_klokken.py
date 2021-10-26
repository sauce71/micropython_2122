# Still klokken på mikrokontrolleren
import utime
import ntptime
t = utime.localtime() # Tid før klokken er stilt inn
print(t)

ntptime.settime() # Kobler til en timeserver og stiller klokken 

t = utime.localtime() # Tid etter klokken er stilt inn
print(t)
