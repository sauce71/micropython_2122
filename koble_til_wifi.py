# Koble til nett
import network
import time
sta_if = network.WLAN(network.STA_IF) # Initialiserer nett i valig modus / kan også settes opp som tilgangspunkt
sta_if.active(True) # Aktivere nettverk


wifi_networks = sta_if.scan() # Skanner for tilgjengelige nettverk
print('Tilgjengelige nettverk')
for net in wifi_networks: # Printer tilgjengelig nettverk
    print(net)

sta_if.connect('VG3Data', 'Admin:1234') # Kobler til wifi
while not sta_if.isconnected(): # Venter på at tilkobling er klar
    time.sleep(0.1)

print('IP adresse')
print(sta_if.ifconfig()) # Printer IP adresse du har fått fra DHCP

