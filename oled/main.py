from ssd1306 import SSD1306_I2C
from machine import I2C, Pin

i2c = I2C(scl=Pin(18), sda=Pin(19), freq=100000)

d = SSD1306_I2C(128, 64, i2c)

d.text("ahoj", 10, 10)
d.show()

# To delete the text for possible additions of a new text:
# d.fill(0)
