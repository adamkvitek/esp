import network
from machine import Pin, RTC
from time import sleep, sleep_ms

# MQTT and Wifi credentials
wifi_ssid = "tux" # Internet_28 
wifi_pass = "Ohyae4na" # 88DDA3656BACE8JA64EW
mqtt_server = "176.74.137.214"
mqtt_user = "Adam"
mqtt_pass = "daskyleia"
mqtt_topic = "/adam/test"
mqtt_connection_name = "honey"



# Create RTC object and sync time with server
rtc = RTC()
rtc.ntp_sync("cz.pool.ntp.org")

# LED for new MQTT message notification
led = Pin(22, Pin.OUT)
led.value(1)

# Connect to Wifi network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_pass)

while not wlan.isconnected():
    print(". ", end="")
    sleep(1)    
print("\nWiFi connected!")

def message_cb(data):
    """Handle new MQTT message callback."""
    # LED notification blink
    led.value(0)
    sleep_ms(50)
    led.value(1)

    # connection = data[0])
    # topic = data[1]
    message = data[2]
    now = rtc.now()
    # Print timestamp and message payload
    print("{}:{}:{} {}".format(now[3], now[4], now[5], message))


# Create MQTT client object
c = network.mqtt(name=mqtt_connection_name,
                 server=mqtt_server,
                 user=mqtt_user,
                 password=mqtt_pass,
                 autoreconnect=True,
                 data_cb=message_cb)

sleep(1)  # Empirical delay for successful topic subscribe

# Check connection and subscribe
if c.status()[0]:
    c.subscribe(mqtt_topic)
