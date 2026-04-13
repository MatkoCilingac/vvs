from machine import Pin
from machine import UART



uart_instance : UART = UART(1)
uart_instance.init(baudrate=9600, bits=8, parity=None, stop=1)
uart_instance.init(tx=Pin(15), rx=Pin(23))
uart_instance.init(timeout=0, timeout_char=0)
buffer :str =""
while True:


    user_input: bytes= bytes(input('enter a message '), 'utf-8')
    uart_instance.write(user_input)

    if uart_instance.txdone() is False:
        pass

    while uart_instance.any() != 0:
        uart_input: str = str(uart_instance.read(1), 'utf-8')
        if uart_input == ';':
            print(f"The uart message is: {buffer}")
            buffer = ''
        else:
            buffer += uart_input