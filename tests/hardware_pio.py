"""Run after a reset on an otherwise idle RP2040/RP2350; no output pins used."""
import uctypes,json,machine,rp2
from rp2040hw.pio import pios,SM_FIELDS,clkdiv
from rp2040hw.util import RP2350
from rp2040hw import dma as bindings

assert uctypes.sizeof(SM_FIELDS)==24,uctypes.sizeof(SM_FIELDS)
assert len(pios)==(3 if RP2350 else 2)
assert clkdiv(1000000)==(machine.freq()//1000000,0)

@rp2.asm_pio()
def idle():
    nop()

machines=[]
try:
    for block,pio in enumerate(pios):
        assert uctypes.addressof(pio.SM[1])-uctypes.addressof(pio.SM[0])==24
        assert uctypes.addressof(pio.IRQ[1])-uctypes.addressof(pio.IRQ[0])==12
        for index in range(4):
            sm=rp2.StateMachine(block*4+index,idle,freq=(index+1)*1000000)
            sm.active(0);machines.append(sm)
            register=machine.mem32[0x502000c8+block*0x100000+index*24]
            assert pio.SM[index].CLKDIV.INT==register>>16
            assert pio.SM[index].CLKDIV.FRAC==(register>>8)&255
            sm.exec(31)  # Encoded absolute JMP; asm_pio_encode has no labels here.
            assert pio.SM[index].ADDR==31,pio.SM[index].ADDR
            assert isinstance(pio.SM[index].INSTR,int)
        pio.IRQ_FORCE=1
        assert pio.IRQ_FLAGS & 1,pio.IRQ_FLAGS
        machine.mem32[0x50200030+block*0x100000]=1
        assert not pio.IRQ_FLAGS & 1
    assert bindings.DREQ_ADC==(48 if RP2350 else 36)
    if RP2350:
        assert bindings.DREQ_PIO2_TX0==16 and bindings.DREQ_PIO2_RX3==23
    print(json.dumps({'chip':'RP2350' if RP2350 else 'RP2040','pio_blocks':len(pios),
                      'sm_stride':uctypes.sizeof(SM_FIELDS),'tested_state_machines':len(machines),
                      'five_bit_pc':True,'clock_hz':machine.freq(),'dma_requests':True}))
finally:
    for sm in machines:sm.active(0)
    for block in range(len(pios)):rp2.PIO(block).remove_program(idle)
