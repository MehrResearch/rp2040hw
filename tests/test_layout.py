"""Host checks for descriptors; real uctypes strides are checked on the devices."""
import types
import sys
from pathlib import Path
import unittest
from unittest.mock import patch


def load(name,rp2350):
    uctypes=types.ModuleType('uctypes')
    for key,value in {'BF_POS':17,'BF_LEN':22,'BFUINT32':0x40000000,
                      'ARRAY':0x80000000,'UINT32':0x20000000}.items():setattr(uctypes,key,value)
    uctypes.struct=lambda address,fields: (address,fields)
    util=types.ModuleType('rp2040hw.util');util.RP2350=rp2350
    machine=types.ModuleType('machine');machine.freq=lambda:150000000 if rp2350 else 125000000
    module=types.ModuleType('checked_'+name)
    module.const=lambda value:value
    with patch.dict(sys.modules,{'uctypes':uctypes,'rp2040hw.util':util,'machine':machine}):
        exec(compile((Path(__file__).parent.parent/(name+'.py')).read_text(),name+'.py','exec'),module.__dict__)
    return module


class LayoutTests(unittest.TestCase):
    def test_state_machine_registers_are_scalars_with_24_byte_stride(self):
        for chip in (False,True):
            p=load('pio',chip)
            self.assertIsInstance(p.SM_FIELDS['ADDR'],int)
            self.assertIsInstance(p.SM_FIELDS['INSTR'],int)
            self.assertEqual((p.SM_FIELDS['ADDR']>>22)&31,5)
            self.assertEqual((p.SM_FIELDS['INSTR']>>22)&31,16)
            offsets=[(value[0] if isinstance(value,tuple) else value)&0x1ffff for value in p.SM_FIELDS.values()]
            self.assertEqual(max(offsets)+4,24)
            self.assertEqual(len(p.PIO_BASE),3 if chip else 2)

    def test_instruction_memory_and_both_irq_views(self):
        for chip in (False,True):
            p=load('pio',chip)
            self.assertEqual(len(p.PIO_REGS['INSTR_MEM']),2)
            self.assertEqual(p.PIO_REGS['INSTR_MEM'][1]&0x1ffff,32)
            self.assertEqual(p.PIO_REGS['IRQ_FLAGS']&0x1ffff,0x30)
            self.assertEqual(p.PIO_REGS['IRQ0'][0],0x170 if chip else 0x12c)
            self.assertEqual(p.PIO_REGS['IRQ1'][0],0x17c if chip else 0x138)
            self.assertEqual(p.PIO_REGS['IRQ'][1],2)

    def test_current_clock_and_divider_edge_encoding(self):
        for chip in (False,True):
            p=load('pio',chip)
            with patch.dict(sys.modules,{'machine':types.SimpleNamespace(freq=lambda:150000000 if chip else 125000000)}):
                self.assertEqual(p.clkdiv(1000000),(150 if chip else 125,0))
            self.assertEqual(p.clkdiv(125000000/65536,125000000),(0,0))
            for bad in (0,-1,float('inf'),float('nan')):
                with self.subTest(chip=chip,bad=bad),self.assertRaises(ValueError):p.clkdiv(bad,125000000)

    def test_chip_specific_dma_requests(self):
        a,b=load('dma',False),load('dma',True)
        self.assertEqual((a.DREQ_SPI0_TX,a.DREQ_UART0_TX,a.DREQ_PWM_WRAP0,a.DREQ_I2C0_TX,a.DREQ_ADC),(16,20,24,32,36))
        self.assertEqual((b.DREQ_SPI0_TX,b.DREQ_UART0_TX,b.DREQ_PWM_WRAP0,b.DREQ_I2C0_TX,b.DREQ_ADC),(24,28,32,44,48))
        self.assertEqual((b.DREQ_PIO2_TX0,b.DREQ_PIO2_RX3,b.DREQ_PWM_WRAP11,b.DREQ_XIP_QMITX),(16,23,43,50))


if __name__=='__main__':unittest.main()
