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
    print(a)
    if a < 341:
        np.fill((0, 0, map(a, 0, 341, 0, 255)))
        np.write()
        print("blue")
    elif 341 < a < 682:   #a > 341 and a < 682:
        np.fill((0, map(a, 341, 682, 0, 255), 0))
        np.write()
        print("green")
    else:
        np.fill((map(a, 682, 1024, 0, 255), 0, 0))
        np.write()
        print("red")
    sleep_ms(80)
