# rp2040hw
Low-level access to RP2040 hardware registers in MicroPython using uctypes

## What's it good for?
The Raspberry Pi RP2040 microcontroller powers a range of versatile and very powerful development boards, including the [Raspberry Pi Pico] and the [Pimoroni Tiny 2040].The RP2040 Python SDK doesn't cover the chip's full hardware capabilities. Direct register access using the modules in this package allows full control of RP2040's low-level operations using Micropython.

## Status
The following shows progress towards bindings for all documented RP2040 registers, with [datasheet] sections shown in brackets. Please feel free to contribute new bindings or open an issue/submit a PR if you find any bugs.

- Core
  - [ ] Bus fabric (2.1.5)
  - [ ] Cortex-M0+  (2.4.8)
  - [ ] Chip-level reset (2.12.8)
  - [ ] Power-on state machine (2.13.5)
  - [ ] Subsystem resets (2.14.3)
  - [ ] Clocks (2.15.7)
  - [ ] Crystal oscillator (2.16.7)
  - [ ] Ring oscillator (2.17.8)
  - [ ] PLL (2.18.4)
  - [X] Sysinfo (2.20.2)
  - [ ] Syscfg (2.21.2)
- [X] DMA (2.5.7)
- [X] GPIO (2.19.6)
- [X] PIO (3.7)
- Peripherals
  - [ ] USB (4.1.4)
  - [ ] UART (4.2.8)
  - [ ] I<sup>2</sup>C (4.3.17)
  - [ ] SPI (4.4.4)
  - [X] PWM (4.5.3)
  - [ ] Timer (4.6.5)
  - [ ] Watchdog (4.7.6)
  - [ ] RTC (4.8.6)
  - [X] ADC (4.9.6)
  - [ ] SSI (4.10.13)

## Credits
- [jbentham] for implementing uctypes access to some of RP2040's registers ([here][rp_devices]), which inspired this project.

[jbentham]: https://github.com/jbentham
[rp_devices]: https://github.com/jbentham/pico/blob/main/rp_devices.py
[Raspberry Pi Pico]: https://www.raspberrypi.org/products/raspberry-pi-pico/
[Pimoroni Tiny 2040]: https://shop.pimoroni.com/products/tiny-2040
[datasheet]: https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf