import pylse
from control_logic import control_logic_george
from more_cells import *
import random
from parameter import *

def delay_line_memory(read_address,read_address_,write_address,write_address_,write_data,**kargs):
    # clk is only used for finer display without any actual functionality
    loop_data_out = pylse.Wire()
    read_data, loop_data_in = control_logic_george(read_address,read_address_,write_address,write_address_,loop_data_out,write_data, **kargs)
    ptl(loop_data_in,loop_data_out, firing_delay = T_PTL_prop)
    return read_data, loop_data_out  

read_address,read_address_,write_address,write_address_,write_data = \
    pylse.inp_at(10+t_read_offset,20+t_read_offset,30+t_read_offset,50+t_read_offset, 60+t_write_offset, 90+t_read_offset, 100+t_read_offset, 110+t_read_offset, name='read_address'),\
    pylse.inp_at(t_read_offset,40+t_read_offset,70+t_read_offset, 80+t_read_offset, name='read_address_'),\
    pylse.inp_at(10+t_write_offset,60+t_write_offset, 70+t_write_offset, 90+t_write_offset,name='write_address'),\
    pylse.inp_at(t_write_offset,30+t_write_offset,20+t_write_offset,40+t_write_offset,50+t_write_offset,80+t_write_offset, 100+t_write_offset,110+t_write_offset, name='write_address_'),\
    pylse.inp_at(t_write_offset,80+t_write_offset,name='write_data')

clk = pylse.inp_at(*(i*10 for i in range(1, 13)), name='clk')
read_data,loop_data_out = delay_line_memory(read_address,read_address_,write_address,write_address_,write_data,T_DRO2R_hold=T_DRO2R_hold,T_DRO_hold=T_DRO_hold,T_M_hold=T_M_hold)

pylse.inspect(read_data,'read_data')
pylse.inspect(loop_data_out,'loop_data_out')
# First create a simulation object...
sim = pylse.Simulation()
# ...then simulate...
events = sim.simulate()
# ...and finally plot it!
#sim.plot(wires_to_display=['read_address', 'write_address', 'write_data', 'read_data'])
sim.plot()
print("success")
