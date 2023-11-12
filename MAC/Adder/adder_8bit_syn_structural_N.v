
module mymod
(
  A[0],
  A[1],
  A[2],
  A[3],
  A[4],
  A[5],
  A[6],
  A[7],
  B[0],
  B[1],
  B[2],
  B[3],
  B[4],
  B[5],
  B[6],
  B[7],
  SUM[0],
  SUM[1],
  SUM[2],
  SUM[3],
  SUM[4],
  SUM[5],
  SUM[6],
  SUM[7]
);

  input A[0];input A[1];input A[2];input A[3];input A[4];input A[5];input A[6];input A[7];input B[0];input B[1];input B[2];input B[3];input B[4];input B[5];input B[6];input B[7];
  output SUM[0];output SUM[1];output SUM[2];output SUM[3];output SUM[4];output SUM[5];output SUM[6];output SUM[7];
  wire A[0]_p;
  wire A[0]_n;
  wire A[1]_p;
  wire A[1]_n;
  wire A[2]_p;
  wire A[2]_n;
  wire A[3]_p;
  wire A[3]_n;
  wire A[4]_p;
  wire A[4]_n;
  wire A[5]_p;
  wire A[5]_n;
  wire A[6]_p;
  wire A[6]_n;
  wire A[7]_p;
  wire A[7]_n;
  wire B[0]_p;
  wire B[0]_n;
  wire B[1]_p;
  wire B[1]_n;
  wire B[2]_p;
  wire B[2]_n;
  wire B[3]_p;
  wire B[3]_n;
  wire B[4]_p;
  wire B[4]_n;
  wire B[5]_p;
  wire B[5]_n;
  wire B[6]_p;
  wire B[6]_n;
  wire B[7]_p;
  wire B[7]_n;
  wire g17_p;
  wire g17_n;
  wire g18_p;
  wire g18_n;
  wire g19_p;
  wire g19_n;
  wire g20_p;
  wire g20_n;
  wire g21_p;
  wire g21_n;
  wire g22_p;
  wire g22_n;
  wire g23_p;
  wire g23_n;
  wire g24_p;
  wire g24_n;
  wire g25_p;
  wire g25_n;
  wire g26_p;
  wire g26_n;
  wire g27_p;
  wire g27_n;
  wire g28_p;
  wire g28_n;
  wire g29_p;
  wire g29_n;
  wire g30_p;
  wire g30_n;
  wire g31_p;
  wire g31_n;
  wire g32_p;
  wire g32_n;
  wire g33_p;
  wire g33_n;
  wire g34_p;
  wire g34_n;
  wire g35_p;
  wire g35_n;
  wire g36_p;
  wire g36_n;
  wire g37_p;
  wire g37_n;
  wire g38_p;
  wire g38_n;
  wire g39_p;
  wire g39_n;
  wire g40_p;
  wire g40_n;
  wire g41_p;
  wire g41_n;
  wire g42_p;
  wire g42_n;
  wire g43_p;
  wire g43_n;
  wire g44_p;
  wire g44_n;
  wire g45_p;
  wire g45_n;
  wire g46_p;
  wire g46_n;
  wire g47_p;
  wire g47_n;
  wire g48_p;
  wire g48_n;
  wire g49_p;
  wire g49_n;
  wire g50_p;
  wire g50_n;
  wire g51_p;
  wire g51_n;
  wire g52_p;
  wire g52_n;
  wire g53_p;
  wire g53_n;
  wire g54_p;
  wire g54_n;
  wire g55_p;
  wire g55_n;
  wire g56_p;
  wire g56_n;
  wire g57_p;
  wire g57_n;
  wire g58_p;
  wire g58_n;
  wire g59_p;
  wire g59_n;
  wire g60_p;
  wire g60_n;
  wire g61_p;
  wire g61_n;
  wire g62_p;
  wire g62_n;
  wire g63_p;
  wire g63_n;
  wire g64_p;
  wire g64_n;
  wire g65_p;
  wire g65_n;
  wire g66_p;
  wire g66_n;
  wire g67_p;
  wire g67_n;
  wire g68_p;
  wire g68_n;
  wire g69_p;
  wire g69_n;
  wire g70_p;
  wire g70_n;
  wire g71_p;
  wire g71_n;
  wire g72_p;
  wire g72_n;
  wire g73_p;
  wire g73_n;
  wire g74_p;
  wire g74_n;
  wire g75_p;
  wire g75_n;
  wire g76_p;
  wire g76_n;
  wire g77_p;
  wire g77_n;
  wire g78_p;
  wire g78_n;
  wire g79_p;
  wire g79_n;
  wire g80_p;
  wire g80_n;
  wire g81_p;
  wire g81_n;
  wire g82_p;
  wire g82_n;
  wire g83_p;
  wire g83_n;
  wire g84_p;
  wire g84_n;
  wire g85_p;
  wire g85_n;
  wire g86_p;
  wire g86_n;
  wire g87_p;
  wire g87_n;
  wire g88_p;
  wire g88_n;
  wire A[7]_p_spl_;
  wire B[7]_n_spl_;
  wire B[7]_n_spl_0;
  wire A[7]_n_spl_;
  wire A[7]_n_spl_0;
  wire B[7]_p_spl_;
  wire B[7]_p_spl_0;
  wire A[6]_p_spl_;
  wire B[6]_p_spl_;
  wire A[6]_n_spl_;
  wire B[6]_n_spl_;
  wire A[5]_p_spl_;
  wire B[5]_p_spl_;
  wire A[5]_n_spl_;
  wire B[5]_n_spl_;
  wire A[4]_p_spl_;
  wire B[4]_p_spl_;
  wire A[4]_n_spl_;
  wire B[4]_n_spl_;
  wire g20_n_spl_;
  wire g20_p_spl_;
  wire A[3]_p_spl_;
  wire B[3]_p_spl_;
  wire A[3]_n_spl_;
  wire B[3]_n_spl_;
  wire A[2]_p_spl_;
  wire B[2]_p_spl_;
  wire A[2]_n_spl_;
  wire B[2]_n_spl_;
  wire A[1]_p_spl_;
  wire B[1]_p_spl_;
  wire A[1]_n_spl_;
  wire B[1]_n_spl_;
  wire A[0]_n_spl_;
  wire B[0]_n_spl_;
  wire g28_n_spl_;
  wire g29_p_spl_;
  wire g29_p_spl_0;
  wire g28_p_spl_;
  wire g29_n_spl_;
  wire g27_n_spl_;
  wire g27_p_spl_;
  wire g26_n_spl_;
  wire g31_n_spl_;
  wire g26_p_spl_;
  wire g31_p_spl_;
  wire g25_n_spl_;
  wire g25_p_spl_;
  wire g24_n_spl_;
  wire g33_n_spl_;
  wire g24_p_spl_;
  wire g33_p_spl_;
  wire g23_n_spl_;
  wire g23_p_spl_;
  wire g22_n_spl_;
  wire g35_p_spl_;
  wire g36_p_spl_;
  wire g19_n_spl_;
  wire g19_p_spl_;
  wire g37_p_spl_;
  wire g39_n_spl_;
  wire g40_p_spl_;
  wire g18_n_spl_;
  wire g18_p_spl_;
  wire g41_p_spl_;
  wire g43_n_spl_;
  wire g44_p_spl_;
  wire g45_n_spl_;
  wire g45_n_spl_0;
  wire g45_p_spl_;
  wire g17_n_spl_;
  wire g17_p_spl_;
  wire g49_p_spl_;
  wire g49_p_spl_0;
  wire g49_p_spl_00;
  wire g49_p_spl_01;
  wire g49_p_spl_1;
  wire g49_p_spl_10;
  wire g48_n_spl_;
  wire g48_n_spl_0;
  wire g48_n_spl_00;
  wire g48_n_spl_01;
  wire g48_n_spl_1;
  wire g48_n_spl_10;

  buf

  (
    A[0]_p,
    A[0]
  );


  not

  (
    A[0]_n,
    A[0]
  );


  buf

  (
    A[1]_p,
    A[1]
  );


  not

  (
    A[1]_n,
    A[1]
  );


  buf

  (
    A[2]_p,
    A[2]
  );


  not

  (
    A[2]_n,
    A[2]
  );


  buf

  (
    A[3]_p,
    A[3]
  );


  not

  (
    A[3]_n,
    A[3]
  );


  buf

  (
    A[4]_p,
    A[4]
  );


  not

  (
    A[4]_n,
    A[4]
  );


  buf

  (
    A[5]_p,
    A[5]
  );


  not

  (
    A[5]_n,
    A[5]
  );


  buf

  (
    A[6]_p,
    A[6]
  );


  not

  (
    A[6]_n,
    A[6]
  );


  buf

  (
    A[7]_p,
    A[7]
  );


  not

  (
    A[7]_n,
    A[7]
  );


  buf

  (
    B[0]_p,
    B[0]
  );


  not

  (
    B[0]_n,
    B[0]
  );


  buf

  (
    B[1]_p,
    B[1]
  );


  not

  (
    B[1]_n,
    B[1]
  );


  buf

  (
    B[2]_p,
    B[2]
  );


  not

  (
    B[2]_n,
    B[2]
  );


  buf

  (
    B[3]_p,
    B[3]
  );


  not

  (
    B[3]_n,
    B[3]
  );


  buf

  (
    B[4]_p,
    B[4]
  );


  not

  (
    B[4]_n,
    B[4]
  );


  buf

  (
    B[5]_p,
    B[5]
  );


  not

  (
    B[5]_n,
    B[5]
  );


  buf

  (
    B[6]_p,
    B[6]
  );


  not

  (
    B[6]_n,
    B[6]
  );


  buf

  (
    B[7]_p,
    B[7]
  );


  not

  (
    B[7]_n,
    B[7]
  );


  and

  (
    g17_p,
    A[7]_p_spl_,
    B[7]_n_spl_0
  );


  or

  (
    g17_n,
    A[7]_n_spl_0,
    B[7]_p_spl_0
  );


  and

  (
    g18_p,
    A[6]_p_spl_,
    B[6]_p_spl_
  );


  or

  (
    g18_n,
    A[6]_n_spl_,
    B[6]_n_spl_
  );


  and

  (
    g19_p,
    A[5]_p_spl_,
    B[5]_p_spl_
  );


  or

  (
    g19_n,
    A[5]_n_spl_,
    B[5]_n_spl_
  );


  and

  (
    g20_p,
    A[4]_p_spl_,
    B[4]_p_spl_
  );


  or

  (
    g20_n,
    A[4]_n_spl_,
    B[4]_n_spl_
  );


  and

  (
    g21_p,
    A[4]_n_spl_,
    B[4]_n_spl_
  );


  or

  (
    g21_n,
    A[4]_p_spl_,
    B[4]_p_spl_
  );


  and

  (
    g22_p,
    g20_n_spl_,
    g21_n
  );


  or

  (
    g22_n,
    g20_p_spl_,
    g21_p
  );


  and

  (
    g23_p,
    A[3]_p_spl_,
    B[3]_p_spl_
  );


  or

  (
    g23_n,
    A[3]_n_spl_,
    B[3]_n_spl_
  );


  and

  (
    g24_p,
    A[3]_n_spl_,
    B[3]_n_spl_
  );


  or

  (
    g24_n,
    A[3]_p_spl_,
    B[3]_p_spl_
  );


  and

  (
    g25_p,
    A[2]_p_spl_,
    B[2]_p_spl_
  );


  or

  (
    g25_n,
    A[2]_n_spl_,
    B[2]_n_spl_
  );


  and

  (
    g26_p,
    A[2]_n_spl_,
    B[2]_n_spl_
  );


  or

  (
    g26_n,
    A[2]_p_spl_,
    B[2]_p_spl_
  );


  and

  (
    g27_p,
    A[1]_p_spl_,
    B[1]_p_spl_
  );


  or

  (
    g27_n,
    A[1]_n_spl_,
    B[1]_n_spl_
  );


  and

  (
    g28_p,
    A[1]_n_spl_,
    B[1]_n_spl_
  );


  or

  (
    g28_n,
    A[1]_p_spl_,
    B[1]_p_spl_
  );


  and

  (
    g29_p,
    A[0]_p,
    B[0]_p
  );


  or

  (
    g29_n,
    A[0]_n_spl_,
    B[0]_n_spl_
  );


  and

  (
    g30_p,
    g28_n_spl_,
    g29_p_spl_0
  );


  or

  (
    g30_n,
    g28_p_spl_,
    g29_n_spl_
  );


  and

  (
    g31_p,
    g27_n_spl_,
    g30_n
  );


  or

  (
    g31_n,
    g27_p_spl_,
    g30_p
  );


  and

  (
    g32_p,
    g26_n_spl_,
    g31_n_spl_
  );


  or

  (
    g32_n,
    g26_p_spl_,
    g31_p_spl_
  );


  and

  (
    g33_p,
    g25_n_spl_,
    g32_n
  );


  or

  (
    g33_n,
    g25_p_spl_,
    g32_p
  );


  and

  (
    g34_p,
    g24_n_spl_,
    g33_n_spl_
  );


  or

  (
    g34_n,
    g24_p_spl_,
    g33_p_spl_
  );


  and

  (
    g35_p,
    g23_n_spl_,
    g34_n
  );


  or

  (
    g35_n,
    g23_p_spl_,
    g34_p
  );


  and

  (
    g36_p,
    g22_p,
    g35_n
  );


  or

  (
    g36_n,
    g22_n_spl_,
    g35_p_spl_
  );


  and

  (
    g37_p,
    g20_n_spl_,
    g36_n
  );


  or

  (
    g37_n,
    g20_p_spl_,
    g36_p_spl_
  );


  and

  (
    g38_p,
    A[5]_n_spl_,
    B[5]_n_spl_
  );


  or

  (
    g38_n,
    A[5]_p_spl_,
    B[5]_p_spl_
  );


  and

  (
    g39_p,
    g19_n_spl_,
    g38_n
  );


  or

  (
    g39_n,
    g19_p_spl_,
    g38_p
  );


  and

  (
    g40_p,
    g37_n,
    g39_p
  );


  or

  (
    g40_n,
    g37_p_spl_,
    g39_n_spl_
  );


  and

  (
    g41_p,
    g19_n_spl_,
    g40_n
  );


  or

  (
    g41_n,
    g19_p_spl_,
    g40_p_spl_
  );


  and

  (
    g42_p,
    A[6]_n_spl_,
    B[6]_n_spl_
  );


  or

  (
    g42_n,
    A[6]_p_spl_,
    B[6]_p_spl_
  );


  and

  (
    g43_p,
    g18_n_spl_,
    g42_n
  );


  or

  (
    g43_n,
    g18_p_spl_,
    g42_p
  );


  and

  (
    g44_p,
    g41_n,
    g43_p
  );


  or

  (
    g44_n,
    g41_p_spl_,
    g43_n_spl_
  );


  and

  (
    g45_p,
    g18_n_spl_,
    g44_n
  );


  or

  (
    g45_n,
    g18_p_spl_,
    g44_p_spl_
  );


  and

  (
    g46_p,
    B[7]_p_spl_0,
    g45_n_spl_0
  );


  or

  (
    g46_n,
    B[7]_n_spl_0,
    g45_p_spl_
  );


  and

  (
    g47_p,
    g17_n_spl_,
    g46_n
  );


  or

  (
    g47_n,
    g17_p_spl_,
    g46_p
  );


  or

  (
    g48_n,
    A[7]_n_spl_0,
    g47_n
  );


  and

  (
    g49_p,
    g45_n_spl_0,
    g47_p
  );


  and

  (
    g50_p,
    A[0]_n_spl_,
    B[0]_n_spl_
  );


  or

  (
    g51_n,
    g29_p_spl_0,
    g50_p
  );


  or

  (
    g52_n,
    g49_p_spl_00,
    g51_n
  );


  and

  (
    g53_p,
    g48_n_spl_00,
    g52_n
  );


  and

  (
    g54_p,
    g27_n_spl_,
    g28_n_spl_
  );


  or

  (
    g54_n,
    g27_p_spl_,
    g28_p_spl_
  );


  and

  (
    g55_p,
    g29_p_spl_,
    g54_p
  );


  and

  (
    g56_p,
    g29_n_spl_,
    g54_n
  );


  or

  (
    g57_n,
    g55_p,
    g56_p
  );


  or

  (
    g58_n,
    g49_p_spl_00,
    g57_n
  );


  and

  (
    g59_p,
    g48_n_spl_00,
    g58_n
  );


  and

  (
    g60_p,
    g25_n_spl_,
    g26_n_spl_
  );


  or

  (
    g60_n,
    g25_p_spl_,
    g26_p_spl_
  );


  or

  (
    g61_n,
    g31_n_spl_,
    g60_n
  );


  or

  (
    g62_n,
    g31_p_spl_,
    g60_p
  );


  and

  (
    g63_p,
    g61_n,
    g62_n
  );


  or

  (
    g64_n,
    g49_p_spl_01,
    g63_p
  );


  and

  (
    g65_p,
    g48_n_spl_01,
    g64_n
  );


  and

  (
    g66_p,
    g23_n_spl_,
    g24_n_spl_
  );


  or

  (
    g66_n,
    g23_p_spl_,
    g24_p_spl_
  );


  or

  (
    g67_n,
    g33_n_spl_,
    g66_n
  );


  or

  (
    g68_n,
    g33_p_spl_,
    g66_p
  );


  and

  (
    g69_p,
    g67_n,
    g68_n
  );


  or

  (
    g70_n,
    g49_p_spl_01,
    g69_p
  );


  and

  (
    g71_p,
    g48_n_spl_01,
    g70_n
  );


  and

  (
    g72_p,
    g22_n_spl_,
    g35_p_spl_
  );


  or

  (
    g73_n,
    g36_p_spl_,
    g72_p
  );


  or

  (
    g74_n,
    g49_p_spl_10,
    g73_n
  );


  and

  (
    g75_p,
    g48_n_spl_10,
    g74_n
  );


  and

  (
    g76_p,
    g37_p_spl_,
    g39_n_spl_
  );


  or

  (
    g77_n,
    g40_p_spl_,
    g76_p
  );


  or

  (
    g78_n,
    g49_p_spl_10,
    g77_n
  );


  and

  (
    g79_p,
    g48_n_spl_10,
    g78_n
  );


  and

  (
    g80_p,
    g41_p_spl_,
    g43_n_spl_
  );


  or

  (
    g81_n,
    g44_p_spl_,
    g80_p
  );


  or

  (
    g82_n,
    g49_p_spl_1,
    g81_n
  );


  and

  (
    g83_p,
    g48_n_spl_1,
    g82_n
  );


  and

  (
    g84_p,
    A[7]_n_spl_,
    B[7]_p_spl_
  );


  or

  (
    g84_n,
    A[7]_p_spl_,
    B[7]_n_spl_
  );


  and

  (
    g85_p,
    g17_n_spl_,
    g84_n
  );


  or

  (
    g85_n,
    g17_p_spl_,
    g84_p
  );


  or

  (
    g86_n,
    g45_n_spl_,
    g85_n
  );


  or

  (
    g87_n,
    g45_p_spl_,
    g85_p
  );


  and

  (
    g88_p,
    g86_n,
    g87_n
  );


  not

  (
    SUM[0],
    g53_p
  );


  not

  (
    SUM[1],
    g59_p
  );


  not

  (
    SUM[2],
    g65_p
  );


  not

  (
    SUM[3],
    g71_p
  );


  not

  (
    SUM[4],
    g75_p
  );


  not

  (
    SUM[5],
    g79_p
  );


  not

  (
    SUM[6],
    g83_p
  );


  buf

  (
    SUM[7],
    g88_p
  );


  buf

  (
    A[7]_p_spl_,
    A[7]_p
  );


  buf

  (
    B[7]_n_spl_,
    B[7]_n
  );


  buf

  (
    B[7]_n_spl_0,
    B[7]_n_spl_
  );


  buf

  (
    A[7]_n_spl_,
    A[7]_n
  );


  buf

  (
    A[7]_n_spl_0,
    A[7]_n_spl_
  );


  buf

  (
    B[7]_p_spl_,
    B[7]_p
  );


  buf

  (
    B[7]_p_spl_0,
    B[7]_p_spl_
  );


  buf

  (
    A[6]_p_spl_,
    A[6]_p
  );


  buf

  (
    B[6]_p_spl_,
    B[6]_p
  );


  buf

  (
    A[6]_n_spl_,
    A[6]_n
  );


  buf

  (
    B[6]_n_spl_,
    B[6]_n
  );


  buf

  (
    A[5]_p_spl_,
    A[5]_p
  );


  buf

  (
    B[5]_p_spl_,
    B[5]_p
  );


  buf

  (
    A[5]_n_spl_,
    A[5]_n
  );


  buf

  (
    B[5]_n_spl_,
    B[5]_n
  );


  buf

  (
    A[4]_p_spl_,
    A[4]_p
  );


  buf

  (
    B[4]_p_spl_,
    B[4]_p
  );


  buf

  (
    A[4]_n_spl_,
    A[4]_n
  );


  buf

  (
    B[4]_n_spl_,
    B[4]_n
  );


  buf

  (
    g20_n_spl_,
    g20_n
  );


  buf

  (
    g20_p_spl_,
    g20_p
  );


  buf

  (
    A[3]_p_spl_,
    A[3]_p
  );


  buf

  (
    B[3]_p_spl_,
    B[3]_p
  );


  buf

  (
    A[3]_n_spl_,
    A[3]_n
  );


  buf

  (
    B[3]_n_spl_,
    B[3]_n
  );


  buf

  (
    A[2]_p_spl_,
    A[2]_p
  );


  buf

  (
    B[2]_p_spl_,
    B[2]_p
  );


  buf

  (
    A[2]_n_spl_,
    A[2]_n
  );


  buf

  (
    B[2]_n_spl_,
    B[2]_n
  );


  buf

  (
    A[1]_p_spl_,
    A[1]_p
  );


  buf

  (
    B[1]_p_spl_,
    B[1]_p
  );


  buf

  (
    A[1]_n_spl_,
    A[1]_n
  );


  buf

  (
    B[1]_n_spl_,
    B[1]_n
  );


  buf

  (
    A[0]_n_spl_,
    A[0]_n
  );


  buf

  (
    B[0]_n_spl_,
    B[0]_n
  );


  buf

  (
    g28_n_spl_,
    g28_n
  );


  buf

  (
    g29_p_spl_,
    g29_p
  );


  buf

  (
    g29_p_spl_0,
    g29_p_spl_
  );


  buf

  (
    g28_p_spl_,
    g28_p
  );


  buf

  (
    g29_n_spl_,
    g29_n
  );


  buf

  (
    g27_n_spl_,
    g27_n
  );


  buf

  (
    g27_p_spl_,
    g27_p
  );


  buf

  (
    g26_n_spl_,
    g26_n
  );


  buf

  (
    g31_n_spl_,
    g31_n
  );


  buf

  (
    g26_p_spl_,
    g26_p
  );


  buf

  (
    g31_p_spl_,
    g31_p
  );


  buf

  (
    g25_n_spl_,
    g25_n
  );


  buf

  (
    g25_p_spl_,
    g25_p
  );


  buf

  (
    g24_n_spl_,
    g24_n
  );


  buf

  (
    g33_n_spl_,
    g33_n
  );


  buf

  (
    g24_p_spl_,
    g24_p
  );


  buf

  (
    g33_p_spl_,
    g33_p
  );


  buf

  (
    g23_n_spl_,
    g23_n
  );


  buf

  (
    g23_p_spl_,
    g23_p
  );


  buf

  (
    g22_n_spl_,
    g22_n
  );


  buf

  (
    g35_p_spl_,
    g35_p
  );


  buf

  (
    g36_p_spl_,
    g36_p
  );


  buf

  (
    g19_n_spl_,
    g19_n
  );


  buf

  (
    g19_p_spl_,
    g19_p
  );


  buf

  (
    g37_p_spl_,
    g37_p
  );


  buf

  (
    g39_n_spl_,
    g39_n
  );


  buf

  (
    g40_p_spl_,
    g40_p
  );


  buf

  (
    g18_n_spl_,
    g18_n
  );


  buf

  (
    g18_p_spl_,
    g18_p
  );


  buf

  (
    g41_p_spl_,
    g41_p
  );


  buf

  (
    g43_n_spl_,
    g43_n
  );


  buf

  (
    g44_p_spl_,
    g44_p
  );


  buf

  (
    g45_n_spl_,
    g45_n
  );


  buf

  (
    g45_n_spl_0,
    g45_n_spl_
  );


  buf

  (
    g45_p_spl_,
    g45_p
  );


  buf

  (
    g17_n_spl_,
    g17_n
  );


  buf

  (
    g17_p_spl_,
    g17_p
  );


  buf

  (
    g49_p_spl_,
    g49_p
  );


  buf

  (
    g49_p_spl_0,
    g49_p_spl_
  );


  buf

  (
    g49_p_spl_00,
    g49_p_spl_0
  );


  buf

  (
    g49_p_spl_01,
    g49_p_spl_0
  );


  buf

  (
    g49_p_spl_1,
    g49_p_spl_
  );


  buf

  (
    g49_p_spl_10,
    g49_p_spl_1
  );


  buf

  (
    g48_n_spl_,
    g48_n
  );


  buf

  (
    g48_n_spl_0,
    g48_n_spl_
  );


  buf

  (
    g48_n_spl_00,
    g48_n_spl_0
  );


  buf

  (
    g48_n_spl_01,
    g48_n_spl_0
  );


  buf

  (
    g48_n_spl_1,
    g48_n_spl_
  );


  buf

  (
    g48_n_spl_10,
    g48_n_spl_1
  );


endmodule
