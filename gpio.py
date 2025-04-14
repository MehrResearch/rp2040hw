#    Copyright 2023–25 Hessam Mehr

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from uctypes import BF_POS, BF_LEN, BFUINT32, ARRAY, UINT32, struct

IO_BANK0_BASE   = const(0x40014000)
IO_QSPI_BASE    = const(0x40018000)
PADS_BANK0_BASE = const(0x4001c000)
PADS_QSPI_BASE  = const(0x40020000)

STATUS_FIELDS = {
    "IRQTOPROC": 26 << BF_POS | 1 << BF_LEN | BFUINT32,
    "IRQFROMPAD": 24 << BF_POS | 1 << BF_LEN | BFUINT32,
    "INTOPERI": 19 << BF_POS | 1 << BF_LEN | BFUINT32,
    "INFROMPAD": 17 << BF_POS | 1 << BF_LEN | BFUINT32,
    "OETOPAD": 13 << BF_POS | 1 << BF_LEN | BFUINT32,
    "OEFROMPERI": 12 << BF_POS | 1 << BF_LEN | BFUINT32,
    "OUTTOPAD": 9 << BF_POS | 1 << BF_LEN | BFUINT32,
    "OUTFROMPERI": 8 << BF_POS | 1 << BF_LEN | BFUINT32,
}

CTRL_FIELDS = {
    "IRQOVER": 28 << BF_POS | 2 << BF_LEN | BFUINT32,
    "INOVER": 16 << BF_POS | 2 << BF_LEN | BFUINT32,
    "OEOVER": 12 << BF_POS | 2 << BF_LEN | BFUINT32,
    "OUTOVER": 8 << BF_POS | 2 << BF_LEN | BFUINT32,
    "FUNCSEL": 0 << BF_POS | 5 << BF_LEN | BFUINT32,
}

GPIO_FIELDS = {
    "STATUS": (0x0, STATUS_FIELDS),
    "CTRL": (0x4, CTRL_FIELDS),
}

# INTR_FIELDS = [{
#      'EDGE_HIGH': offset + 3 << BF_POS | 1 << BF_LEN | BFUINT32,
#      'EDGE_LOW': offset + 2 << BF_POS | 1 << BF_LEN | BFUINT32,
#      'LEVEL_HIGH': offset + 1 << BF_POS | 1 << BF_LEN | BFUINT32,
#      'LEVEL_LOW': offset + 0 << BF_POS | 1 << BF_LEN | BFUINT32,
# } for offset in range(0, 32, 4)]

IO_QSPI_FIELDS = {
    "SCLK": (0x00, GPIO_FIELDS),
    "SS": (0x08, GPIO_FIELDS),
    "SD0": (0x10, GPIO_FIELDS),
    "SD1": (0x18, GPIO_FIELDS),
    "SD2": (0x20, GPIO_FIELDS),
    "SD3": (0x28, GPIO_FIELDS),
    "INTR": 0x30 | UINT32,
    "PROC0_INTE": 0x34 | UINT32,
    "PROC0_INTF": 0x38 | UINT32,
    "PROC0_INTS": 0x3C | UINT32,
    "PROC1_INTE": 0x40 | UINT32,
    "PROC1_INTF": 0x44 | UINT32,
    "PROC1_INTS": 0x48 | UINT32,
    "DORMANT_WAKE_INTE": 0x40 | UINT32,
    "DORMANT_WAKE_INTF": 0x44 | UINT32,
    "DORMANT_WAKE_INTS": 0x48 | UINT32,
}

io_qspi = struct(IO_QSPI_BASE, IO_QSPI_FIELDS)

IO_BANK0_FIELDS = {
    "GPIO": (0x000 | ARRAY, 30, GPIO_FIELDS),
    "INTR": (0x0F0 | ARRAY, 4 | UINT32),
    "PROC0_INTE": (0x100 | ARRAY, 4 | UINT32),
    "PROC0_INTF": (0x110 | ARRAY, 4 | UINT32),
    "PROC0_INTS": (0x120 | ARRAY, 4 | UINT32),
    "PROC1_INTE": (0x130 | ARRAY, 4 | UINT32),
    "PROC1_INTF": (0x140 | ARRAY, 4 | UINT32),
    "PROC1_INTS": (0x150 | ARRAY, 4 | UINT32),
    "DORMANT_WAKE_INTE": (0x130 | ARRAY, 4 | UINT32),
    "DORMANT_WAKE_INTF": (0x140 | ARRAY, 4 | UINT32),
    "DORMANT_WAKE_INTS": (0x150 | ARRAY, 4 | UINT32),
}

io_bank0 = struct(IO_BANK0_BASE, IO_BANK0_FIELDS)

GPIO_PAD_FIELDS = {
    "OD": 7 << BF_POS | 1 << BF_LEN | UINT32, # Output disable
    "IE": 6 << BF_POS | 1 << BF_LEN | UINT32, # Input enable
    "DRIVE": 4 << BF_POS | 2 << BF_LEN | UINT32, # Drive strength, see PADS_DRIVE_*
    "PUE": 3 << BF_POS | 1 << BF_LEN | UINT32, # Pull-up enable
    "PDE": 2 << BF_POS | 1 << BF_LEN | UINT32, # Pull-down enable
    "SCHMITT": 1 << BF_POS | 1 << BF_LEN | UINT32,
    "SLEWFAST": 0 << BF_POS | 1 << BF_LEN | UINT32,
}

PADS_BANK0_FIELDS = {
    "VOLTAGE_SELECT": 0x00 | 0 << BF_POS | 1 << BF_LEN | BFUINT32,
    "GPIO": (0x04 | ARRAY, 30, GPIO_PAD_FIELDS),
    "SWCLK": (0x7C, GPIO_PAD_FIELDS),
    "SWD": (0x80, GPIO_PAD_FIELDS),
}

pads_bank0 = struct(PADS_BANK0_BASE, PADS_BANK0_FIELDS)

PADS_QSPI_FIELDS = {
    "VOLTAGE_SELECT": 0x00 | 0 << BF_POS | 1 << BF_LEN | BFUINT32,
    "QSPI_SCLK": (0x04, GPIO_PAD_FIELDS),
    "QSPI_SD0": (0x08, GPIO_PAD_FIELDS),
    "QSPI_SD1": (0x0C, GPIO_PAD_FIELDS),
    "QSPI_SD2": (0x10, GPIO_PAD_FIELDS),
    "QSPI_SD3": (0x14, GPIO_PAD_FIELDS),
    "QSPI_SS": (0x18, GPIO_PAD_FIELDS),
}

pads_qspi = struct(PADS_QSPI_BASE, PADS_QSPI_FIELDS)

# GPIO Voltage Select (for VOLTAGE_SELECT in PADS_BANK0 and PADS_QSPI)
GPIO_VOLTAGE_3V3 = const(0) # 3.3V
GPIO_VOLTAGE_1V8 = const(1) # 1.8V

# GPIO Override Modes (for IRQOVER, INOVER, OEOVER, OUTOVER in CTRL_FIELDS)
GPIO_OVERRIDE_NORMAL = const(0) # Drive output from peripheral/pad input is passed to peripheral
GPIO_OVERRIDE_INVERT = const(1) # Invert output/input
GPIO_OVERRIDE_LOW    = const(2) # Drive output low/input is low
GPIO_OVERRIDE_HIGH   = const(3) # Drive output high/input is high

GPIO_FUNC_XIP         = const(0)
GPIO_FUNC_SPI         = const(1)
GPIO_FUNC_UART        = const(2)
GPIO_FUNC_I2C         = const(3)
GPIO_FUNC_PWM         = const(4)
GPIO_FUNC_SIO         = const(5) # Software control via SIO registers
GPIO_FUNC_PIO0        = const(6) # Programmable IO block 0
GPIO_FUNC_PIO1        = const(7) # Programmable IO block 1
GPIO_FUNC_GPCK        = const(8) # General purpose clock output
GPIO_FUNC_USB         = const(9) # USB VBUS detect/overcurrent
GPIO_FUNC_NULL        = const(31) # Default, disables connection to peripheral

PADS_DRIVE_2MA  = const(0)
PADS_DRIVE_4MA  = const(1)
PADS_DRIVE_8MA  = const(2)
PADS_DRIVE_12MA = const(3)