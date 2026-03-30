import neopixel
from machine import Pin

serial_leds : neopixel.NeoPixel = neopixel.NeoPixel(Pin(8), 3)
#serial_leds[0] = (255, 0, 0)
#serial_leds[1] = (0, 255, 0)
#serial_leds[2] = (0, 0, 255)
#serial_leds.write()

cislo1: int = 0
cislo2: int = 0
cislo3: int = 0
while True:
    print("zadaj cislo od 0 - 255 pre rozsvietenie intenzity prvej ledky")
    try:
        cislo1 = int(input("cislo > "))
    except ValueError:
        print("nezadal si cislo")
        continue
    if (cislo1 >= 0 and cislo1 <= 255):
         break
    else :
        print("zadal is zle cislo")
        continue
while True:
    print("zadaj cislo od 0 - 255 pre rozsvietenie intenzity druhej ledky")
    try:
        cislo2 = int(input("cislo > "))
    except ValueError:
        print("nezadal si cislo")
        continue
    if (cislo2 >= 0 and cislo2 <= 255):
         break
    else :
        print("zadal is zle cislo")
        continue
while True:
    print("zadaj cislo od 0 - 255 pre rozsvietenie intenzity tretej ledky")
    try:
        cislo3 = int(input("cislo > "))
    except ValueError:
        print("nezadal si cislo")
        continue
    if (cislo3 >= 0 and cislo3 <= 255):
         break
    else :
        print("zadal is zle cislo")
        continue

serial_leds[0] = (cislo1, 0, 0)
serial_leds[1] = (0, cislo2, 0)
serial_leds[2] = (0, 0, cislo3)
serial_leds.write()




print("daj 1, aby si vypol")
cislo: int = int(input("cislo > "))
if cislo == 1:
    serial_leds[0] = (0, 0, 0)
    serial_leds[1] = (0, 0, 0)
    serial_leds[2] = (0, 0, 0)
    serial_leds.write()