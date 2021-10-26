# Bruk av urequest for å hente data fra internett - eksempel med bitcoint kurser
import urequests
r = urequests.get('https://blockchain.info/ticker')

print(r.text) # Dette viser rå data som blei hentet

d = r.json() # Json funksjonen konverterer JSON data til en dict
for c in d: # Skriver ut hver key-> value i dict
    print(c, d[c])