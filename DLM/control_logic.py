import pylse
from more_cells import dro2r,dro,s,m
def control_logic(read_address,read_address_,write_address,write_address_,loop_data_out,write_data):
    write_address_2r,write_address_dro = s(write_address, jjs = 0, firing_delay = 0)
    dro_out = dro(write_data,write_address_dro, firing_delay = 7)
    dro2r_out0, _ = dro2r(loop_data_out, write_address_, write_address_2r, firing_delay = 5.8)
    m_out = m(dro2r_out0,dro_out, firing_delay=5.9, transition_time = 5.9)
    # here the code is not so clear
    # the firing_delay is used as transition_time
    # however to override transition_time, provide firing_delay alone is not enough
    loop_data_in_2r, loop_data_in = s(m_out, jjs = 0, firing_delay = 0)
    read_data, _ = dro2r(read_address, loop_data_in_2r, read_address_,firing_delay = 5.8)
    return read_data, loop_data_in


def control_logic_george(read_address,read_address_,write_address,write_address_,loop_data_out,write_data,**kwargs):
    T_DRO_hold = 7
    T_DRO2R_hold = 5.8
    T_M_hold = 5.9
    if 'T_DRO_hold' in kwargs:
        T_DRO_hold = kwargs['T_DRO_hold']
    if 'T_DRO2R_hold' in kwargs:
        T_DRO2R_hold = kwargs['T_DRO2R_hold']
    if 'T_M_hold' in kwargs:
        T_M_hold = kwargs['T_M_hold']                
    write_address_2r,write_address_dro = s(write_address, jjs = 0, firing_delay = 0)
    loop_data_out_cir,loop_data_out_read = s(loop_data_out, jjs = 0, firing_delay = 0)
    dro_out = dro(write_data,write_address_dro, firing_delay = 7, transition_time = T_DRO_hold)
    dro2r_out0, _ = dro2r(loop_data_out_cir, write_address_, write_address_2r, firing_delay = 5.8, transition_time = T_DRO2R_hold)
    loop_data_in = m(dro2r_out0,dro_out, firing_delay=5.9, transition_time = T_M_hold)
    read_data, _ = dro2r(loop_data_out_read,read_address, read_address_,firing_delay = 5.8, transition_time = T_DRO2R_hold)
    return read_data, loop_data_in



# read_address,read_address_,write_address,write_address_,loop_data_out,write_data = pylse.inp_at(200,500,name='read_address'),\
#     pylse.inp_at(100,300,400,600,name='read_address_'),\
#     pylse.inp_at(200,name='write_address'),\
#     pylse.inp_at(100,300,400,505,600,name='write_address_'),\
#     pylse.inp_at(500,name='loop_data_out'),\
#     pylse.inp_at(0,name='write_data')

# # write_address_2r,write_address_dro = pylse.s(write_address)
# # dro_out = pylse.dro(write_data,write_address_dro)
# # dro2r_out0, _ = dro2r(loop_data_out, write_address_, write_address_2r)
# # m_out = pylse.m(dro2r_out0,dro_out)
# # loop_data_in_2r, loop_data_in = pylse.s(m_out)
# # read_data, _ = dro2r(read_address, loop_data_in_2r, read_address_)

# read_data, loop_data_in = control_logic(read_address,read_address_,write_address,write_address_,loop_data_out,write_data)

# pylse.inspect(read_data,'read_data')
# pylse.inspect(loop_data_in,'loop_data_in')

# # First create a simulation object...
# sim = pylse.Simulation()
# # ...then simulate...
# events = sim.simulate()
# # ...and finally plot it!
# sim.plot(wires_to_display=['read_address', 'write_address', 'loop_data_out', 'write_data', 'read_data', 'loop_data_in'])


