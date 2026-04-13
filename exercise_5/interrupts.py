from machine import Pin
from machine import Timer

timer_1 : Timer = Timer(1)
timer_2 : Timer = Timer(0)

red : Pin = Pin(21, Pin.OUT, value=0)

timer_2_flag : bool = False

def inq_timer_1(x) :
    global red
    if red.value() == 1:
        red.value(0)
    else :
        red.value(1)

def inq_timer_2(x) :
    global timer_2_flag
    timer_2_flag = True

timer_1.init(period=2000, mode=Timer.PERIODIC, callback=inq_timer_1)
timer_2.init(period=10000, mode=Timer.ONE_SHOT, callback=inq_timer_2)

while not timer_2_flag :
    pass
print("10 seconds have passed")
timer_2.deinit()