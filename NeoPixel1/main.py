from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms   # možné i: from time import sleep


np = NeoPixel(Pin(4),8)     # pin změněn z pěti na čtyři!

while True:
    for i in range(7):
        np.fill((0,0,0))
        np[i]=(10,10,10)
        np.write()
        sleep_ms(100)
    for i in range(7, 0, -1):
        np.fill((0,0,0))
        np[i]=(15,0,15)
        np.write()
        sleep_ms(100)   # Zapojení - DIn (digital input)
                        # na Pin5 -- libovolná barva, napětí červené
                        # 5v/3v3/vcc, GND černě či modře
        
