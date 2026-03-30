
from time import sleep

import time

import exercise_2.rgb_led
from machine import Pin

from exercise_2.rgb_led import RGBled

button1 :Pin = Pin(2, Pin.IN, Pin.PULL_UP)

ledka : RGBled = RGBled()
pocitadlo : int = 0
zmena : bool = False
while True:
    if button1.value() == 0:
        if zmena == False:
            time.sleep_us(20)
            if button1.value() == 0:
                ledka.ukaz_slabomodra()
                zmena = True


    else:
        ledka.ukaz_zlta()
        zmena = False






