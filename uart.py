from uctypes import BF_POS, BF_LEN, BFUINT32, struct
from rp2040hw.util import RP2350

if RP2350:
    UART_BASE = [0x40070000, 0x40078000]
else:
    UART_BASE = [0x40034000, 0x40038000]

DR_FIELDS = {
    "OE":  11 << BF_POS | 1 << BF_LEN | BFUINT32, # Overrun error
    "BE":  10 << BF_POS | 1 << BF_LEN | BFUINT32, # Break error
    "PE":   9 << BF_POS | 1 << BF_LEN | BFUINT32, # Parity error
    "FE":   8 << BF_POS | 1 << BF_LEN | BFUINT32, # Framing error
    "DATA": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # Data character
}

RSR_FIELDS = {
    "OE": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # Overrun error
    "BE": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # Break error
    "PE": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # Parity error
    "FE": 0 << BF_POS | 1 << BF_LEN | BFUINT32, # Framing error
}

FR_FIELDS = {
    "RI":   8 << BF_POS | 1 << BF_LEN | BFUINT32, # Ring indicator
    "TXFE": 7 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit FIFO empty
    "RXFF": 6 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive FIFO full
    "TXFF": 5 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit FIFO full
    "RXFE": 4 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive FIFO empty
    "BUSY": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit busy
    "DCD":  2 << BF_POS | 1 << BF_LEN | BFUINT32, # Data carrier detect
    "DSR":  1 << BF_POS | 1 << BF_LEN | BFUINT32, # Data set ready
    "CTS":  0 << BF_POS | 1 << BF_LEN | BFUINT32, # Clear to send
}

ILPR_FIELDS = {
    "ILPDVSR": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # Low-power divisor
}

IBRD_FIELDS = {
    "BAUD_DIVINT": 0 << BF_POS | 16 << BF_LEN | BFUINT32, # Integer baud rate divisor
}

FBRD_FIELDS = {
    "BAUD_DIVFRAC": 0 << BF_POS | 6 << BF_LEN | BFUINT32, # Fractional baud rate divisor
}

LCR_H_FIELDS = {
    "SPS":  7 << BF_POS | 1 << BF_LEN | BFUINT32, # Stick parity select
    "WLEN": 5 << BF_POS | 2 << BF_LEN | BFUINT32, # Word length
    "FEN":  4 << BF_POS | 1 << BF_LEN | BFUINT32, # Enable FIFOs
    "STP2": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # Two stop bits select
    "EPS":  2 << BF_POS | 1 << BF_LEN | BFUINT32, # Even parity select
    "PEN":  1 << BF_POS | 1 << BF_LEN | BFUINT32, # Parity enable
    "BRK":  0 << BF_POS | 1 << BF_LEN | BFUINT32, # Send break
}

CR_FIELDS = {
    "CTSEN": 15 << BF_POS | 1 << BF_LEN | BFUINT32, # CTS hardware flow enable
    "RTSEN": 14 << BF_POS | 1 << BF_LEN | BFUINT32, # RTS hardware flow enable
    "OUT2":  13 << BF_POS | 1 << BF_LEN | BFUINT32, # OUT2 / RI modem status
    "OUT1":  12 << BF_POS | 1 << BF_LEN | BFUINT32, # OUT1 / DCD modem status
    "RTS":   11 << BF_POS | 1 << BF_LEN | BFUINT32, # Request to send
    "DTR":   10 << BF_POS | 1 << BF_LEN | BFUINT32, # Data transmit ready
    "RXE":    9 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive enable
    "TXE":    8 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit enable
    "LBE":    7 << BF_POS | 1 << BF_LEN | BFUINT32, # Loopback enable
    "SIRLP":  2 << BF_POS | 1 << BF_LEN | BFUINT32, # SIR low-power IrDA mode
    "SIREN":  1 << BF_POS | 1 << BF_LEN | BFUINT32, # SIR enable
    "UARTEN": 0 << BF_POS | 1 << BF_LEN | BFUINT32, # UART enable
}

IFLS_FIELDS = {
    "RXIFLSEL": 3 << BF_POS | 3 << BF_LEN | BFUINT32, # Receive interrupt FIFO level select
    "TXIFLSEL": 0 << BF_POS | 3 << BF_LEN | BFUINT32, # Transmit interrupt FIFO level select
}

IMSC_FIELDS = {
    "OEIM":  10 << BF_POS | 1 << BF_LEN | BFUINT32, # Overrun error interrupt mask
    "BEIM":   9 << BF_POS | 1 << BF_LEN | BFUINT32, # Break error interrupt mask
    "PEIM":   8 << BF_POS | 1 << BF_LEN | BFUINT32, # Parity error interrupt mask
    "FEIM":   7 << BF_POS | 1 << BF_LEN | BFUINT32, # Framing error interrupt mask
    "RTIM":   6 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive timeout interrupt mask
    "TXIM":   5 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit interrupt mask
    "RXIM":   4 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive interrupt mask
    "DSRMIM": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # DSR modem interrupt mask
    "DCDMIM": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # DCD modem interrupt mask
    "CTSMIM": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # CTS modem interrupt mask
    "RIMIM":  0 << BF_POS | 1 << BF_LEN | BFUINT32, # RI modem interrupt mask
}

RIS_FIELDS = {
    "OERIS":  10 << BF_POS | 1 << BF_LEN | BFUINT32, # Overrun error raw interrupt status
    "BERIS":   9 << BF_POS | 1 << BF_LEN | BFUINT32, # Break error raw interrupt status
    "PERIS":   8 << BF_POS | 1 << BF_LEN | BFUINT32, # Parity error raw interrupt status
    "FERIS":   7 << BF_POS | 1 << BF_LEN | BFUINT32, # Framing error raw interrupt status
    "RTRIS":   6 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive timeout raw interrupt status
    "TXRIS":   5 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit raw interrupt status
    "RXRIS":   4 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive raw interrupt status
    "DSRRMIS": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # DSR modem raw interrupt status
    "DCDRMIS": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # DCD modem raw interrupt status
    "CTSRMIS": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # CTS modem raw interrupt status
    "RIRMIS":  0 << BF_POS | 1 << BF_LEN | BFUINT32, # RI modem raw interrupt status
}

MIS_FIELDS = {
    "OEMIS":  10 << BF_POS | 1 << BF_LEN | BFUINT32, # Overrun error masked interrupt status
    "BEMIS":   9 << BF_POS | 1 << BF_LEN | BFUINT32, # Break error masked interrupt status
    "PEMIS":   8 << BF_POS | 1 << BF_LEN | BFUINT32, # Parity error masked interrupt status
    "FEMIS":   7 << BF_POS | 1 << BF_LEN | BFUINT32, # Framing error masked interrupt status
    "RTMIS":   6 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive timeout masked interrupt status
    "TXMIS":   5 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit masked interrupt status
    "RXMIS":   4 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive masked interrupt status
    "DSRMMIS": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # DSR modem masked interrupt status
    "DCDMMIS": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # DCD modem masked interrupt status
    "CTSMMIS": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # CTS modem masked interrupt status
    "RIMMIS":  0 << BF_POS | 1 << BF_LEN | BFUINT32, # RI modem masked interrupt status
}

ICR_FIELDS = {
    "OEIC":  10 << BF_POS | 1 << BF_LEN | BFUINT32, # Overrun error interrupt clear
    "BEIC":   9 << BF_POS | 1 << BF_LEN | BFUINT32, # Break error interrupt clear
    "PEIC":   8 << BF_POS | 1 << BF_LEN | BFUINT32, # Parity error interrupt clear
    "FEIC":   7 << BF_POS | 1 << BF_LEN | BFUINT32, # Framing error interrupt clear
    "RTIC":   6 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive timeout interrupt clear
    "TXIC":   5 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit interrupt clear
    "RXIC":   4 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive interrupt clear
    "DSRMIC": 3 << BF_POS | 1 << BF_LEN | BFUINT32, # DSR modem interrupt clear
    "DCDMIC": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # DCD modem interrupt clear
    "CTSMIC": 1 << BF_POS | 1 << BF_LEN | BFUINT32, # CTS modem interrupt clear
    "RIMIC":  0 << BF_POS | 1 << BF_LEN | BFUINT32, # RI modem interrupt clear
}

DMACR_FIELDS = {
    "DMAONERR": 2 << BF_POS | 1 << BF_LEN | BFUINT32, # DMA receive request disable on error
    "TXDMAE":   1 << BF_POS | 1 << BF_LEN | BFUINT32, # Transmit DMA enable
    "RXDMAE":   0 << BF_POS | 1 << BF_LEN | BFUINT32, # Receive DMA enable
}

PERIPHID0_FIELDS = {
    "PARTNUMBER0": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # These bits read back as 0x11
}

PERIPHID1_FIELDS = {
    "DESIGNER0":   4 << BF_POS | 4 << BF_LEN | BFUINT32, # These bits read back as 0x1
    "PARTNUMBER1": 0 << BF_POS | 4 << BF_LEN | BFUINT32, # These bits read back as 0x0
}

PERIPHID2_FIELDS = {
    "REVISION":  4 << BF_POS | 4 << BF_LEN | BFUINT32, # This field depends on the revision of the UART
    "DESIGNER1": 0 << BF_POS | 4 << BF_LEN | BFUINT32, # These bits read back as 0x4
}

PERIPHID3_FIELDS = {
    "CONFIGURATION": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # These bits read back as 0x00
}

PCELLID0_FIELDS = {
    "UARTPCELLID0": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # These bits read back as 0x0D
}

PCELLID1_FIELDS = {
    "UARTPCELLID1": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # These bits read back as 0xF0
}

PCELLID2_FIELDS = {
    "UARTPCELLID2": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # These bits read back as 0x05
}

PCELLID3_FIELDS = {
    "UARTPCELLID3": 0 << BF_POS | 8 << BF_LEN | BFUINT32, # These bits read back as 0xB1
}

UART_REGS = {
    "UARTDR":    (0x000, DR_FIELDS),
    "UARTRSR":   (0x004, RSR_FIELDS),
    "UARTFR":    (0x018, FR_FIELDS),
    "UARTILPR":  (0x020, ILPR_FIELDS),
    "UARTIBRD":  (0x024, IBRD_FIELDS),
    "UARTFBRD":  (0x028, FBRD_FIELDS),
    "UARTLCR_H": (0x02C, LCR_H_FIELDS),
    "UARTCR":    (0x030, CR_FIELDS),
    "UARTIFLS":  (0x034, IFLS_FIELDS),
    "UARTIMSC":  (0x038, IMSC_FIELDS),
    "UARTRIS":   (0x03C, RIS_FIELDS),
    "UARTMIS":   (0x040, MIS_FIELDS),
    "UARTICR":   (0x044, ICR_FIELDS),
    "UARTDMACR": (0x048, DMACR_FIELDS),
    "UARTPERIPHID0": (0xFE0, PERIPHID0_FIELDS),
    "UARTPERIPHID1": (0xFE4, PERIPHID1_FIELDS),
    "UARTPERIPHID2": (0xFE8, PERIPHID2_FIELDS),
    "UARTPERIPHID3": (0xFEC, PERIPHID3_FIELDS),
    "UARTPCELLID0":  (0xFF0, PCELLID0_FIELDS),
    "UARTPCELLID1":  (0xFF4, PCELLID1_FIELDS),
    "UARTPCELLID2":  (0xFF8, PCELLID2_FIELDS),
    "UARTPCELLID3":  (0xFFC, PCELLID3_FIELDS),
}

uarts = [struct(addr, UART_REGS) for addr in UART_BASE]

UART_WLEN_5BIT = const(0)
UART_WLEN_6BIT = const(1)
UART_WLEN_7BIT = const(2)
UART_WLEN_8BIT = const(3)
