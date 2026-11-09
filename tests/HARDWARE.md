# Register layout verification

Verified on 2026-11-09 with the same `hardware_pio.py` script:

| Device | Firmware | Clock | PIO blocks / state machines | Result |
|---|---|---|---|---|
| Pimoroni Tiny 2040 | MicroPython 1.29.0 | 125 MHz | 2 / 8 | Passed |
| Pimoroni Pico Plus 2 | Pimoroni MicroPython 1.29.0-2 | 150 MHz | 3 / 12 | Passed |

The script verifies native uctypes state-machine stride of 24 bytes, scalar PC and
instruction access, PC value 31, every CLKDIV register, IRQ controller stride of
12 bytes, raw IRQ force/clear and chip-dependent DMA request constants. It does
not drive output pins. Before the scalar-register correction, native uctypes
reported a state-machine size/stride of 268435488 bytes, misaddressing SM1 onward.

Descriptor offsets and fields follow the Raspberry Pi SDK's generated
[RP2040 PIO header](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2040/hardware_regs/include/hardware/regs/pio.h),
[RP2350 PIO header](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2350/hardware_regs/include/hardware/regs/pio.h)
and [RP2350 DREQ table](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2350/hardware_regs/include/hardware/regs/dreq.h).
