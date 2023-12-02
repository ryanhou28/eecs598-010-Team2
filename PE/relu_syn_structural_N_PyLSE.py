import pylse

def relu(input_f_0__p, input_f_0__n, input_f_1__p, input_f_1__n, input_f_2__p, input_f_2__n, input_f_3__p, input_f_3__n, input_f_4__p, input_f_4__n, input_f_5__p, input_f_5__n, input_f_6__p, input_f_6__n, input_f_7__p, input_f_7__n):

    # Define helpers to ensure same delay numbers (currently the same as PyLSE example)
    def jtl(*args):
        return pylse.jtl(*args, firing_delay=5.7)

    def fa(x, y):
        """ First-arrival cell based on an inverted C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c_inv(jtl(x), jtl(y), firing_delay=9.0)

    def la(x, y):
        """ Last-arrival cell based on a C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c(jtl(x), jtl(y), firing_delay=8.0)

    def s(x):
        return pylse.s(x, firing_delay=4.3)

    def dro(*args):
        return pylse.dro(*args, firing_delay=5.1)

    input_f_7__n_spl_ = pylse.split(input_f_7__n, n=7, firing_delay=4.3)

    output_f_0_ = la(input_f_0__p, input_f_7__n_spl_[0])
    output_f_1_ = la(input_f_1__p, input_f_7__n_spl_[1])
    output_f_2_ = la(input_f_2__p, input_f_7__n_spl_[2])
    output_f_3_ = la(input_f_3__p, input_f_7__n_spl_[3])
    output_f_4_ = la(input_f_4__p, input_f_7__n_spl_[4])
    output_f_5_ = la(input_f_5__p, input_f_7__n_spl_[5])
    output_f_6_ = la(input_f_6__p, input_f_7__n_spl_[6])
    output_f_7_ = pylse.Wire() # Connected to ground, always 0

    return output_f_0_, output_f_1_, output_f_2_, output_f_3_, output_f_4_, output_f_5_, output_f_6_, output_f_7_

def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def test_single_input(input_f_0_, input_f_1_, input_f_2_, input_f_3_, input_f_4_, input_f_5_, input_f_6_, input_f_7_):
    print("Inputs:")
    print("input_f_0_ input_f_1_ input_f_2_ input_f_3_ input_f_4_ input_f_5_ input_f_6_ input_f_7_")
    print(input_f_0_, input_f_1_, input_f_2_, input_f_3_, input_f_4_, input_f_5_, input_f_6_, input_f_7_)
    input_f_0__p_t = inv(input_f_0_)
    input_f_0__n_t = input_f_0_
    input_f_1__p_t = inv(input_f_1_)
    input_f_1__n_t = input_f_1_
    input_f_2__p_t = inv(input_f_2_)
    input_f_2__n_t = input_f_2_
    input_f_3__p_t = inv(input_f_3_)
    input_f_3__n_t = input_f_3_
    input_f_4__p_t = inv(input_f_4_)
    input_f_4__n_t = input_f_4_
    input_f_5__p_t = inv(input_f_5_)
    input_f_5__n_t = input_f_5_
    input_f_6__p_t = inv(input_f_6_)
    input_f_6__n_t = input_f_6_
    input_f_7__p_t = inv(input_f_7_)
    input_f_7__n_t = input_f_7_

    input_f_0__p = pylse.inp_at(input_f_0__p_t*T, name='input_f_0__p')
    input_f_0__n = pylse.inp_at(input_f_0__n_t*T, name='input_f_0__n')
    input_f_1__p = pylse.inp_at(input_f_1__p_t*T, name='input_f_1__p')
    input_f_1__n = pylse.inp_at(input_f_1__n_t*T, name='input_f_1__n')
    input_f_2__p = pylse.inp_at(input_f_2__p_t*T, name='input_f_2__p')
    input_f_2__n = pylse.inp_at(input_f_2__n_t*T, name='input_f_2__n')
    input_f_3__p = pylse.inp_at(input_f_3__p_t*T, name='input_f_3__p')
    input_f_3__n = pylse.inp_at(input_f_3__n_t*T, name='input_f_3__n')
    input_f_4__p = pylse.inp_at(input_f_4__p_t*T, name='input_f_4__p')
    input_f_4__n = pylse.inp_at(input_f_4__n_t*T, name='input_f_4__n')
    input_f_5__p = pylse.inp_at(input_f_5__p_t*T, name='input_f_5__p')
    input_f_5__n = pylse.inp_at(input_f_5__n_t*T, name='input_f_5__n')
    input_f_6__p = pylse.inp_at(input_f_6__p_t*T, name='input_f_6__p')
    input_f_6__n = pylse.inp_at(input_f_6__n_t*T, name='input_f_6__n')
    input_f_7__p = pylse.inp_at(input_f_7__p_t*T, name='input_f_7__p')
    input_f_7__n = pylse.inp_at(input_f_7__n_t*T, name='input_f_7__n')

    return input_f_0__p, input_f_0__n, input_f_1__p, input_f_1__n, input_f_2__p, input_f_2__n, input_f_3__p, input_f_3__n, input_f_4__p, input_f_4__n, input_f_5__p, input_f_5__n, input_f_6__p, input_f_6__n, input_f_7__p, input_f_7__n

def check_events(events, T):
    print("Output Events:")
    print("out_0_ out_1_ out_2_ out_3_ out_4_ out_5_ out_6_ out_7_")
    sums = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        try:
            sums[i] = int(events['output_f_' + str(i) + '_'][0] < T)
        except:
            sums[i] = 0
    
    print("Binary Results:")
    print(sums)
    # print(int(events['SUM_0_'][0] < T), int(events['SUM_1_'][0] < T), int(events['SUM_2_'][0] < T), int(events['SUM_3_'][0] < T), int(events['SUM_4_'][0] < T), int(events['SUM_5_'][0] < T), int(events['SUM_6_'][0] < T), int(events['SUM_7_'][0] < T))
    print("Decimal Results:")
    print(twos_to_dec(sums))

def twos_to_dec(binary_array):
    # Convert a binary array of bits of the 8-bit twos complement to a decimal number
    if not binary_array:
        return 0

    # Check if the number is negative (MSB is 1)
    is_negative = binary_array[-1] == 1

    if is_negative:
        # Invert the bits
        inverted_array = [1 - bit for bit in binary_array]

        # Add 1 to the inverted array
        carry = 1
        for i in range(len(inverted_array)):
            inverted_array[i] += carry
            if inverted_array[i] == 2:
                inverted_array[i] = 0
                carry = 1
            else:
                carry = 0

        # Convert to number and negate
        number = -sum(bit * (2 ** i) for i, bit in enumerate(inverted_array))
    else:
        # Convert to number directly
        number = sum(bit * (2 ** i) for i, bit in enumerate(binary_array))

    return number

def twos_complement_bin(num):
    # Generate a binary array of bits of the 8-bit twos complement of the number
    # Saturate the bit array if the number is out of range
    if num < -128:
        num = -128
    elif num > 127:
        num = 127

    if num < 0:
        num = 256 + num

    bin_str = bin(num)[2:].zfill(8)

    binarr = [int(x) for x in bin_str]

    # Flip the binarr so that the LSB is at the beginning
    binarr.reverse()

    return binarr

if __name__ == "__main__":
    # Create clock signal
    T = 400  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=4, name='clk')

    num1 = -121
    num1bin = twos_complement_bin(num1)
    input_f_0__p, input_f_0__n, input_f_1__p, input_f_1__n, input_f_2__p, input_f_2__n, input_f_3__p, input_f_3__n, input_f_4__p, input_f_4__n, input_f_5__p, input_f_5__n, input_f_6__p, input_f_6__n, input_f_7__p, input_f_7__n= test_single_input(num1bin[0], num1bin[1], num1bin[2], num1bin[3], num1bin[4], num1bin[5], num1bin[6], num1bin[7])
    print("Input num:", num1)
    print("Input binary:", num1bin)

    # Instantiate the module
    output_f_0_, output_f_1_, output_f_2_, output_f_3_, output_f_4_, output_f_5_, output_f_6_, output_f_7_= relu(input_f_0__p, input_f_0__n, input_f_1__p, input_f_1__n, input_f_2__p, input_f_2__n, input_f_3__p, input_f_3__n, input_f_4__p, input_f_4__n, input_f_5__p, input_f_5__n, input_f_6__p, input_f_6__n, input_f_7__p, input_f_7__n)

    # Probe outputs
    pylse.inspect(output_f_0_, 'output_f_0_')
    pylse.inspect(output_f_1_, 'output_f_1_')
    pylse.inspect(output_f_2_, 'output_f_2_')
    pylse.inspect(output_f_3_, 'output_f_3_')
    pylse.inspect(output_f_4_, 'output_f_4_')
    pylse.inspect(output_f_5_, 'output_f_5_')
    pylse.inspect(output_f_6_, 'output_f_6_')
    pylse.inspect(output_f_7_, 'output_f_7_')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Print out the events
    check_events(events, T)
