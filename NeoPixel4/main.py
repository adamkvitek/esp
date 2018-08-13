from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep_ms


analog = ADC(0)
np = NeoPixel(Pin(4),8)


def map(value, range, target_value):   # !!! Proměnné zadané funkci v závorkách zanikají s ukončením čtení dané funkce, proměnné téhož názvu níže
                                    # se mohou jmenovat stejně, jedná se však o jiné proměnné. !!!
    """
    Map value to given range.
    
    Args:
        value (int):     Value ought to be mapped.
        range (int):     Range of value.
        target_value (int): Number of leds on NeoPixel strip.
        
    Returns:             
        (int): Mapped value.             
    """ 
    
    return int(value/range*target_value)


def led_bar(target_value, colour):

    """
    Light given number of leds with given colour.
    
    Args:
        target_value (int): Number of leds on NeoPixel strip.
        colour (touple): RGB value of colour
    """

    np.fill((0, 0, 0))      # abych nemusel dělat for funkci -- np.fill ((0, 0, 0)) aktuální hodnotu nastaví na 0
    for led in range(target_value):    # dočasná proměnná led nabývá hodnoty od nuly do target_value
        np[led] = colour    # np je list, hranaté závorky odkazují na konkrétní položku listu[], konkrétně na led...
    np.write()
      

# Následuje jádro programu, 
while True:
    tripleledcount = map(analog.read(), 1024, 24) # přemapuj hodnotu potenciometru na 24 (protože třikrát osm je 24, chceme tři barvy jako na semaforu)
    if tripleledcount < 8:
        # led_bar(tripleledcount, (0, 90, 0))
        led_bar(tripleledcount, (0, 0, 90))
        print(tripleledcount)
        print("green")
    elif tripleledcount < 16:
        led_bar(tripleledcount - 8, (45, 45, 0))
        print(tripleledcount)
        print("yellow")
    else:
        led_bar(tripleledcount - 16, (90, 0, 0))
        print(tripleledcount)
        print("red")
sleep_ms(30)

# line 50 (elif) odebráno tripleledcount >= 8 and
