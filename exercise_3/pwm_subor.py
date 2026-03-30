import time

from machine import Pin
from machine import PWM

green_led : PWM = PWM(Pin(11),freq=50,duty_u16=0)
red_led = PWM(Pin(21),freq=50,duty_u16=0)
blue_led = PWM(Pin(10),freq=50,duty_u16=0)

def calculate_PWM(value: int) -> int:
    x: int = int(value / 255)
    z: int = int(x * 100)


while True:
    user_input : int = int(input("enter i in range 0 - 255 for green "))
    green_led.duty_u16(calculate_PWM(user_input))
    user_input: int = int(input("enter i in range 0 - 255 for red"))
    red_led.duty_u16(calculate_PWM(user_input))
    user_input: int = int(input("enter i in range 0 - 255 for blue"))
    blue_led.duty_u16(calculate_PWM(user_input))