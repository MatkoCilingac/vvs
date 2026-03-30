from machine import Pin
from machine import PWM

buzzer : PWM = PWM(Pin(5), freq=2000, duty_u16= 10000)