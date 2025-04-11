from uctypes import BF_POS, BF_LEN, BFUINT32, ARRAY, UINT32, struct

PWM_BASE = const(0x40050000)

CSR_FIELDS = {
    "PH_ADV": 7 << BF_POS | 1 << BF_LEN | BFUINT32, # Self-clearing: Advance counter phase by 1 while running
    "PH_RET": 6 << BF_POS | 1 << BF_LEN | BFUINT32, # Self-clearing: Retard counter phase by 1 while running
    "DIVMODE": 4 << BF_POS | 2 << BF_LEN | BFUINT32, # See DIVMODE constants
    "B_INV": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # Invert output B
    "A_INV": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # Invert output A
    "PH_CORRECT": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # 1: Phase-correct modulation 
    "EN": 0 << BF_POS | 1 << BF_LEN | BFUINT32, # Enable channel
}

# Counting rate = System clock / (INT + FRAC/16)
DIV_FIELDS = {
    "INT": 4 << BF_POS | 8 << BF_LEN | BFUINT32,
    "FRAC": 0 << BF_POS | 16 << BF_LEN | BFUINT32,
}

CC_FIELDS = {
    "B": 16 << BF_POS | 16 << BF_LEN | BFUINT32,
    "A": 0 << BF_POS | 16 << BF_LEN | BFUINT32,
}

CHANNEL_FIELDS = {
    "CSR": (0x00, CSR_FIELDS),
    "DIV": (0x04, DIV_FIELDS),
    "CTR": 0x08 | 0 << BF_POS | 16 << BF_LEN | BFUINT32, # Read only: Direct access to PWM counter
    "CC": (0x0c, CC_FIELDS),
    "TOP": 0x10 | 0 << BF_POS | 16 << BF_LEN | BFUINT32, # Counter wrap value
}

PWM_FIELDS = {
    "CH": (0x00, ARRAY, 8, CHANNEL_FIELDS),
    # 1 bit per channel (CH0–CH7) for the following registers
    "EN": 0xa0 | 0 << BF_POS | 8 << BF_LEN | BFUINT32,
    "INTR": 0xa4 | 0 << BF_POS | 8 << BF_LEN | BFUINT32, # Raw interrupts
    "INTE": 0xa8 | 0 << BF_POS | 8 << BF_LEN | BFUINT32, # Interrupt enable
    "INTF": 0xac | 0 << BF_POS | 8 << BF_LEN | BFUINT32, # Interrupt force
    "INTS": 0xb0 | 0 << BF_POS | 8 << BF_LEN | BFUINT32, # Interrupt status
}

pwm = struct(PWM_BASE, PWM_FIELDS)

# Free-running counting dictated by fractional divider
CSR_DIVMODE_DIV = const(0x0)
# Fractional divider gated by PWM B pin
CSR_DIVMODE_LEVEL = const(0x1)
# Advance counter with rising PWM B pin
CSR_DIVMODE_RISE = const(0x2)
# Advance counter with falling PWM B pin
CSR_DIVMODE_FALL = const(0x3)