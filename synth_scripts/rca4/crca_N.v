
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
  S_0,
  S_1,
  S_2,
  S_3,
  Co
);

  input X_0;input Y_0;input X_1;input Y_1;input X_2;input Y_2;input X_3;input Y_3;
  output S_0;output S_1;output S_2;output S_3;output Co;
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
  wire g9_p;
  wire g9_n;
  wire g10_p;
  wire g10_n;
  wire g11_p;
  wire g11_n;
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
  wire X_0_p_spl_;
  wire Y_0_p_spl_;
  wire g9_n_spl_;
  wire X_1_p_spl_;
  wire Y_1_p_spl_;
  wire X_1_n_spl_;
  wire Y_1_n_spl_;
  wire g12_n_spl_;
  wire g12_p_spl_;
  wire g9_p_spl_;
  wire g14_p_spl_;
  wire g15_n_spl_;
  wire X_2_p_spl_;
  wire Y_2_p_spl_;
  wire X_2_n_spl_;
  wire Y_2_n_spl_;
  wire g19_n_spl_;
  wire g19_p_spl_;
  wire g18_n_spl_;
  wire g21_p_spl_;
  wire g22_n_spl_;
  wire X_3_p_spl_;
  wire Y_3_p_spl_;
  wire X_3_n_spl_;
  wire Y_3_n_spl_;
  wire g26_n_spl_;
  wire g29_n_spl_;

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


  and

  (
    g9_p,
    X_0_p_spl_,
    Y_0_p_spl_
  );


  or

  (
    g9_n,
    X_0_n,
    Y_0_n
  );


  or

  (
    g10_n,
    X_0_p_spl_,
    Y_0_p_spl_
  );


  and

  (
    g11_p,
    g9_n_spl_,
    g10_n
  );


  and

  (
    g12_p,
    X_1_p_spl_,
    Y_1_p_spl_
  );


  or

  (
    g12_n,
    X_1_n_spl_,
    Y_1_n_spl_
  );


  and

  (
    g13_p,
    X_1_n_spl_,
    Y_1_n_spl_
  );


  or

  (
    g13_n,
    X_1_p_spl_,
    Y_1_p_spl_
  );


  and

  (
    g14_p,
    g12_n_spl_,
    g13_n
  );


  or

  (
    g14_n,
    g12_p_spl_,
    g13_p
  );


  and

  (
    g15_p,
    g9_p_spl_,
    g14_p_spl_
  );


  or

  (
    g15_n,
    g9_n_spl_,
    g14_n
  );


  or

  (
    g16_n,
    g9_p_spl_,
    g14_p_spl_
  );


  and

  (
    g17_p,
    g15_n_spl_,
    g16_n
  );


  and

  (
    g18_p,
    g12_n_spl_,
    g15_n_spl_
  );


  or

  (
    g18_n,
    g12_p_spl_,
    g15_p
  );


  and

  (
    g19_p,
    X_2_p_spl_,
    Y_2_p_spl_
  );


  or

  (
    g19_n,
    X_2_n_spl_,
    Y_2_n_spl_
  );


  and

  (
    g20_p,
    X_2_n_spl_,
    Y_2_n_spl_
  );


  or

  (
    g20_n,
    X_2_p_spl_,
    Y_2_p_spl_
  );


  and

  (
    g21_p,
    g19_n_spl_,
    g20_n
  );


  or

  (
    g21_n,
    g19_p_spl_,
    g20_p
  );


  and

  (
    g22_p,
    g18_n_spl_,
    g21_p_spl_
  );


  or

  (
    g22_n,
    g18_p,
    g21_n
  );


  or

  (
    g23_n,
    g18_n_spl_,
    g21_p_spl_
  );


  and

  (
    g24_p,
    g22_n_spl_,
    g23_n
  );


  and

  (
    g25_p,
    g19_n_spl_,
    g22_n_spl_
  );


  or

  (
    g25_n,
    g19_p_spl_,
    g22_p
  );


  and

  (
    g26_p,
    X_3_p_spl_,
    Y_3_p_spl_
  );


  or

  (
    g26_n,
    X_3_n_spl_,
    Y_3_n_spl_
  );


  and

  (
    g27_p,
    X_3_n_spl_,
    Y_3_n_spl_
  );


  or

  (
    g27_n,
    X_3_p_spl_,
    Y_3_p_spl_
  );


  and

  (
    g28_p,
    g26_n_spl_,
    g27_n
  );


  or

  (
    g28_n,
    g26_p,
    g27_p
  );


  or

  (
    g29_n,
    g25_p,
    g28_n
  );


  or

  (
    g30_n,
    g25_n,
    g28_p
  );


  and

  (
    g31_p,
    g29_n_spl_,
    g30_n
  );


  and

  (
    g32_p,
    g26_n_spl_,
    g29_n_spl_
  );


  buf

  (
    S_0,
    g11_p
  );


  buf

  (
    S_1,
    g17_p
  );


  buf

  (
    S_2,
    g24_p
  );


  buf

  (
    S_3,
    g31_p
  );


  not

  (
    Co,
    g32_p
  );


  buf

  (
    X_0_p_spl_,
    X_0_p
  );


  buf

  (
    Y_0_p_spl_,
    Y_0_p
  );


  buf

  (
    g9_n_spl_,
    g9_n
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
    g12_n_spl_,
    g12_n
  );


  buf

  (
    g12_p_spl_,
    g12_p
  );


  buf

  (
    g9_p_spl_,
    g9_p
  );


  buf

  (
    g14_p_spl_,
    g14_p
  );


  buf

  (
    g15_n_spl_,
    g15_n
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
    g18_n_spl_,
    g18_n
  );


  buf

  (
    g21_p_spl_,
    g21_p
  );


  buf

  (
    g22_n_spl_,
    g22_n
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
    g26_n_spl_,
    g26_n
  );


  buf

  (
    g29_n_spl_,
    g29_n
  );


endmodule
