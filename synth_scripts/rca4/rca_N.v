
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
  rippe_adder|xw1,
  rippe_adder|xw2,
  rippe_adder|xw3,
  S_0,
  S_1,
  S_2,
  S_3,
  Co,
  n34_li0_li0,
  n37_li1_li1,
  n40_li2_li2
);

  input X_0;input Y_0;input X_1;input Y_1;input X_2;input Y_2;input X_3;input Y_3;input rippe_adder|xw1;input rippe_adder|xw2;input rippe_adder|xw3;
  output S_0;output S_1;output S_2;output S_3;output Co;output n34_li0_li0;output n37_li1_li1;output n40_li2_li2;
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
  wire rippe_adder|xw1_p;
  wire rippe_adder|xw1_n;
  wire rippe_adder|xw2_p;
  wire rippe_adder|xw2_n;
  wire rippe_adder|xw3_p;
  wire rippe_adder|xw3_n;
  wire g12_p;
  wire g12_n;
  wire g13_p;
  wire g13_n;
  wire g14_p;
  wire g14_n;
  wire g15_p;
  wire g15_n;
  wire g16_p;
  wire g16_n;
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
  wire g12_n_spl_;
  wire X_1_p_spl_;
  wire Y_1_p_spl_;
  wire X_1_n_spl_;
  wire Y_1_n_spl_;
  wire g15_n_spl_;
  wire g18_n_spl_;
  wire X_2_p_spl_;
  wire Y_2_p_spl_;
  wire X_2_n_spl_;
  wire Y_2_n_spl_;
  wire g21_n_spl_;
  wire g24_n_spl_;
  wire X_3_p_spl_;
  wire Y_3_p_spl_;
  wire X_3_n_spl_;
  wire Y_3_n_spl_;
  wire g27_n_spl_;
  wire g30_n_spl_;

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


  or

  (
    g12_n,
    X_0_n,
    Y_0_n
  );


  or

  (
    g13_n,
    X_0_p,
    Y_0_p
  );


  and

  (
    g14_p,
    g12_n_spl_,
    g13_n
  );


  and

  (
    g15_p,
    X_1_p_spl_,
    Y_1_p_spl_
  );


  or

  (
    g15_n,
    X_1_n_spl_,
    Y_1_n_spl_
  );


  and

  (
    g16_p,
    X_1_n_spl_,
    Y_1_n_spl_
  );


  or

  (
    g16_n,
    X_1_p_spl_,
    Y_1_p_spl_
  );


  and

  (
    g17_p,
    g15_n_spl_,
    g16_n
  );


  or

  (
    g17_n,
    g15_p,
    g16_p
  );


  or

  (
    g18_n,
    rippe_adder|xw1_n,
    g17_n
  );


  or

  (
    g19_n,
    rippe_adder|xw1_p,
    g17_p
  );


  and

  (
    g20_p,
    g18_n_spl_,
    g19_n
  );


  and

  (
    g21_p,
    X_2_p_spl_,
    Y_2_p_spl_
  );


  or

  (
    g21_n,
    X_2_n_spl_,
    Y_2_n_spl_
  );


  and

  (
    g22_p,
    X_2_n_spl_,
    Y_2_n_spl_
  );


  or

  (
    g22_n,
    X_2_p_spl_,
    Y_2_p_spl_
  );


  and

  (
    g23_p,
    g21_n_spl_,
    g22_n
  );


  or

  (
    g23_n,
    g21_p,
    g22_p
  );


  or

  (
    g24_n,
    rippe_adder|xw2_n,
    g23_n
  );


  or

  (
    g25_n,
    rippe_adder|xw2_p,
    g23_p
  );


  and

  (
    g26_p,
    g24_n_spl_,
    g25_n
  );


  and

  (
    g27_p,
    X_3_p_spl_,
    Y_3_p_spl_
  );


  or

  (
    g27_n,
    X_3_n_spl_,
    Y_3_n_spl_
  );


  and

  (
    g28_p,
    X_3_n_spl_,
    Y_3_n_spl_
  );


  or

  (
    g28_n,
    X_3_p_spl_,
    Y_3_p_spl_
  );


  and

  (
    g29_p,
    g27_n_spl_,
    g28_n
  );


  or

  (
    g29_n,
    g27_p,
    g28_p
  );


  or

  (
    g30_n,
    rippe_adder|xw3_n,
    g29_n
  );


  or

  (
    g31_n,
    rippe_adder|xw3_p,
    g29_p
  );


  and

  (
    g32_p,
    g30_n_spl_,
    g31_n
  );


  and

  (
    g33_p,
    g27_n_spl_,
    g30_n_spl_
  );


  and

  (
    g34_p,
    g15_n_spl_,
    g18_n_spl_
  );


  and

  (
    g35_p,
    g21_n_spl_,
    g24_n_spl_
  );


  buf

  (
    S_0,
    g14_p
  );


  buf

  (
    S_1,
    g20_p
  );


  buf

  (
    S_2,
    g26_p
  );


  buf

  (
    S_3,
    g32_p
  );


  not

  (
    Co,
    g33_p
  );


  not

  (
    n34_li0_li0,
    g12_n_spl_
  );


  not

  (
    n37_li1_li1,
    g34_p
  );


  not

  (
    n40_li2_li2,
    g35_p
  );


  buf

  (
    g12_n_spl_,
    g12_n
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
    X_1_n_spl_,
    X_1_n
  );


  buf

  (
    Y_1_n_spl_,
    Y_1_n
  );


  buf

  (
    g15_n_spl_,
    g15_n
  );


  buf

  (
    g18_n_spl_,
    g18_n
  );


  buf

  (
    X_2_p_spl_,
    X_2_p
  );


  buf

  (
    Y_2_p_spl_,
    Y_2_p
  );


  buf

  (
    X_2_n_spl_,
    X_2_n
  );


  buf

  (
    Y_2_n_spl_,
    Y_2_n
  );


  buf

  (
    g21_n_spl_,
    g21_n
  );


  buf

  (
    g24_n_spl_,
    g24_n
  );


  buf

  (
    X_3_p_spl_,
    X_3_p
  );


  buf

  (
    Y_3_p_spl_,
    Y_3_p
  );


  buf

  (
    X_3_n_spl_,
    X_3_n
  );


  buf

  (
    Y_3_n_spl_,
    Y_3_n
  );


  buf

  (
    g27_n_spl_,
    g27_n
  );


  buf

  (
    g30_n_spl_,
    g30_n
  );


endmodule
