from dht import DHT22
from machine import Pin
from time import sleep


d = DHT22(Pin(5))

while True:
    d.measure()
    print(str(d.temperature())+"C"+" "+str(d.humidity())+"%")
    sleep(1)
