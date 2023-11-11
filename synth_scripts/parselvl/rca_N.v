
module mymod
(
  X_0,
  Y_0,
  X_1,
  Y_1,
  X_2,
  Y_2,
  X_3,
  Y_3,
  rippe_adder|XX_2,
  rippe_adder|XX_3,
  rippe_adder|XXX_3,
  rippe_adder|YY_2,
  rippe_adder|YY_3,
  rippe_adder|YYY_3,
  rippe_adder|sS_0,
  rippe_adder|SS_0,
  rippe_adder|SSS_0,
  rippe_adder|sS_1,
  rippe_adder|SS_1,
  rippe_adder|sS_2,
  rippe_adder|xw1,
  rippe_adder|xw2,
  rippe_adder|xw3,
  n87_o2,
  n88_o2,
  n93_o2,
  n94_o2,
  n77_o2,
  n78_o2,
  S_0,
  S_1,
  S_2,
  S_3,
  Co,
  n61_li01_li01,
  n67_li03_li03,
  n70_li04_li04,
  n79_li07_li07,
  n85_li09_li09,
  n88_li10_li10,
  n94_li12_li12,
  n97_li13_li13,
  n100_li14_li14,
  n103_li15_li15,
  n106_li16_li16,
  n109_li17_li17,
  n112_li18_li18,
  n115_li19_li19,
  n118_li20_li20,
  n87_i2,
  n88_i2,
  n93_i2,
  n94_i2,
  n77_i2,
  n78_i2
);

  input X_0;input Y_0;input X_1;input Y_1;input X_2;input Y_2;input X_3;input Y_3;input rippe_adder|XX_2;input rippe_adder|XX_3;input rippe_adder|XXX_3;input rippe_adder|YY_2;input rippe_adder|YY_3;input rippe_adder|YYY_3;input rippe_adder|sS_0;input rippe_adder|SS_0;input rippe_adder|SSS_0;input rippe_adder|sS_1;input rippe_adder|SS_1;input rippe_adder|sS_2;input rippe_adder|xw1;input rippe_adder|xw2;input rippe_adder|xw3;input n87_o2;input n88_o2;input n93_o2;input n94_o2;input n77_o2;input n78_o2;
  output S_0;output S_1;output S_2;output S_3;output Co;output n61_li01_li01;output n67_li03_li03;output n70_li04_li04;output n79_li07_li07;output n85_li09_li09;output n88_li10_li10;output n94_li12_li12;output n97_li13_li13;output n100_li14_li14;output n103_li15_li15;output n106_li16_li16;output n109_li17_li17;output n112_li18_li18;output n115_li19_li19;output n118_li20_li20;output n87_i2;output n88_i2;output n93_i2;output n94_i2;output n77_i2;output n78_i2;
  wire X_0_p;
  wire X_0_n;
  wire Y_0_p;
  wire Y_0_n;
  wire X_1_p;
  wire X_1_n;
  wire Y_1_p;
  wire Y_1_n;
  wire X_2_p;
  wire X_2_n;
  wire Y_2_p;
  wire Y_2_n;
  wire X_3_p;
  wire X_3_n;
  wire Y_3_p;
  wire Y_3_n;
  wire rippe_adder|XX_2_p;
  wire rippe_adder|XX_2_n;
  wire rippe_adder|XX_3_p;
  wire rippe_adder|XX_3_n;
  wire rippe_adder|XXX_3_p;
  wire rippe_adder|XXX_3_n;
  wire rippe_adder|YY_2_p;
  wire rippe_adder|YY_2_n;
  wire rippe_adder|YY_3_p;
  wire rippe_adder|YY_3_n;
  wire rippe_adder|YYY_3_p;
  wire rippe_adder|YYY_3_n;
  wire rippe_adder|sS_0_p;
  wire rippe_adder|sS_0_n;
  wire rippe_adder|SS_0_p;
  wire rippe_adder|SS_0_n;
  wire rippe_adder|SSS_0_p;
  wire rippe_adder|SSS_0_n;
  wire rippe_adder|sS_1_p;
  wire rippe_adder|sS_1_n;
  wire rippe_adder|SS_1_p;
  wire rippe_adder|SS_1_n;
  wire rippe_adder|sS_2_p;
  wire rippe_adder|sS_2_n;
  wire rippe_adder|xw1_p;
  wire rippe_adder|xw1_n;
  wire rippe_adder|xw2_p;
  wire rippe_adder|xw2_n;
  wire rippe_adder|xw3_p;
  wire rippe_adder|xw3_n;
  wire n87_o2_p;
  wire n87_o2_n;
  wire n88_o2_p;
  wire n88_o2_n;
  wire n93_o2_p;
  wire n93_o2_n;
  wire n94_o2_p;
  wire n94_o2_n;
  wire n77_o2_p;
  wire n77_o2_n;
  wire n78_o2_p;
  wire n78_o2_n;
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
  wire n77_o2_n_spl_;
  wire g31_n_spl_;
  wire g35_n_spl_;
  wire n87_o2_n_spl_;
  wire g39_n_spl_;
  wire n93_o2_n_spl_;
  wire g43_n_spl_;
  wire X_1_p_spl_;
  wire Y_1_p_spl_;
  wire rippe_adder|XX_2_p_spl_;
  wire rippe_adder|YY_2_p_spl_;
  wire rippe_adder|XXX_3_p_spl_;
  wire rippe_adder|YYY_3_p_spl_;

  buf

  (
    X_0_p,
    X_0
  );


  not

  (
    X_0_n,
    X_0
  );


  buf

  (
    Y_0_p,
    Y_0
  );


  not

  (
    Y_0_n,
    Y_0
  );


  buf

  (
    X_1_p,
    X_1
  );


  not

  (
    X_1_n,
    X_1
  );


  buf

  (
    Y_1_p,
    Y_1
  );


  not

  (
    Y_1_n,
    Y_1
  );


  buf

  (
    X_2_p,
    X_2
  );


  not

  (
    X_2_n,
    X_2
  );


  buf

  (
    Y_2_p,
    Y_2
  );


  not

  (
    Y_2_n,
    Y_2
  );


  buf

  (
    X_3_p,
    X_3
  );


  not

  (
    X_3_n,
    X_3
  );


  buf

  (
    Y_3_p,
    Y_3
  );


  not

  (
    Y_3_n,
    Y_3
  );


  buf

  (
    rippe_adder|XX_2_p,
    rippe_adder|XX_2
  );


  not

  (
    rippe_adder|XX_2_n,
    rippe_adder|XX_2
  );


  buf

  (
    rippe_adder|XX_3_p,
    rippe_adder|XX_3
  );


  not

  (
    rippe_adder|XX_3_n,
    rippe_adder|XX_3
  );


  buf

  (
    rippe_adder|XXX_3_p,
    rippe_adder|XXX_3
  );


  not

  (
    rippe_adder|XXX_3_n,
    rippe_adder|XXX_3
  );


  buf

  (
    rippe_adder|YY_2_p,
    rippe_adder|YY_2
  );


  not

  (
    rippe_adder|YY_2_n,
    rippe_adder|YY_2
  );


  buf

  (
    rippe_adder|YY_3_p,
    rippe_adder|YY_3
  );


  not

  (
    rippe_adder|YY_3_n,
    rippe_adder|YY_3
  );


  buf

  (
    rippe_adder|YYY_3_p,
    rippe_adder|YYY_3
  );


  not

  (
    rippe_adder|YYY_3_n,
    rippe_adder|YYY_3
  );


  buf

  (
    rippe_adder|sS_0_p,
    rippe_adder|sS_0
  );


  not

  (
    rippe_adder|sS_0_n,
    rippe_adder|sS_0
  );


  buf

  (
    rippe_adder|SS_0_p,
    rippe_adder|SS_0
  );


  not

  (
    rippe_adder|SS_0_n,
    rippe_adder|SS_0
  );


  buf

  (
    rippe_adder|SSS_0_p,
    rippe_adder|SSS_0
  );


  not

  (
    rippe_adder|SSS_0_n,
    rippe_adder|SSS_0
  );


  buf

  (
    rippe_adder|sS_1_p,
    rippe_adder|sS_1
  );


  not

  (
    rippe_adder|sS_1_n,
    rippe_adder|sS_1
  );


  buf

  (
    rippe_adder|SS_1_p,
    rippe_adder|SS_1
  );


  not

  (
    rippe_adder|SS_1_n,
    rippe_adder|SS_1
  );


  buf

  (
    rippe_adder|sS_2_p,
    rippe_adder|sS_2
  );


  not

  (
    rippe_adder|sS_2_n,
    rippe_adder|sS_2
  );


  buf

  (
    rippe_adder|xw1_p,
    rippe_adder|xw1
  );


  not

  (
    rippe_adder|xw1_n,
    rippe_adder|xw1
  );


  buf

  (
    rippe_adder|xw2_p,
    rippe_adder|xw2
  );


  not

  (
    rippe_adder|xw2_n,
    rippe_adder|xw2
  );


  buf

  (
    rippe_adder|xw3_p,
    rippe_adder|xw3
  );


  not

  (
    rippe_adder|xw3_n,
    rippe_adder|xw3
  );


  buf

  (
    n87_o2_p,
    n87_o2
  );


  not

  (
    n87_o2_n,
    n87_o2
  );


  buf

  (
    n88_o2_p,
    n88_o2
  );


  not

  (
    n88_o2_n,
    n88_o2
  );


  buf

  (
    n93_o2_p,
    n93_o2
  );


  not

  (
    n93_o2_n,
    n93_o2
  );


  buf

  (
    n94_o2_p,
    n94_o2
  );


  not

  (
    n94_o2_n,
    n94_o2
  );


  buf

  (
    n77_o2_p,
    n77_o2
  );


  not

  (
    n77_o2_n,
    n77_o2
  );


  buf

  (
    n78_o2_p,
    n78_o2
  );


  not

  (
    n78_o2_n,
    n78_o2
  );


  and

  (
    g30_p,
    n77_o2_n_spl_,
    n78_o2_p
  );


  or

  (
    g30_n,
    n77_o2_p,
    n78_o2_n
  );


  or

  (
    g31_n,
    rippe_adder|xw3_n,
    g30_n
  );


  or

  (
    g32_n,
    rippe_adder|xw3_p,
    g30_p
  );


  and

  (
    g33_p,
    g31_n_spl_,
    g32_n
  );


  and

  (
    g34_p,
    n77_o2_n_spl_,
    g31_n_spl_
  );


  or

  (
    g35_n,
    X_0_n,
    Y_0_n
  );


  or

  (
    g36_n,
    X_0_p,
    Y_0_p
  );


  and

  (
    g37_p,
    g35_n_spl_,
    g36_n
  );


  and

  (
    g38_p,
    n87_o2_n_spl_,
    n88_o2_p
  );


  or

  (
    g38_n,
    n87_o2_p,
    n88_o2_n
  );


  or

  (
    g39_n,
    rippe_adder|xw1_n,
    g38_n
  );


  or

  (
    g40_n,
    rippe_adder|xw1_p,
    g38_p
  );


  and

  (
    g41_p,
    g39_n_spl_,
    g40_n
  );


  and

  (
    g42_p,
    n93_o2_n_spl_,
    n94_o2_p
  );


  or

  (
    g42_n,
    n93_o2_p,
    n94_o2_n
  );


  or

  (
    g43_n,
    rippe_adder|xw2_n,
    g42_n
  );


  or

  (
    g44_n,
    rippe_adder|xw2_p,
    g42_p
  );


  and

  (
    g45_p,
    g43_n_spl_,
    g44_n
  );


  and

  (
    g46_p,
    n87_o2_n_spl_,
    g39_n_spl_
  );


  and

  (
    g47_p,
    n93_o2_n_spl_,
    g43_n_spl_
  );


  and

  (
    g48_p,
    X_1_p_spl_,
    Y_1_p_spl_
  );


  or

  (
    g49_n,
    X_1_p_spl_,
    Y_1_p_spl_
  );


  and

  (
    g50_p,
    rippe_adder|XX_2_p_spl_,
    rippe_adder|YY_2_p_spl_
  );


  or

  (
    g51_n,
    rippe_adder|XX_2_p_spl_,
    rippe_adder|YY_2_p_spl_
  );


  and

  (
    g52_p,
    rippe_adder|XXX_3_p_spl_,
    rippe_adder|YYY_3_p_spl_
  );


  or

  (
    g53_n,
    rippe_adder|XXX_3_p_spl_,
    rippe_adder|YYY_3_p_spl_
  );


  buf

  (
    S_0,
    rippe_adder|sS_0_p
  );


  buf

  (
    S_1,
    rippe_adder|sS_1_p
  );


  buf

  (
    S_2,
    rippe_adder|sS_2_p
  );


  buf

  (
    S_3,
    g33_p
  );


  not

  (
    Co,
    g34_p
  );


  buf

  (
    n61_li01_li01,
    X_2_p
  );


  buf

  (
    n67_li03_li03,
    X_3_p
  );


  buf

  (
    n70_li04_li04,
    rippe_adder|XX_3_p
  );


  buf

  (
    n79_li07_li07,
    Y_2_p
  );


  buf

  (
    n85_li09_li09,
    Y_3_p
  );


  buf

  (
    n88_li10_li10,
    rippe_adder|YY_3_p
  );


  buf

  (
    n94_li12_li12,
    rippe_adder|SS_0_p
  );


  buf

  (
    n97_li13_li13,
    rippe_adder|SSS_0_p
  );


  buf

  (
    n100_li14_li14,
    g37_p
  );


  buf

  (
    n103_li15_li15,
    rippe_adder|SS_1_p
  );


  buf

  (
    n106_li16_li16,
    g41_p
  );


  buf

  (
    n109_li17_li17,
    g45_p
  );


  not

  (
    n112_li18_li18,
    g35_n_spl_
  );


  not

  (
    n115_li19_li19,
    g46_p
  );


  not

  (
    n118_li20_li20,
    g47_p
  );


  buf

  (
    n87_i2,
    g48_p
  );


  buf

  (
    n88_i2,
    g49_n
  );


  buf

  (
    n93_i2,
    g50_p
  );


  buf

  (
    n94_i2,
    g51_n
  );


  buf

  (
    n77_i2,
    g52_p
  );


  buf

  (
    n78_i2,
    g53_n
  );


  buf

  (
    n77_o2_n_spl_,
    n77_o2_n
  );


  buf

  (
    g31_n_spl_,
    g31_n
  );


  buf

  (
    g35_n_spl_,
    g35_n
  );


  buf

  (
    n87_o2_n_spl_,
    n87_o2_n
  );


  buf

  (
    g39_n_spl_,
    g39_n
  );


  buf

  (
    n93_o2_n_spl_,
    n93_o2_n
  );


  buf

  (
    g43_n_spl_,
    g43_n
  );


  buf

  (
    X_1_p_spl_,
    X_1_p
  );


  buf

  (
    Y_1_p_spl_,
    Y_1_p
  );


  buf

  (
    rippe_adder|XX_2_p_spl_,
    rippe_adder|XX_2_p
  );


  buf

  (
    rippe_adder|YY_2_p_spl_,
    rippe_adder|YY_2_p
  );


  buf

  (
    rippe_adder|XXX_3_p_spl_,
    rippe_adder|XXX_3_p
  );


  buf

  (
    rippe_adder|YYY_3_p_spl_,
    rippe_adder|YYY_3_p
  );


endmodule
