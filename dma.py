#    Copyright 2025 Hessam Mehr
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from uctypes import BF_POS, BF_LEN, BFUINT32, ARRAY, UINT32, struct

DMA_BASE = const(0x50000000)

# --- DMA Channel Control Register Fields ---
DMA_CTRL_FIELDS = {
    "AHB_ERROR":        31 << BF_POS | 1 << BF_LEN | BFUINT32, # Read only: Logical OR of READ_ERROR and WRITE_ERROR
    "READ_ERROR":       30 << BF_POS | 1 << BF_LEN | BFUINT32, # Read only: Read bus error
    "WRITE_ERROR":      29 << BF_POS | 1 << BF_LEN | BFUINT32, # Read only: Write bus error
    # 28:25 reserved
    "BUSY":             24 << BF_POS | 1 << BF_LEN | BFUINT32, # Read only: Channel busy status
    "SNIFF_EN":         23 << BF_POS | 1 << BF_LEN | BFUINT32, # Enable sniffer
    "BSWAP":            22 << BF_POS | 1 << BF_LEN | BFUINT32, # Byte swap
    "IRQ_QUIET":        21 << BF_POS | 1 << BF_LEN | BFUINT32, # Disable IRQ generation for this channel
    "TREQ_SEL":         15 << BF_POS | 6 << BF_LEN | BFUINT32, # Transfer Request signal select
    "CHAIN_TO":         11 << BF_POS | 4 << BF_LEN | BFUINT32, # Channel to chain to after completion
    "RING_SEL":         10 << BF_POS | 1 << BF_LEN | BFUINT32, # Ring buffer wrap selector (0=read, 1=write)
    "RING_SIZE":        6 << BF_POS | 4 << BF_LEN | BFUINT32,  # Ring buffer size (log2)
    "INCR_WRITE":       5 << BF_POS | 1 << BF_LEN | BFUINT32, # Increment write address
    "INCR_READ":        4 << BF_POS | 1 << BF_LEN | BFUINT32, # Increment read address
    "DATA_SIZE":        2 << BF_POS | 2 << BF_LEN | BFUINT32,  # Transfer data size (byte/halfword/word)
    "HIGH_PRIORITY":    1 << BF_POS | 1 << BF_LEN | BFUINT32, # High priority channel
    "EN":               0 << BF_POS | 1 << BF_LEN | BFUINT32,  # Channel enable
}

# --- DMA Channel Register Aliases ---
# Writing to the last register in each alias struct triggers the channel.

# Alias 1: Trigger is TRANS_COUNT_TRIG
DMA_CHANNEL_ALIAS1_FIELDS = {
    "CTRL":             (0x00, DMA_CTRL_FIELDS),
    "READ_ADDR":        0x04 | UINT32,
    "WRITE_ADDR":       0x08 | UINT32,
    "TRANS_COUNT_TRIG": 0x0C | UINT32,
}

# Alias 2: Trigger is WRITE_ADDR_TRIG
DMA_CHANNEL_ALIAS2_FIELDS = {
    "CTRL":             (0x00, DMA_CTRL_FIELDS),
    "TRANS_COUNT":      0x04 | UINT32,
    "READ_ADDR":        0x08 | UINT32,
    "WRITE_ADDR_TRIG":  0x0C | UINT32,
}

# Alias 3: Trigger is READ_ADDR_TRIG
DMA_CHANNEL_ALIAS3_FIELDS = {
    "CTRL":             (0x00, DMA_CTRL_FIELDS),
    "WRITE_ADDR":       0x04 | UINT32,
    "TRANS_COUNT":      0x08 | UINT32,
    "READ_ADDR_TRIG":   0x0C | UINT32,
}

# --- Combined DMA Channel Structure ---
# Writing to CTRL_TRIG acts as trigger.
DMA_CHANNEL_FIELDS = {
    "READ_ADDR":        0x00 | UINT32,
    "WRITE_ADDR":       0x04 | UINT32,
    "TRANS_COUNT":      0x08 | UINT32,
    "CTRL_TRIG":        (0x0C, DMA_CTRL_FIELDS),

    "ALIAS1":           (0x10, DMA_CHANNEL_ALIAS1_FIELDS), # Trigger on TRANS_COUNT write
    "ALIAS2":           (0x20, DMA_CHANNEL_ALIAS2_FIELDS), # Trigger on WRITE_ADDR write
    "ALIAS3":           (0x30, DMA_CHANNEL_ALIAS3_FIELDS), # Trigger on READ_ADDR write
}

# DMA Interrupt Status Registers (INTR, INTE0/1, INTF0/1, INTS0/1)
DMA_INTS_FIELDS = {
    # Bits 0-11 for channels 0-11
    "INTS":             (0<<BF_POS | 16<<BF_LEN | BFUINT32)
}

# DMA Timer Registers (TIMER0 - TIMER3)
DMA_TIMER_FIELDS = {
    "X":                (16 << BF_POS | 16 << BF_LEN | BFUINT32), # Pacing Timer Dividend
    "Y":                (0 << BF_POS | 16 << BF_LEN | BFUINT32),  # Pacing Timer Divisor
}

# DMA Sniffer Control Register Fields
DMA_SNIFF_CTRL_FIELDS = {
    "OUT_INV":          11 << BF_POS | 1 << BF_LEN | BFUINT32, # Invert sniffed data before feeding to checksum
    "OUT_REV":          10 << BF_POS | 1 << BF_LEN | BFUINT32, # Bit-reverse sniffed data before feeding to checksum
    "BSWAP":            9 << BF_POS | 1 << BF_LEN | BFUINT32,  # Byte swap sniffed data before feeding to checksum
    "CALC":             5 << BF_POS | 4 << BF_LEN | BFUINT32,  # Checksum calculation type
    "DMACH":            1 << BF_POS | 4 << BF_LEN | BFUINT32,  # DMA channel for sniffer to observe
    "EN":               0 << BF_POS | 1 << BF_LEN | BFUINT32,  # Sniffer enable
}

# DMA FIFO Levels Register Fields (Read Only)
DMA_FIFO_LEVELS_FIELDS = {
    "WAF_LVL":          (16 << BF_POS | 8 << BF_LEN | BFUINT32), # Write Address FIFO level
    "RAF_LVL":          (8 << BF_POS | 8 << BF_LEN | BFUINT32),  # Read Address FIFO level
    "TDF_LVL":          (0 << BF_POS | 8 << BF_LEN | BFUINT32),  # Transfer Data FIFO level
}

# DMA Channel Abort Register Fields
DMA_CHAN_ABORT_FIELDS = {
    # Bits 0-11 for RP2040 channels 0-11
    "ABORT":            (0 << BF_POS | 16 << BF_LEN | BFUINT32)
}

# DMA Debug Channel Trigger Request Counter Fields (Read Only)
DMA_DBG_CTDREQ_FIELDS = {
    "CTDREQ":           (0 << BF_POS | 6 << BF_LEN | BFUINT32) # Current value of channel's DREQ counter
}

# DMA Debug Channel Structure
DMA_DEBUG_CHANNEL_FIELDS = {
    "CTDREQ":           (0x00, DMA_DBG_CTDREQ_FIELDS),
    "TCR":              0x04 | UINT32, # Debug Transfer Count Register reload value
}


# --- Main DMA Peripheral Structure Definition ---
DMA_FIELDS = {
    # Channels 0-11 (Array stride ensures correct 0x40 spacing)
    "CH":               (0x000 | ARRAY, 12, DMA_CHANNEL_FIELDS),
    # Interrupt Registers
    "INTR":             (0x400, DMA_INTS_FIELDS),       # Raw Interrupt Status
    "INTE0":            (0x404, DMA_INTS_FIELDS),       # Interrupt Enables for IRQ 0
    "INTF0":            (0x408, DMA_INTS_FIELDS),       # Interrupt Force for IRQ 0
    "INTS0":            (0x40C, DMA_INTS_FIELDS),       # Interrupt Status for IRQ 0 (masked & forced)
    # Reserved 0x410
    "INTE1":            (0x414, DMA_INTS_FIELDS),       # Interrupt Enables for IRQ 1
    "INTF1":            (0x418, DMA_INTS_FIELDS),       # Interrupt Force for IRQ 1
    "INTS1":            (0x41C, DMA_INTS_FIELDS),       # Interrupt Status for IRQ 1 (masked & forced)
    # Timers
    "TIMER":            (0x420 | ARRAY, 4, DMA_TIMER_FIELDS), # Pacing Timers 0-3
    # Miscellaneous Control
    "MULTI_CHAN_TRIGGER": 0x430 | BFUINT32,            # Trigger multiple channels simultaneously (bitmask)
    "SNIFF_CTRL":       (0x434, DMA_SNIFF_CTRL_FIELDS), # Sniffer Control
    "SNIFF_DATA":       0x438 | UINT32,                # Sniffer Data Accumulator
    # Reserved 0x43C
    "FIFO_LEVELS":      (0x440, DMA_FIFO_LEVELS_FIELDS),# (Read Only) Debug FIFO Levels
    "CHAN_ABORT":       (0x444, DMA_CHAN_ABORT_FIELDS), # Abort channel transfers (bitmask)
    "N_CHANNELS":       0x448 | UINT32,                # (Read Only) Number of DMA Channels implemented
    # Reserved space 0x44C to 0x7FC
    # Debug Registers (Array stride ensures correct 0x08 spacing)
    "CH_DBG":           (0x800 | ARRAY, 12, DMA_DEBUG_CHANNEL_FIELDS)
}

# --- Create the DMA structure instance ---
dma = struct(DMA_BASE, DMA_FIELDS)

# DMA_CTRL_FIELDS['DATA_SIZE']
DMA_SIZE_BYTE     = const(0)
DMA_SIZE_HALFWORD = const(1)
DMA_SIZE_WORD     = const(2)

# DMA_CTRL_FIELDS['RING_SIZE'] (Log2 size in bytes)
DMA_RING_SIZE_NONE = const(0)  # No wrapping
DMA_RING_SIZE_2B   = const(1)  # For halfword transfers
DMA_RING_SIZE_4B   = const(2)  # For word transfers
DMA_RING_SIZE_8B   = const(3)
DMA_RING_SIZE_16B  = const(4)
DMA_RING_SIZE_32B  = const(5)
DMA_RING_SIZE_64B  = const(6)
DMA_RING_SIZE_128B = const(7)
DMA_RING_SIZE_256B = const(8)
DMA_RING_SIZE_512B = const(9)
DMA_RING_SIZE_1KB  = const(10)
DMA_RING_SIZE_2KB  = const(11)
DMA_RING_SIZE_4KB  = const(12)
DMA_RING_SIZE_8KB  = const(13)
DMA_RING_SIZE_16KB = const(14)
DMA_RING_SIZE_32KB = const(15) # Maximum size

# DMA_CTRL_FIELDS['TREQ_SEL'] (Transfer Request Select)
# See RP2040 Datasheet Section 2.5.3.1, Table 119
# PIO TX DREQs
DREQ_PIO0_TX0 = const(0)
DREQ_PIO0_TX1 = const(1)
DREQ_PIO0_TX2 = const(2)
DREQ_PIO0_TX3 = const(3)
DREQ_PIO1_TX0 = const(8)
DREQ_PIO1_TX1 = const(9)
DREQ_PIO1_TX2 = const(10)
DREQ_PIO1_TX3 = const(11)
# PIO RX DREQs
DREQ_PIO0_RX0 = const(4)
DREQ_PIO0_RX1 = const(5)
DREQ_PIO0_RX2 = const(6)
DREQ_PIO0_RX3 = const(7)
DREQ_PIO1_RX0 = const(12)
DREQ_PIO1_RX1 = const(13)
DREQ_PIO1_RX2 = const(14)
DREQ_PIO1_RX3 = const(15)
# SPI DREQs
DREQ_SPI0_TX = const(16)
DREQ_SPI0_RX = const(17)
DREQ_SPI1_TX = const(18)
DREQ_SPI1_RX = const(19)
# UART DREQs
DREQ_UART0_TX = const(20)
DREQ_UART0_RX = const(21)
DREQ_UART1_TX = const(22)
DREQ_UART1_RX = const(23)
# PWM DREQs
DREQ_PWM_WRAP0 = const(24)
DREQ_PWM_WRAP1 = const(25)
DREQ_PWM_WRAP2 = const(26)
DREQ_PWM_WRAP3 = const(27)
DREQ_PWM_WRAP4 = const(28)
DREQ_PWM_WRAP5 = const(29)
DREQ_PWM_WRAP6 = const(30)
DREQ_PWM_WRAP7 = const(31)
# I2C DREQs
DREQ_I2C0_TX = const(32)
DREQ_I2C0_RX = const(33)
DREQ_I2C1_TX = const(34)
DREQ_I2C1_RX = const(35)
# ADC DREQ
DREQ_ADC = const(36)
# XIP DREQs
DREQ_XIP_STREAM = const(37)
DREQ_XIP_SSITX = const(38)
DREQ_XIP_SSIRX = const(39)
# Pacing Timers (0x3a reserved)
DREQ_TIMER0 = const(0x3b)
DREQ_TIMER1 = const(0x3c)
DREQ_TIMER2 = const(0x3d)
DREQ_TIMER3 = const(0x3e)
# Permanent request (unpaced transfer)
DREQ_PERMANENT = const(0x3f)

# DMA_SNIFF_CTRL_FIELDS['CALC'] (Sniffer checksum calculation)
DMA_SNIFF_CALC_CRC32  = const(0)
DMA_SNIFF_CALC_CRC32R = const(1)  # Bit reversed data
DMA_SNIFF_CALC_CRC16  = const(2)
DMA_SNIFF_CALC_CRC16R = const(3)  # Bit reversed data
# 4-13 reserved
DMA_SNIFF_CALC_EVEN   = const(14) # XOR reduction over all data
DMA_SNIFF_CALC_SUM    = const(15) # Simple 32-bit checksum (addition)