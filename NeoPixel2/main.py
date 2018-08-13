from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep_ms

analog = ADC(0)
np = NeoPixel (Pin(5),8)

def map(x, in_min, in_max, out_min, out_max):
    """ Map value from given range to target range. """
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)



while True:
    a = analog.read()
    if a > 512:
        np.fill((map(a, 512, 1024, 0, 255), 0, 0))
        np.write()
    else:    
        np.fill((0, 0, map(a, 0, 512, 0, 255)))
        np.write()
    sleep_ms(40)
