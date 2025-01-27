# LIGHT SPEED AHEAD, LUX PERPETUA

from time import time
from machine import Pin, Timer

horn = Pin(5, Pin.OUT)          #horn je připojená siréna
sensor = Pin(4, Pin.IN)         #světelný sensor

triggered = False
time_of_light = 0
timeout = 3                    
tim = Timer(-1)  # časovač               

                                # pokud se dvere lednicky, kde merime
                                # svetelnost, nezavrou do triceti sekund
                                # zacni vydavat zvuk, kdyz se pak zavrou
                                # vypni zvuk

def check_light(t):
    """Check light sensor and trigger horn with delay."""
    global triggered            # proměnnou timeout neoznačujeme jako globální,
    global time_of_light        # protože je v našem programu konstantní (time_of_light i triggered dostávají níže jiné hodnoty, než zadané výše)
    if sensor.value() == 0 and not triggered:
        time_of_light = time()          # poznamenej si aktualni čas
        triggered = True                # odjisti si = opdočitavame
        print("Budiž světlo.")
    elif sensor.value() == 1:           # tma
        triggered = False
        horn.off()
    elif triggered and time() - time_of_light >= timeout:   # pokud je světlo a jsi odjistěn + vypršel čas - začni znít          
        horn.on()
    
        
tim.init(period=1000, mode=Timer.PERIODIC, callback=check_light)                                         
                                                
       
