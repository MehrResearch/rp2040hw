# rp2040hw
Low-level access to RP2040 hardware registers in Micropython using uctypes

# Status
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
  - [ ] Sysinfo (2.20.2)
  - [ ] Syscfg (2.21.2)
- [ ] DMA (2.5.7)
- [X] GPIO (2.19.6)
- [x] PIO (3.7)
- Peripherals
  - [ ] USB (4.1.4)
  - [ ] UART (4.2.8)
  - [ ] I<sup>2</sup>C (4.3.17)
  - [ ] SPI (4.4.4)
  - [ ] PWM (4.5.3)
  - [ ] Timer (4.6.5)
  - [ ] Watchdog (4.7.6)
  - [ ] RTC (4.8.6)
  - [ ] ADC (4.9.6)
  - [ ] SSI (4.10.13)

# Credits
- [jbentham] for implementing uctypes access to some of RP2040's registers ([here][rpi_devices]), which inspired this project.

[jbentham]: https://github.com/jbentham
[rpi_devices]: https://github.com/jbentham/pico/blob/main/rp_devices.py