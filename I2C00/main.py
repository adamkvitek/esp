import network
from machine import Pin, RTC, unique_id, I2C
from ssd1306 import SSD1306_I2C
from time import sleep, sleep_ms

# MQTT and Wifi credentials
wifi_ssid = "Internet_28"
wifi_pass = "88DDA3656BACE8JA64EW"
mqtt_server = "176.74.137.214"
mqtt_user = "adam"
mqtt_pass = "daskyleia"
mqtt_topic = "/adam/test"
mqtt_connection_name = "honey"

# Create RTC object and sync time with NTP server
rtc = RTC()
rtc.ntp_sync("cz.pool.ntp.org")

# LED for new MQTT message notification
led = Pin(22, Pin.OUT)
led.value(1)

# Create I2C and oled display objects
i2c = I2C(scl=Pin(19), sda=Pin(18), speed=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Connect to Wifi network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_pass)
while not wlan.isconnected():
    print(". ", end="")
    sleep(1) 
print("\nWiFi connected!")

def data_cb(data):
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
    simple_message(message)

# Create MQTT client object
c = network.mqtt(name=mqtt_connection_name,
                 server=mqtt_server,
                 user=mqtt_user,
                 password=mqtt_pass,
                 autoreconnect=True,
                 clientid=str(unique_id()),
                 data_cb=data_cb)

sleep(1)  # Empirical delay for successful topic subscribe

# Check connection and subscribe
if c.status()[0]:
    c.subscribe(mqtt_topic)

def simple_message(msg):
   oled.fill(0)
   oled.text(msg, 10, 10)
   oled.show()
