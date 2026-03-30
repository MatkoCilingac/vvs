from machine import Pin
from machine import ADC
import time
import neopixel


serial_leds : neopixel.NeoPixel = neopixel.NeoPixel(Pin(8), 3)


photoresistor : ADC = ADC(Pin(3), atten = ADC.ATTN_11DB)

#print (photoresistor.read_u16())
#raw_value : int = photoresistor.read_u16()
#prepocet na percenta
#percentage : float = raw_value / (65535/100)

#calculation to voltage
#voltage : float = percentage * (3.3/100)

while True:
    raw_value: int = photoresistor.read_u16()
    percentage: float = raw_value / (65535 / 100)
    led_percentage: int = int(percentage * (255/100))
    if led_percentage <= 3 : led_percentage = 0



    serial_leds[0] = (led_percentage, 0, 0)
    serial_leds[1] = (0, led_percentage, 0)
    serial_leds[2] = (0, 0, led_percentage)
    serial_leds.write()