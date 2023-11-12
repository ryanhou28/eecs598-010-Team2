import pylse

def mymod(A_0__p, A_0__n, A_1__p, A_1__n, A_2__p, A_2__n, A_3__p, A_3__n, A_4__p, A_4__n, A_5__p, A_5__n, A_6__p, A_6__n, A_7__p, A_7__n, B_0__p, B_0__n, B_1__p, B_1__n, B_2__p, B_2__n, B_3__p, B_3__n, B_4__p, B_4__n, B_5__p, B_5__n, B_6__p, B_6__n, B_7__p, B_7__n):

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

    A_7__p_spl_ = pylse.split(A_7__p, n=2, firing_delay=4.3)
    B_7__n_spl_ = pylse.split(B_7__n, n=3, firing_delay=4.3)
    A_7__n_spl_ = pylse.split(A_7__n, n=3, firing_delay=4.3)
    B_7__p_spl_ = pylse.split(B_7__p, n=3, firing_delay=4.3)
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
    A_0__n_spl_ = pylse.split(A_0__n, n=2, firing_delay=4.3)
    B_0__n_spl_ = pylse.split(B_0__n, n=2, firing_delay=4.3)

    g17_p = la(A_7__p_spl_[0], B_7__n_spl_[0])
    g17_p_spl_ = pylse.split(g17_p, n=2, firing_delay=4.3)
    g17_n = fa(A_7__n_spl_[0], B_7__p_spl_[0])
    g17_n_spl_ = pylse.split(g17_n, n=2, firing_delay=4.3)
    g18_p = la(A_6__p_spl_[0], B_6__p_spl_[0])
    g18_p_spl_ = pylse.split(g18_p, n=2, firing_delay=4.3)
    g18_n = fa(A_6__n_spl_[0], B_6__n_spl_[0])
    g18_n_spl_ = pylse.split(g18_n, n=2, firing_delay=4.3)
    g19_p = la(A_5__p_spl_[0], B_5__p_spl_[0])
    g19_p_spl_ = pylse.split(g19_p, n=2, firing_delay=4.3)
    g19_n = fa(A_5__n_spl_[0], B_5__n_spl_[0])
    g19_n_spl_ = pylse.split(g19_n, n=2, firing_delay=4.3)
    g20_p = la(A_4__p_spl_[0], B_4__p_spl_[0])
    g20_p_spl_ = pylse.split(g20_p, n=2, firing_delay=4.3)
    g20_n = fa(A_4__n_spl_[0], B_4__n_spl_[0])
    g20_n_spl_ = pylse.split(g20_n, n=2, firing_delay=4.3)
    g21_p = la(A_4__n_spl_[1], B_4__n_spl_[1])
    g21_n = fa(A_4__p_spl_[1], B_4__p_spl_[1])
    g22_p = la(g20_n_spl_[0], g21_n)
    g22_n = fa(g20_p_spl_[0], g21_p)
    g22_n_spl_ = pylse.split(g22_n, n=2, firing_delay=4.3)
    g23_p = la(A_3__p_spl_[0], B_3__p_spl_[0])
    g23_p_spl_ = pylse.split(g23_p, n=2, firing_delay=4.3)
    g23_n = fa(A_3__n_spl_[0], B_3__n_spl_[0])
    g23_n_spl_ = pylse.split(g23_n, n=2, firing_delay=4.3)
    g24_p = la(A_3__n_spl_[1], B_3__n_spl_[1])
    g24_p_spl_ = pylse.split(g24_p, n=2, firing_delay=4.3)
    g24_n = fa(A_3__p_spl_[1], B_3__p_spl_[1])
    g24_n_spl_ = pylse.split(g24_n, n=2, firing_delay=4.3)
    g25_p = la(A_2__p_spl_[0], B_2__p_spl_[0])
    g25_p_spl_ = pylse.split(g25_p, n=2, firing_delay=4.3)
    g25_n = fa(A_2__n_spl_[0], B_2__n_spl_[0])
    g25_n_spl_ = pylse.split(g25_n, n=2, firing_delay=4.3)
    g26_p = la(A_2__n_spl_[1], B_2__n_spl_[1])
    g26_p_spl_ = pylse.split(g26_p, n=2, firing_delay=4.3)
    g26_n = fa(A_2__p_spl_[1], B_2__p_spl_[1])
    g26_n_spl_ = pylse.split(g26_n, n=2, firing_delay=4.3)
    g27_p = la(A_1__p_spl_[0], B_1__p_spl_[0])
    g27_p_spl_ = pylse.split(g27_p, n=2, firing_delay=4.3)
    g27_n = fa(A_1__n_spl_[0], B_1__n_spl_[0])
    g27_n_spl_ = pylse.split(g27_n, n=2, firing_delay=4.3)
    g28_p = la(A_1__n_spl_[1], B_1__n_spl_[1])
    g28_p_spl_ = pylse.split(g28_p, n=2, firing_delay=4.3)
    g28_n = fa(A_1__p_spl_[1], B_1__p_spl_[1])
    g28_n_spl_ = pylse.split(g28_n, n=2, firing_delay=4.3)
    g29_p = la(A_0__p, B_0__p)
    g29_p_spl_ = pylse.split(g29_p, n=3, firing_delay=4.3)
    g29_n = fa(A_0__n_spl_[0], B_0__n_spl_[0])
    g29_n_spl_ = pylse.split(g29_n, n=2, firing_delay=4.3)
    g30_p = la(g28_n_spl_[0], g29_p_spl_[0])
    g30_n = fa(g28_p_spl_[0], g29_n_spl_[0])
    g31_p = la(g27_n_spl_[0], g30_n)
    g31_p_spl_ = pylse.split(g31_p, n=2, firing_delay=4.3)
    g31_n = fa(g27_p_spl_[0], g30_p)
    g31_n_spl_ = pylse.split(g31_n, n=2, firing_delay=4.3)
    g32_p = la(g26_n_spl_[0], g31_n_spl_[0])
    g32_n = fa(g26_p_spl_[0], g31_p_spl_[0])
    g33_p = la(g25_n_spl_[0], g32_n)
    g33_p_spl_ = pylse.split(g33_p, n=2, firing_delay=4.3)
    g33_n = fa(g25_p_spl_[0], g32_p)
    g33_n_spl_ = pylse.split(g33_n, n=2, firing_delay=4.3)
    g34_p = la(g24_n_spl_[0], g33_n_spl_[0])
    g34_n = fa(g24_p_spl_[0], g33_p_spl_[0])
    g35_p = la(g23_n_spl_[0], g34_n)
    g35_p_spl_ = pylse.split(g35_p, n=2, firing_delay=4.3)
    g35_n = fa(g23_p_spl_[0], g34_p)
    g36_p = la(g22_p, g35_n)
    g36_p_spl_ = pylse.split(g36_p, n=2, firing_delay=4.3)
    g36_n = fa(g22_n_spl_[0], g35_p_spl_[0])
    g37_p = la(g20_n_spl_[1], g36_n)
    g37_p_spl_ = pylse.split(g37_p, n=2, firing_delay=4.3)
    g37_n = fa(g20_p_spl_[1], g36_p_spl_[0])
    g38_p = la(A_5__n_spl_[1], B_5__n_spl_[1])
    g38_n = fa(A_5__p_spl_[1], B_5__p_spl_[1])
    g39_p = la(g19_n_spl_[0], g38_n)
    g39_n = fa(g19_p_spl_[0], g38_p)
    g39_n_spl_ = pylse.split(g39_n, n=2, firing_delay=4.3)
    g40_p = la(g37_n, g39_p)
    g40_p_spl_ = pylse.split(g40_p, n=2, firing_delay=4.3)
    g40_n = fa(g37_p_spl_[0], g39_n_spl_[0])
    g41_p = la(g19_n_spl_[1], g40_n)
    g41_p_spl_ = pylse.split(g41_p, n=2, firing_delay=4.3)
    g41_n = fa(g19_p_spl_[1], g40_p_spl_[0])
    g42_p = la(A_6__n_spl_[1], B_6__n_spl_[1])
    g42_n = fa(A_6__p_spl_[1], B_6__p_spl_[1])
    g43_p = la(g18_n_spl_[0], g42_n)
    g43_n = fa(g18_p_spl_[0], g42_p)
    g43_n_spl_ = pylse.split(g43_n, n=2, firing_delay=4.3)
    g44_p = la(g41_n, g43_p)
    g44_p_spl_ = pylse.split(g44_p, n=2, firing_delay=4.3)
    g44_n = fa(g41_p_spl_[0], g43_n_spl_[0])
    g45_p = la(g18_n_spl_[1], g44_n)
    g45_p_spl_ = pylse.split(g45_p, n=2, firing_delay=4.3)
    g45_n = fa(g18_p_spl_[1], g44_p_spl_[0])
    g45_n_spl_ = pylse.split(g45_n, n=3, firing_delay=4.3)
    g46_p = la(B_7__p_spl_[1], g45_n_spl_[0])
    g46_n = fa(B_7__n_spl_[1], g45_p_spl_[0])
    g47_p = la(g17_n_spl_[0], g46_n)
    g47_n = fa(g17_p_spl_[0], g46_p)
    g48_n = fa(A_7__n_spl_[1], g47_n)
    g48_n_spl_ = pylse.split(g48_n, n=7, firing_delay=4.3)
    g49_p = la(g45_n_spl_[1], g47_p)
    g49_p_spl_ = pylse.split(g49_p, n=7, firing_delay=4.3)
    g50_p = la(A_0__n_spl_[1], B_0__n_spl_[1])
    g51_n = fa(g29_p_spl_[1], g50_p)
    g52_n = fa(g49_p_spl_[0], g51_n)
    g53_p = la(g48_n_spl_[0], g52_n)
    g54_p = la(g27_n_spl_[1], g28_n_spl_[1])
    g54_n = fa(g27_p_spl_[1], g28_p_spl_[1])
    g55_p = la(g29_p_spl_[2], g54_p)
    g56_p = la(g29_n_spl_[1], g54_n)
    g57_n = fa(g55_p, g56_p)
    g58_n = fa(g49_p_spl_[1], g57_n)
    g59_p = la(g48_n_spl_[1], g58_n)
    g60_p = la(g25_n_spl_[1], g26_n_spl_[1])
    g60_n = fa(g25_p_spl_[1], g26_p_spl_[1])
    g61_n = fa(g31_n_spl_[1], g60_n)
    g62_n = fa(g31_p_spl_[1], g60_p)
    g63_p = la(g61_n, g62_n)
    g64_n = fa(g49_p_spl_[2], g63_p)
    g65_p = la(g48_n_spl_[2], g64_n)
    g66_p = la(g23_n_spl_[1], g24_n_spl_[1])
    g66_n = fa(g23_p_spl_[1], g24_p_spl_[1])
    g67_n = fa(g33_n_spl_[1], g66_n)
    g68_n = fa(g33_p_spl_[1], g66_p)
    g69_p = la(g67_n, g68_n)
    g70_n = fa(g49_p_spl_[3], g69_p)
    g71_p = la(g48_n_spl_[3], g70_n)
    g72_p = la(g22_n_spl_[1], g35_p_spl_[1])
    g73_n = fa(g36_p_spl_[1], g72_p)
    g74_n = fa(g49_p_spl_[4], g73_n)
    g75_p = la(g48_n_spl_[4], g74_n)
    g76_p = la(g37_p_spl_[1], g39_n_spl_[1])
    g77_n = fa(g40_p_spl_[1], g76_p)
    g78_n = fa(g49_p_spl_[5], g77_n)
    g79_p = la(g48_n_spl_[5], g78_n)
    g80_p = la(g41_p_spl_[1], g43_n_spl_[1])
    g81_n = fa(g44_p_spl_[1], g80_p)
    g82_n = fa(g49_p_spl_[6], g81_n)
    g83_p = la(g48_n_spl_[6], g82_n)
    g84_p = la(A_7__n_spl_[2], B_7__p_spl_[2])
    g84_n = fa(A_7__p_spl_[1], B_7__n_spl_[2])
    g85_p = la(g17_n_spl_[1], g84_n)
    g85_n = fa(g17_p_spl_[1], g84_p)
    g86_n = fa(g45_n_spl_[2], g85_n)
    g87_n = fa(g45_p_spl_[1], g85_p)
    g88_p = la(g86_n, g87_n)
    SUM_0_ = g53_p
    SUM_1_ = g59_p
    SUM_2_ = g65_p
    SUM_3_ = g71_p
    SUM_4_ = g75_p
    SUM_5_ = g79_p
    SUM_6_ = g83_p
    SUM_7_ = g88_p


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
    print(int(events['SUM_0_'][0] < T), int(events['SUM_1_'][0] < T), int(events['SUM_2_'][0] < T), int(events['SUM_3_'][0] < T), int(events['SUM_4_'][0] < T), int(events['SUM_5_'][0] < T), int(events['SUM_6_'][0] < T), int(events['SUM_7_'][0] < T))

if __name__ == "__main__":
    # Create clock signal
    T = 2000  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=4, name='clk')
    A_0__p, A_0__n, A_1__p, A_1__n, A_2__p, A_2__n, A_3__p, A_3__n, A_4__p, A_4__n, A_5__p, A_5__n, A_6__p, A_6__n, A_7__p, A_7__n, B_0__p, B_0__n, B_1__p, B_1__n, B_2__p, B_2__n, B_3__p, B_3__n, B_4__p, B_4__n, B_5__p, B_5__n, B_6__p, B_6__n, B_7__p, B_7__n= test_single_input(0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1)

    # Instantiate the module
    SUM_0_, SUM_1_, SUM_2_, SUM_3_, SUM_4_, SUM_5_, SUM_6_, SUM_7_= mymod(A_0__p, A_0__n, A_1__p, A_1__n, A_2__p, A_2__n, A_3__p, A_3__n, A_4__p, A_4__n, A_5__p, A_5__n, A_6__p, A_6__n, A_7__p, A_7__n, B_0__p, B_0__n, B_1__p, B_1__n, B_2__p, B_2__n, B_3__p, B_3__n, B_4__p, B_4__n, B_5__p, B_5__n, B_6__p, B_6__n, B_7__p, B_7__n)

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
