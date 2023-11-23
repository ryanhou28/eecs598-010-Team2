import pylse

def adder(A_0__p, A_0__n, A_1__p, A_1__n, A_2__p, A_2__n, A_3__p, A_3__n, A_4__p, A_4__n, A_5__p, A_5__n, A_6__p, A_6__n, A_7__p, A_7__n, B_0__p, B_0__n, B_1__p, B_1__n, B_2__p, B_2__n, B_3__p, B_3__n, B_4__p, B_4__n, B_5__p, B_5__n, B_6__p, B_6__n, B_7__p, B_7__n):

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

    A_6__p_spl_ = pylse.split(A_6__p, n=2, firing_delay=4.3)
    B_6__p_spl_ = pylse.split(B_6__p, n=2, firing_delay=4.3)
    A_6__n_spl_ = pylse.split(A_6__n, n=2, firing_delay=4.3)
    B_6__n_spl_ = pylse.split(B_6__n, n=2, firing_delay=4.3)
    A_5__p_spl_ = pylse.split(A_5__p, n=2, firing_delay=4.3)
    B_5__p_spl_ = pylse.split(B_5__p, n=2, firing_delay=4.3)
    A_5__n_spl_ = pylse.split(A_5__n, n=2, firing_delay=4.3)
    B_5__n_spl_ = pylse.split(B_5__n, n=2, firing_delay=4.3)
    A_4__p_spl_ = pylse.split(A_4__p, n=2, firing_delay=4.3)
    B_4__p_spl_ = pylse.split(B_4__p, n=2, firing_delay=4.3)
    A_4__n_spl_ = pylse.split(A_4__n, n=2, firing_delay=4.3)
    B_4__n_spl_ = pylse.split(B_4__n, n=2, firing_delay=4.3)
    A_3__p_spl_ = pylse.split(A_3__p, n=2, firing_delay=4.3)
    B_3__p_spl_ = pylse.split(B_3__p, n=2, firing_delay=4.3)
    A_3__n_spl_ = pylse.split(A_3__n, n=2, firing_delay=4.3)
    B_3__n_spl_ = pylse.split(B_3__n, n=2, firing_delay=4.3)
    A_2__p_spl_ = pylse.split(A_2__p, n=2, firing_delay=4.3)
    B_2__p_spl_ = pylse.split(B_2__p, n=2, firing_delay=4.3)
    A_2__n_spl_ = pylse.split(A_2__n, n=2, firing_delay=4.3)
    B_2__n_spl_ = pylse.split(B_2__n, n=2, firing_delay=4.3)
    A_1__p_spl_ = pylse.split(A_1__p, n=2, firing_delay=4.3)
    B_1__p_spl_ = pylse.split(B_1__p, n=2, firing_delay=4.3)
    A_1__n_spl_ = pylse.split(A_1__n, n=2, firing_delay=4.3)
    B_1__n_spl_ = pylse.split(B_1__n, n=2, firing_delay=4.3)
    A_0__p_spl_ = pylse.split(A_0__p, n=2, firing_delay=4.3)
    B_0__p_spl_ = pylse.split(B_0__p, n=2, firing_delay=4.3)
    A_7__n_spl_ = pylse.split(A_7__n, n=2, firing_delay=4.3)
    B_7__n_spl_ = pylse.split(B_7__n, n=2, firing_delay=4.3)

    g17_p = la(A_6__p_spl_[0], B_6__p_spl_[0])
    g17_p_spl_ = pylse.split(g17_p, n=2, firing_delay=4.3)
    g17_n = fa(A_6__n_spl_[0], B_6__n_spl_[0])
    g18_p = la(A_5__p_spl_[0], B_5__p_spl_[0])
    g18_p_spl_ = pylse.split(g18_p, n=2, firing_delay=4.3)
    g18_n = fa(A_5__n_spl_[0], B_5__n_spl_[0])
    g18_n_spl_ = pylse.split(g18_n, n=2, firing_delay=4.3)
    g19_p = la(A_4__p_spl_[0], B_4__p_spl_[0])
    g19_p_spl_ = pylse.split(g19_p, n=2, firing_delay=4.3)
    g19_n = fa(A_4__n_spl_[0], B_4__n_spl_[0])
    g19_n_spl_ = pylse.split(g19_n, n=2, firing_delay=4.3)
    g20_p = la(A_4__n_spl_[1], B_4__n_spl_[1])
    g20_n = fa(A_4__p_spl_[1], B_4__p_spl_[1])
    g21_p = la(g19_n_spl_[0], g20_n)
    g21_p_spl_ = pylse.split(g21_p, n=2, firing_delay=4.3)
    g21_n = fa(g19_p_spl_[0], g20_p)
    g22_p = la(A_3__p_spl_[0], B_3__p_spl_[0])
    g22_p_spl_ = pylse.split(g22_p, n=2, firing_delay=4.3)
    g22_n = fa(A_3__n_spl_[0], B_3__n_spl_[0])
    g22_n_spl_ = pylse.split(g22_n, n=2, firing_delay=4.3)
    g23_p = la(A_3__n_spl_[1], B_3__n_spl_[1])
    g23_p_spl_ = pylse.split(g23_p, n=2, firing_delay=4.3)
    g23_n = fa(A_3__p_spl_[1], B_3__p_spl_[1])
    g23_n_spl_ = pylse.split(g23_n, n=2, firing_delay=4.3)
    g24_p = la(A_2__p_spl_[0], B_2__p_spl_[0])
    g24_p_spl_ = pylse.split(g24_p, n=2, firing_delay=4.3)
    g24_n = fa(A_2__n_spl_[0], B_2__n_spl_[0])
    g24_n_spl_ = pylse.split(g24_n, n=2, firing_delay=4.3)
    g25_p = la(A_2__n_spl_[1], B_2__n_spl_[1])
    g25_p_spl_ = pylse.split(g25_p, n=2, firing_delay=4.3)
    g25_n = fa(A_2__p_spl_[1], B_2__p_spl_[1])
    g25_n_spl_ = pylse.split(g25_n, n=2, firing_delay=4.3)
    g26_p = la(A_1__p_spl_[0], B_1__p_spl_[0])
    g26_p_spl_ = pylse.split(g26_p, n=2, firing_delay=4.3)
    g26_n = fa(A_1__n_spl_[0], B_1__n_spl_[0])
    g26_n_spl_ = pylse.split(g26_n, n=2, firing_delay=4.3)
    g27_p = la(A_1__n_spl_[1], B_1__n_spl_[1])
    g27_p_spl_ = pylse.split(g27_p, n=2, firing_delay=4.3)
    g27_n = fa(A_1__p_spl_[1], B_1__p_spl_[1])
    g27_n_spl_ = pylse.split(g27_n, n=2, firing_delay=4.3)
    g28_p = la(A_0__p_spl_[0], B_0__p_spl_[0])
    g28_p_spl_ = pylse.split(g28_p, n=2, firing_delay=4.3)
    g28_n = fa(A_0__n, B_0__n)
    g28_n_spl_ = pylse.split(g28_n, n=3, firing_delay=4.3)
    g29_p = la(g27_n_spl_[0], g28_p_spl_[0])
    g29_n = fa(g27_p_spl_[0], g28_n_spl_[0])
    g30_p = la(g26_n_spl_[0], g29_n)
    g30_p_spl_ = pylse.split(g30_p, n=2, firing_delay=4.3)
    g30_n = fa(g26_p_spl_[0], g29_p)
    g30_n_spl_ = pylse.split(g30_n, n=2, firing_delay=4.3)
    g31_p = la(g25_n_spl_[0], g30_n_spl_[0])
    g31_n = fa(g25_p_spl_[0], g30_p_spl_[0])
    g32_p = la(g24_n_spl_[0], g31_n)
    g32_p_spl_ = pylse.split(g32_p, n=2, firing_delay=4.3)
    g32_n = fa(g24_p_spl_[0], g31_p)
    g32_n_spl_ = pylse.split(g32_n, n=2, firing_delay=4.3)
    g33_p = la(g23_n_spl_[0], g32_n_spl_[0])
    g33_n = fa(g23_p_spl_[0], g32_p_spl_[0])
    g34_p = la(g22_n_spl_[0], g33_n)
    g34_n = fa(g22_p_spl_[0], g33_p)
    g34_n_spl_ = pylse.split(g34_n, n=2, firing_delay=4.3)
    g35_p = la(g21_p_spl_[0], g34_n_spl_[0])
    g35_n = fa(g21_n, g34_p)
    g35_n_spl_ = pylse.split(g35_n, n=2, firing_delay=4.3)
    g36_p = la(g19_n_spl_[1], g35_n_spl_[0])
    g36_n = fa(g19_p_spl_[1], g35_p)
    g36_n_spl_ = pylse.split(g36_n, n=2, firing_delay=4.3)
    g37_p = la(A_5__n_spl_[1], B_5__n_spl_[1])
    g37_n = fa(A_5__p_spl_[1], B_5__p_spl_[1])
    g38_p = la(g18_n_spl_[0], g37_n)
    g38_p_spl_ = pylse.split(g38_p, n=2, firing_delay=4.3)
    g38_n = fa(g18_p_spl_[0], g37_p)
    g39_p = la(g36_n_spl_[0], g38_p_spl_[0])
    g39_n = fa(g36_p, g38_n)
    g39_n_spl_ = pylse.split(g39_n, n=2, firing_delay=4.3)
    g40_p = la(g18_n_spl_[1], g39_n_spl_[0])
    g40_n = fa(g18_p_spl_[1], g39_p)
    g40_n_spl_ = pylse.split(g40_n, n=2, firing_delay=4.3)
    g41_p = la(A_6__n_spl_[1], B_6__n_spl_[1])
    g41_n = fa(A_6__p_spl_[1], B_6__p_spl_[1])
    g42_p = la(g17_n, g41_n)
    g42_p_spl_ = pylse.split(g42_p, n=2, firing_delay=4.3)
    g42_n = fa(g17_p_spl_[0], g41_p)
    g43_p = la(g40_n_spl_[0], g42_p_spl_[0])
    g43_n = fa(g40_p, g42_n)
    g44_n = fa(g17_p_spl_[1], g43_p)
    g44_n_spl_ = pylse.split(g44_n, n=3, firing_delay=4.3)
    g45_p = la(A_7__n_spl_[0], B_7__n_spl_[0])
    g45_p_spl_ = pylse.split(g45_p, n=2, firing_delay=4.3)
    g46_p = la(g44_n_spl_[0], g45_p_spl_[0])
    g46_p_spl_ = pylse.split(g46_p, n=7, firing_delay=4.3)
    g47_n = fa(A_7__n_spl_[1], B_7__n_spl_[1])
    g47_n_spl_ = pylse.split(g47_n, n=2, firing_delay=4.3)
    g48_n = fa(g44_n_spl_[1], g47_n_spl_[0])
    g48_n_spl_ = pylse.split(g48_n, n=7, firing_delay=4.3)
    g49_n = fa(A_0__p_spl_[1], B_0__p_spl_[1])
    g50_p = la(g28_n_spl_[1], g49_n)
    g51_p = la(g48_n_spl_[0], g50_p)
    g52_n = fa(g46_p_spl_[0], g51_p)
    g53_p = la(g26_n_spl_[1], g27_n_spl_[1])
    g53_n = fa(g26_p_spl_[1], g27_p_spl_[1])
    g54_n = fa(g28_n_spl_[2], g53_n)
    g55_n = fa(g28_p_spl_[1], g53_p)
    g56_p = la(g54_n, g55_n)
    g57_p = la(g48_n_spl_[1], g56_p)
    g58_n = fa(g46_p_spl_[1], g57_p)
    g59_p = la(g24_n_spl_[1], g25_n_spl_[1])
    g59_n = fa(g24_p_spl_[1], g25_p_spl_[1])
    g60_p = la(g30_p_spl_[1], g59_p)
    g61_p = la(g30_n_spl_[1], g59_n)
    g62_n = fa(g60_p, g61_p)
    g63_p = la(g48_n_spl_[2], g62_n)
    g64_n = fa(g46_p_spl_[2], g63_p)
    g65_p = la(g22_n_spl_[1], g23_n_spl_[1])
    g65_n = fa(g22_p_spl_[1], g23_p_spl_[1])
    g66_n = fa(g32_p_spl_[1], g65_n)
    g67_n = fa(g32_n_spl_[1], g65_p)
    g68_p = la(g66_n, g67_n)
    g69_p = la(g48_n_spl_[3], g68_p)
    g70_n = fa(g46_p_spl_[3], g69_p)
    g71_n = fa(g21_p_spl_[1], g34_n_spl_[1])
    g72_p = la(g35_n_spl_[1], g71_n)
    g73_p = la(g48_n_spl_[4], g72_p)
    g74_n = fa(g46_p_spl_[4], g73_p)
    g75_n = fa(g36_n_spl_[1], g38_p_spl_[1])
    g76_p = la(g39_n_spl_[1], g75_n)
    g77_p = la(g48_n_spl_[5], g76_p)
    g78_n = fa(g46_p_spl_[5], g77_p)
    g79_n = fa(g40_n_spl_[1], g42_p_spl_[1])
    g80_p = la(g43_n, g79_n)
    g81_p = la(g48_n_spl_[6], g80_p)
    g82_n = fa(g46_p_spl_[6], g81_p)
    g83_n = fa(g44_n_spl_[2], g45_p_spl_[1])
    g84_p = la(g47_n_spl_[1], g83_n)
    SUM_0_ = g52_n
    SUM_1_ = g58_n
    SUM_2_ = g64_n
    SUM_3_ = g70_n
    SUM_4_ = g74_n
    SUM_5_ = g78_n
    SUM_6_ = g82_n
    SUM_7_ = g84_p


    return SUM_0_, SUM_1_, SUM_2_, SUM_3_, SUM_4_, SUM_5_, SUM_6_, SUM_7_

def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def test_single_input(A_0_, A_1_, A_2_, A_3_, A_4_, A_5_, A_6_, A_7_, B_0_, B_1_, B_2_, B_3_, B_4_, B_5_, B_6_, B_7_):
    print("Inputs:")
    print("A_0_ A_1_ A_2_ A_3_ A_4_ A_5_ A_6_ A_7_ B_0_ B_1_ B_2_ B_3_ B_4_ B_5_ B_6_ B_7_")
    print(A_0_, A_1_, A_2_, A_3_, A_4_, A_5_, A_6_, A_7_, B_0_, B_1_, B_2_, B_3_, B_4_, B_5_, B_6_, B_7_)
    A_0__p_t = inv(A_0_)
    A_0__n_t = A_0_
    A_1__p_t = inv(A_1_)
    A_1__n_t = A_1_
    A_2__p_t = inv(A_2_)
    A_2__n_t = A_2_
    A_3__p_t = inv(A_3_)
    A_3__n_t = A_3_
    A_4__p_t = inv(A_4_)
    A_4__n_t = A_4_
    A_5__p_t = inv(A_5_)
    A_5__n_t = A_5_
    A_6__p_t = inv(A_6_)
    A_6__n_t = A_6_
    A_7__p_t = inv(A_7_)
    A_7__n_t = A_7_
    B_0__p_t = inv(B_0_)
    B_0__n_t = B_0_
    B_1__p_t = inv(B_1_)
    B_1__n_t = B_1_
    B_2__p_t = inv(B_2_)
    B_2__n_t = B_2_
    B_3__p_t = inv(B_3_)
    B_3__n_t = B_3_
    B_4__p_t = inv(B_4_)
    B_4__n_t = B_4_
    B_5__p_t = inv(B_5_)
    B_5__n_t = B_5_
    B_6__p_t = inv(B_6_)
    B_6__n_t = B_6_
    B_7__p_t = inv(B_7_)
    B_7__n_t = B_7_

    A_0__p = pylse.inp_at(A_0__p_t*T, name='A_0__p')
    A_0__n = pylse.inp_at(A_0__n_t*T, name='A_0__n')
    A_1__p = pylse.inp_at(A_1__p_t*T, name='A_1__p')
    A_1__n = pylse.inp_at(A_1__n_t*T, name='A_1__n')
    A_2__p = pylse.inp_at(A_2__p_t*T, name='A_2__p')
    A_2__n = pylse.inp_at(A_2__n_t*T, name='A_2__n')
    A_3__p = pylse.inp_at(A_3__p_t*T, name='A_3__p')
    A_3__n = pylse.inp_at(A_3__n_t*T, name='A_3__n')
    A_4__p = pylse.inp_at(A_4__p_t*T, name='A_4__p')
    A_4__n = pylse.inp_at(A_4__n_t*T, name='A_4__n')
    A_5__p = pylse.inp_at(A_5__p_t*T, name='A_5__p')
    A_5__n = pylse.inp_at(A_5__n_t*T, name='A_5__n')
    A_6__p = pylse.inp_at(A_6__p_t*T, name='A_6__p')
    A_6__n = pylse.inp_at(A_6__n_t*T, name='A_6__n')
    A_7__p = pylse.inp_at(A_7__p_t*T, name='A_7__p')
    A_7__n = pylse.inp_at(A_7__n_t*T, name='A_7__n')
    B_0__p = pylse.inp_at(B_0__p_t*T, name='B_0__p')
    B_0__n = pylse.inp_at(B_0__n_t*T, name='B_0__n')
    B_1__p = pylse.inp_at(B_1__p_t*T, name='B_1__p')
    B_1__n = pylse.inp_at(B_1__n_t*T, name='B_1__n')
    B_2__p = pylse.inp_at(B_2__p_t*T, name='B_2__p')
    B_2__n = pylse.inp_at(B_2__n_t*T, name='B_2__n')
    B_3__p = pylse.inp_at(B_3__p_t*T, name='B_3__p')
    B_3__n = pylse.inp_at(B_3__n_t*T, name='B_3__n')
    B_4__p = pylse.inp_at(B_4__p_t*T, name='B_4__p')
    B_4__n = pylse.inp_at(B_4__n_t*T, name='B_4__n')
    B_5__p = pylse.inp_at(B_5__p_t*T, name='B_5__p')
    B_5__n = pylse.inp_at(B_5__n_t*T, name='B_5__n')
    B_6__p = pylse.inp_at(B_6__p_t*T, name='B_6__p')
    B_6__n = pylse.inp_at(B_6__n_t*T, name='B_6__n')
    B_7__p = pylse.inp_at(B_7__p_t*T, name='B_7__p')
    B_7__n = pylse.inp_at(B_7__n_t*T, name='B_7__n')

    return A_0__p, A_0__n, A_1__p, A_1__n, A_2__p, A_2__n, A_3__p, A_3__n, A_4__p, A_4__n, A_5__p, A_5__n, A_6__p, A_6__n, A_7__p, A_7__n, B_0__p, B_0__n, B_1__p, B_1__n, B_2__p, B_2__n, B_3__p, B_3__n, B_4__p, B_4__n, B_5__p, B_5__n, B_6__p, B_6__n, B_7__p, B_7__n

def check_events(events, T):
    print("Output Events:")
    print("SUM_0_ SUM_1_ SUM_2_ SUM_3_ SUM_4_ SUM_5_ SUM_6_ SUM_7_")
    sums = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        sums[i] = int(events['SUM_' + str(i) + '_'][0] < T)
    # sums[0] = inv(sums[0])
    # sums[1] = inv(sums[1])
    # sums[2] = inv(sums[2])
    # sums[3] = inv(sums[3])
    # sums[4] = inv(sums[4])
    # sums[5] = inv(sums[5])
    # sums[6] = inv(sums[6])
    sums[7] = inv(sums[7])
    print("Binary Results (output flip accounted for):")
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
    T = 200  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=4, name='clk')
    num1 = -123
    num2 = 126
    num1bin = twos_complement_bin(num1)
    num2bin = twos_complement_bin(num2)
    A_0__p, A_0__n, A_1__p, A_1__n, A_2__p, A_2__n, A_3__p, A_3__n, A_4__p, A_4__n, A_5__p, A_5__n, A_6__p, A_6__n, A_7__p, A_7__n, B_0__p, B_0__n, B_1__p, B_1__n, B_2__p, B_2__n, B_3__p, B_3__n, B_4__p, B_4__n, B_5__p, B_5__n, B_6__p, B_6__n, B_7__p, B_7__n= test_single_input(num1bin[0], num1bin[1], num1bin[2], num1bin[3], num1bin[4], num1bin[5], num1bin[6], num1bin[7], num2bin[0], num2bin[1], num2bin[2], num2bin[3], num2bin[4], num2bin[5], num2bin[6], num2bin[7])
    print("Input Numbers (binary array is LSB -> MSB):")
    print(num1,"=", num1bin)
    print(num2,"=", num2bin)
    # Instantiate the module
    SUM_0_, SUM_1_, SUM_2_, SUM_3_, SUM_4_, SUM_5_, SUM_6_, SUM_7_= adder(A_0__p, A_0__n, A_1__p, A_1__n, A_2__p, A_2__n, A_3__p, A_3__n, A_4__p, A_4__n, A_5__p, A_5__n, A_6__p, A_6__n, A_7__p, A_7__n, B_0__p, B_0__n, B_1__p, B_1__n, B_2__p, B_2__n, B_3__p, B_3__n, B_4__p, B_4__n, B_5__p, B_5__n, B_6__p, B_6__n, B_7__p, B_7__n)

    # Probe outputs
    pylse.inspect(SUM_0_, 'SUM_0_')
    pylse.inspect(SUM_1_, 'SUM_1_')
    pylse.inspect(SUM_2_, 'SUM_2_')
    pylse.inspect(SUM_3_, 'SUM_3_')
    pylse.inspect(SUM_4_, 'SUM_4_')
    pylse.inspect(SUM_5_, 'SUM_5_')
    pylse.inspect(SUM_6_, 'SUM_6_')
    pylse.inspect(SUM_7_, 'SUM_7_')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()


    # Print out the events
    check_events(events, T)
