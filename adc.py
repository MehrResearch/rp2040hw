#    Copyright 2025 Hessam Mehr

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from uctypes import BF_POS, BF_LEN, BFUINT32, struct

ADC_BASE = 0x4004c000

# ADC control and status
CS_FIELDS = {
    "RROBIN": 16 << BF_POS | 5 << BF_LEN | BFUINT32, # Round-robin mode; one bit per channel
    "AINSEL": 12 << BF_POS | 3 << BF_LEN | BFUINT32, # Selected channel number; updated automatically in round-robin mode
    "ERR_STICKY": 10 << BF_POS | 1 << BF_LEN | BFUINT32, # Write to clear past ADC conversion error
    "ERR": 9 << BF_POS | 1 << BF_LEN | BFUINT32, # Read only: Most recent conversion caused an error
    "READY": 8 << BF_POS | 1 << BF_LEN | BFUINT32, # Read only: 0 => Conversion in progress 1 => Ready to start new conversion
    "START_MANY": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # Continuously convert while 1
    "START_ONCE": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # Self clearing: Start single conversion
    "TS_EN": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # Temperature sensor enable/disbable
    "EN": 0 << BF_POS | 1 << BF_LEN | BFUINT32, # ADC + clock enable/disable
}

# FIFO control and status
FCS_FIELDS = {
    "THRESH": 24 << BF_POS | 4 << BF_LEN | BFUINT32, # DREQ/IRQ when level>=threshold
    "LEVEL": 16 << BF_POS | 5 << BF_LEN | BFUINT32, # Current results in FIFO
    "OVER": 11 << BF_POS | 1 << BF_LEN | BFUINT32, # Write to clear FIFO overflow
    "UNDER": 10 << BF_POS | 1 << BF_LEN | BFUINT32, # Write to clear FIFO underflow
    "FULL": 9 << BF_POS | 1<< BF_LEN | BFUINT32, # Read only
    "EMPTY": 8<< BF_POS | 1 << BF_LEN | BFUINT32, # Read only
    "DREQ_EN": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # If 1 assert DREQ when FIFO contains data
    "ERR": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # Include error bit in
    "SHIFT": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # Right shift results to be 1 byte
    "EN": 0 << BF_POS | 1 << BF_LEN | BFUINT32, # Write result to FIFO after each conversion
}

FIFO_FIELDS = {
    "ERR": 15 << BF_POS | 1 << BF_LEN | BFUINT32,
    "VAL": 0 << BF_POS | 12 << BF_LEN | BFUINT32,
}

# ADC clock divider = 1 + INT + FRAC/256
DIV_FIELDS = {
    "INT": 8 << BF_POS | 16 << BF_LEN | BFUINT32,
    "FRAC": 0 << BF_POS | 8 << BF_LEN | BFUINT32,
}

ADC_FIELDS = {
    "CS": (0x00, CS_FIELDS),
    "RESULT": 0x04 | 0 << BF_POS | 12 << BF_LEN | BFUINT32,
    "FCS": (0x08, FCS_FIELDS),
    "FIFO": (0x0c, FIFO_FIELDS),
    "DIV": (0x10, DIV_FIELDS),
    "INTR": 0x14 | 0 << BF_POS | 1 << BF_LEN | BFUINT32, # Read only
    "INTE": 0x18 | 0 << BF_POS | 1 << BF_LEN | BFUINT32, # Interrupt enable
    "INTF": 0x1c | 0 << BF_POS | 1 << BF_LEN | BFUINT32, # Interrupt force
    "INTS": 0x20 | 0 << BF_POS | 1 << BF_LEN | BFUINT32, # Interrupt status
}

adc = struct(ADC_BASE, ADC_FIELDS)