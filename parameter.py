T = 10
num_addr = 3
T_DRO2R_prop = 5.8
T_DRO2R_hold = 5.8 
T_DRO2R_setup = 2
T_DRO_prop = 7
T_DRO_hold = 7
T_DRO_setup = 2
T_M_prop = 5.9
T_M_hold = 5.9
t_read_offset = 0
t_write_offset = 0
T_PTL_upper = (num_addr+1)*T-T_DRO2R_setup-T_DRO_prop-T_M_prop
T_PTL_lower = num_addr*T-T_M_prop + T_DRO2R_hold - T_DRO2R_prop
noise = (T_PTL_upper - T_PTL_lower)/\
		(T_DRO_prop+T_M_prop+T_PTL_upper + T_DRO2R_prop + T_M_prop + T_PTL_lower)
noise_M = (T+T_DRO2R_prop-T_M_hold-T_DRO_prop)/(T_DRO2R_prop+T_DRO_prop)
# temporarily set T_M_prop = T_M_hold but it is not always the case
noise = min(noise,noise_M)
T_PTL_prop=(T_PTL_lower+T_PTL_upper+(-T_DRO_prop-T_M_prop-T_PTL_upper + T_DRO2R_prop+T_M_prop+T_PTL_lower)*noise)/2
print(T_PTL_prop)
print(noise)

