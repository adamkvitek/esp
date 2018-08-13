import network
from time import sleep
from machine import Pin
from simple import MQTTClient
from neopixel import NeoPixel

np = NeoPixel(Pin(22), 8)

colour = (0, 0, 0)
count = (0)

topic_colour = b"Daskyleia/feeds/colour"  
topic_count = b"Daskyleia/feeds/count"

wlan = network.WLAN(network.STA_IF)                 # create station interface
wlan.active(True)                                   # activate the interface
wlan.connect('Internet_28', '88DDA3656BACE8JA64EW') # connect to an AP

while not wlan.isconnected():
    print(". ", end="")
    sleep(1)    
print("\nWiFi connected!")

def colour_callback(topic, msg):
    global colour
    global count
    if topic == topic_colour:   # react to MQTT topic_colour
        colour = tuple(map(int,msg.decode("utf-8")[4:-1].split(",")))
                                # change rgb string to tuple
        print(colour)
    elif topic == topic_count:  # change the number of lighted pixels
        count = int(msg.decode("utf-8"))
        print(count)
    
    for i in range(8):          # display no colour
        np[i]= (0,0,0)
    np.write()
    
    for i in range(count):      # display number of pixels according to topic_count
        np[i]= colour           # Martine, prosím Tě, uniká mi spojení mezi hodnotou count a topicem topic_count. Hodnota, která přijde z topic_count, kde, co a jak ví, že to, co přijde z topic_count je hodnota count?
    np.write()
    
"""  colour_callback displays colour on NeoPixel strip through MQTT application in android. Number of lighted pixels can be changed (from 0 to 8).  """

mqtt = MQTTClient("ESP32", "io.adafruit.com", user="Daskyleia", password="a552b53b29cb4cc2a2567d2739393c1d")
mqtt.set_callback(colour_callback)
mqtt.connect()
mqtt.subscribe(topic_colour)
mqtt.subscribe(topic_count)

while True:
    mqtt.wait_msg()
