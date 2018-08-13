from machine import Pin, ADC    # z modulu stroj importuj třídy Pin a ADC (analog digital convertor = transducer -- převodník)
from neopixel import NeoPixel   # z modulu neopixel imortuj ...
from time import sleep_ms       # z modulu čas importuj třídu spánek v milisekundách

# objekt je instance třídy, instance je konkrétní realizace,
# třída je předpis jak má obecný objekt vypadat

analog = ADC(0)     # vytvoř objekt třídy ADC s názvem analog a parametry ADC (0) -- konrétně čip ESP8266 má jen jeden analog odtud 0
np = NeoPixel(Pin(4),8) # vytvoř objekt třídy NeoPixel s parametry... a názvem np (4) = na kterém pinu je připojený, 8 = počet pixelů.


def map(value, range, led_count):   # !!! Proměnné zadané funkci v závorkách zanikají s ukončením čtení dané funkce, proměnné téhož názvu níže
                                    # se mohou jmenovat stejně, jedná se však o jiné proměnné. !!!
    """
    Map value to given range.
    
    Args:
        value (int):     Value ought to be mapped.
        range (int):     Range of value.
        led_count (int): Number of leds on NeoPixel strip.
        
    Returns:             
        (int): Mapped value.             
    """ 
    
    # vždy když budu mít def, napsat dokomuntační řetězec (doc, string) co daná funkce dělá -- musí být imperativ!
    return int(value/range*led_count)


def led_bar(led_count, colour):

    """
    Light given number of leds with given colour.
    
    Args:
        led_count (int): Number of leds on NeoPixel strip.
        colour (touple): RGB value of colour
    """

    np.fill((0, 0, 0))      # abych nemusel dělat for funkci -- np.fill ((0, 0, 0)) aktuální hodnotu nastaví na 0
    for led in range(led_count):    # dočasná proměnná led nabývá hodnoty od nuly do led_count
        np[led] = colour    # np je list, hranaté závorky odkazují na konkrétní položku listu[], konkrétně na led...
    np.write()
      
        
while True:
    led_bar(map(analog.read(), 1024, 8), (255, 0, 0))
    sleep_ms(100)



