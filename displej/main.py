import tm1637
from machine import Pin, ADC
from time import sleep_ms

analog = ADC(0)
display = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

display.brightness(3)


while True:
    display.number(analog.read())
    sleep_ms(200)
