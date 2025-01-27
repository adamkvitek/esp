from dht import DHT22
from machine import Pin, Timer
from time import sleep_ms
from neopixel import NeoPixel

np = NeoPixel(Pin(4),8)
d = DHT22(Pin(5))
tim = Timer(-1)

def measure_environment(t):
    d.measure()
    print(str(d.temperature())+"C"+" "+str(d.humidity())+"%")
    
tim.init(period=1000, mode=Timer.PERIODIC, callback=measure_environment)

while True:
    for i in range(7):
        np.fill((0,0,0))
        np[i]=(10,10,10)
        np.write()
        sleep_ms(200)
    for i in range(7, 0, -1):
        np.fill((0,0,0))
        np[i]=(15,0,15)
        np.write()
        sleep_ms(200)




                        # pin změněn z pěti na čtyři!
                        # Zapojení - DIn (digital input)
                        # na Pin5 -- libovolná barva, napětí červené
                        # 5v/3v3/vcc, GND černě či modře
        
