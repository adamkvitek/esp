import ds18x20, onewire, network, tm1637
from machine import Pin
from time import sleep
from simple import MQTTClient

display = tm1637.TM1637(clk=Pin(32), dio=Pin(33))
display.brightness(3)

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.connect('Internet_28', '88DDA3656BACE8JA64EW') # connect to an AP

while not wlan.isconnected():
    print(". ", end="")
    sleep(1)    
print("\nWiFi connected!")

mqtt = MQTTClient("ESP32", "io.adafruit.com", user="Daskyleia", password="a552b53b29cb4cc2a2567d2739393c1d")
mqtt.connect()

ow = onewire.OneWire(Pin(22)) # create a OneWire bus
ds = ds18x20.DS18X20(ow)
rom = ds.scan()

while True:
    ds.convert_temp()
    sleep(5)
    temperature = ds.read_temp(rom[0])
    print(temperature)
    mqtt.publish(b"Daskyleia/feeds/temperature", str(temperature).encode("utf-8"))
    display.number(int(temperature))
