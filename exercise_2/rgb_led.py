
from time import sleep

from machine import Pin
class RGBled:
    def __init__(self):
            self.blue_light: Pin = Pin(10, Pin.OUT, value=0)
            self.green_light: Pin = Pin(11, Pin.OUT, value=0)
            self.red_light: Pin = Pin(21, Pin.OUT, value=0)

    def ukaz_cervena(self) -> None:
        self.blue_light.value(0)
        self.green_light.value(0)
        self.red_light.value(1)

    def ukaz_zelena(self) -> None:
        self.blue_light.value(0)
        self.green_light.value(1)
        self.red_light.value(0)

    def ukaz_modra(self) -> None:
        self.blue_light.value(1)
        self.green_light.value(0)
        self.red_light.value(0)

    def ukaz_cervena(self) -> None:
        self.blue_light.value(0)
        self.green_light.value(0)
        self.red_light.value(1)

    def ukaz_slabomodra(self) -> None:
        self.blue_light.value(1)
        self.green_light.value(1)
        self.red_light.value(0)

    def ukaz_zlta(self) -> None:
        self.blue_light.value(0)
        self.green_light.value(1)
        self.red_light.value(1)

    def ukaz_ruzova(self) -> None:
        self.blue_light.value(1)
        self.green_light.value(0)
        self.red_light.value(1)

    def efektos(self) -> None:
        self.blue_light.value(0)
        self.green_light.value(0)
        self.red_light.value(1)
        sleep(0.5)
        self.blue_light.value(0)
        self.green_light.value(1)
        self.red_light.value(0)
        sleep(0.5)
        self.blue_light.value(1)
        self.green_light.value(0)
        self.red_light.value(0)
        sleep(0.5)
        self.blue_light.value(1)
        self.green_light.value(0)
        self.red_light.value(1)
        sleep(0.5)
        self.blue_light.value(0)
        self.green_light.value(1)
        self.red_light.value(1)
        sleep(0.5)
        self.blue_light.value(1)
        self.green_light.value(1)
        self.red_light.value(0)
        sleep(0.5)
        self.blue_light.value(1)
        self.green_light.value(1)
        self.red_light.value(1)
        sleep(0.5)
