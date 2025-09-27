from rp2040hw import gpio
from machine import mem32, Pin
from uctypes import addressof
from time import sleep

# Need to adjust to match LED pin
LED_PIN_NUM = 25

ctrl_reg = gpio.io_bank0.GPIO[LED_PIN_NUM].CTRL
ctrl_reg_addr = addressof(ctrl_reg)
ctrl_reg_val = mem32[ctrl_reg_addr]

print(f'Initial value of control register: {mem32[ctrl_reg_addr]:032b}')

pin = Pin(LED_PIN_NUM, Pin.OUT)

print(f'Value after pin initialization: {mem32[ctrl_reg_addr]:032b}')

while True:
    sleep(1)
    ctrl_reg.OEOVER = 0x2
    print(f'Pin low: {mem32[ctrl_reg_addr]:04x}')
    sleep(1)
    ctrl_reg.OEOVER = 0x3
    print(f'Pin high: {mem32[ctrl_reg_addr]:04x}')
