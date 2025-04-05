import machine
import uctypes
import time
from rp2040hw.dma import *
from rp2040hw import gpio
from array import array

LED_PIN_NUM = 18       # GPIO pin for the LED
DMA_CHANNEL = 0        # Choose a free DMA channel (0-11)
DMA_TIMER_NUM = 0      # Choose a free DMA timer (0-3)
BLINK_FREQ_HZ = 3000   # Blink frequency in Hertz (min ~ 2000)

gpio_ctrl_addr = uctypes.addressof(gpio.io_bank0.GPIOS[18].CTRL)

led_pin = machine.Pin(LED_PIN_NUM, machine.Pin.OUT)

# 0x205: LED OFF, 0x305: LED ON
dma_data_buffer = array('L', [0x205, 0x305])
dma_data_addr = uctypes.addressof(dma_data_buffer)

# Configure DMA pacing timer
sys_clk_hz = machine.freq()
timer_divider = sys_clk_hz // BLINK_FREQ_HZ
dma.TIMER[DMA_TIMER_NUM].X = 1
dma.TIMER[DMA_TIMER_NUM].Y = timer_divider

ch = dma.CH[DMA_CHANNEL]

ch.CTRL_TRIG.EN = 0

ch.READ_ADDR = dma_data_addr
ch.WRITE_ADDR = gpio_ctrl_addr           # LED GPIO control register
ch.TRANS_COUNT = 1000                    # No. 32-bit words to transfer

ch.CTRL_TRIG.CHAIN_TO = DMA_CHANNEL      # Chain to self for continuous operation
ch.CTRL_TRIG.TREQ_SEL = DREQ_TIMER0 + DMA_TIMER_NUM # Paced by selected Timer
ch.CTRL_TRIG.INCR_WRITE = 0              # Keep writing to the same register
ch.CTRL_TRIG.INCR_READ = 1
ch.CTRL_TRIG.DATA_SIZE = DMA_SIZE_WORD   # Transfer size: 32 bits
ch.CTRL_TRIG.RING_SIZE=3                 # 2 x 4 bytes
ch.CTRL_TRIG.EN = 1


print(f"DMA Blinking LED on GPIO {LED_PIN_NUM} using DMA Channel {DMA_CHANNEL} and Timer {DMA_TIMER_NUM}")
print(f"Target Frequency: {BLINK_FREQ_HZ} Hz")
print(f"DMA Timer Config: X={dma.TIMER[DMA_TIMER_NUM].X}, Y={dma.TIMER[DMA_TIMER_NUM].Y}")
print("DMA started. Running indefinitely...")

while True:
    try:
        time.sleep(1.0)
        ch.ALIAS1.TRANS_COUNT_TRIG = 1000
        print(ch.TRANS_COUNT, ch.READ_ADDR)
    except KeyboardInterrupt:
        print("Stopping DMA...")
        dma.CH[DMA_CHANNEL].CTRL_TRIG.EN = 0
        print("DMA stopped.")
        break

