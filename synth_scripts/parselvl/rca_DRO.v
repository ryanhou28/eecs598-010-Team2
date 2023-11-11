
module mymod
(
  X_0_p,
  X_0_n,
  Y_0_p,
  Y_0_n,
  X_1_p,
  X_1_n,
  Y_1_p,
  Y_1_n,
  X_2_p,
  X_2_n,
  Y_2_p,
  Y_2_n,
  X_3_p,
  X_3_n,
  Y_3_p,
  Y_3_n,
  S_0_p,
  S_1_p,
  S_2_p,
  S_3_p,
  Co_n
);

  input X_0_p;input X_0_n;input Y_0_p;input Y_0_n;input X_1_p;input X_1_n;input Y_1_p;input Y_1_n;input X_2_p;input X_2_n;input Y_2_p;input Y_2_n;input X_3_p;input X_3_n;input Y_3_p;input Y_3_n;
  output S_0_p;output S_1_p;output S_2_p;output S_3_p;output Co_n;
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
  wire ffc_0_p;
  wire ffc_0_n;
  wire ffc_1_p;
  wire ffc_1_n;
  wire ffc_2_p;
  wire ffc_2_n;
  wire ffc_3_p;
  wire ffc_3_n;
  wire ffc_4_p;
  wire ffc_4_n;
  wire ffc_5_p;
  wire ffc_5_n;
  wire ffc_6_p;
  wire ffc_6_n;
  wire ffc_7_p;
  wire ffc_7_n;
  wire ffc_8_p;
  wire ffc_8_n;
  wire ffc_9_p;
  wire ffc_9_n;
  wire ffc_10_p;
  wire ffc_10_n;
  wire ffc_11_p;
  wire ffc_11_n;
  wire ffc_12_p;
  wire ffc_12_n;
  wire ffc_13_p;
  wire ffc_13_n;
  wire ffc_14_p;
  wire ffc_14_n;
  wire ffc_15_p;
  wire ffc_15_n;
  wire ffc_16_p;
  wire ffc_16_n;
  wire ffc_17_p;
  wire ffc_17_n;
  wire ffc_18_p;
  wire ffc_18_n;
  wire ffc_19_p;
  wire ffc_19_n;
  wire ffc_20_p;
  wire ffc_20_n;
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
  wire ffc_19_n_spl_;
  wire g31_n_spl_;
  wire g35_n_spl_;
  wire ffc_15_n_spl_;
  wire g39_n_spl_;
  wire ffc_17_n_spl_;
  wire g43_n_spl_;
  wire X_1_p_spl_;
  wire Y_1_p_spl_;
  wire ffc_0_p_spl_;
  wire ffc_3_p_spl_;
  wire ffc_2_p_spl_;
  wire ffc_5_p_spl_;

  LA
  g_g30_p
  (
    .dout(g30_p),
    .din1(ffc_19_n_spl_),
    .din2(ffc_20_p)
  );


  FA
  g_g30_n
  (
    .dout(g30_n),
    .din1(ffc_19_p),
    .din2(ffc_20_n)
  );


  FA
  g_g31_n
  (
    .dout(g31_n),
    .din1(ffc_14_n),
    .din2(g30_n)
  );


  FA
  g_g32_n
  (
    .dout(g32_n),
    .din1(ffc_14_p),
    .din2(g30_p)
  );


  LA
  g_g33_p
  (
    .dout(g33_p),
    .din1(g31_n_spl_),
    .din2(g32_n)
  );


  LA
  g_g34_p
  (
    .dout(g34_p),
    .din1(ffc_19_n_spl_),
    .din2(g31_n_spl_)
  );


  FA
  g_g35_n
  (
    .dout(g35_n),
    .din1(X_0_n),
    .din2(Y_0_n)
  );


  FA
  g_g36_n
  (
    .dout(g36_n),
    .din1(X_0_p),
    .din2(Y_0_p)
  );


  LA
  g_g37_p
  (
    .dout(g37_p),
    .din1(g35_n_spl_),
    .din2(g36_n)
  );


  LA
  g_g38_p
  (
    .dout(g38_p),
    .din1(ffc_15_n_spl_),
    .din2(ffc_16_p)
  );


  FA
  g_g38_n
  (
    .dout(g38_n),
    .din1(ffc_15_p),
    .din2(ffc_16_n)
  );


  FA
  g_g39_n
  (
    .dout(g39_n),
    .din1(ffc_12_n),
    .din2(g38_n)
  );


  FA
  g_g40_n
  (
    .dout(g40_n),
    .din1(ffc_12_p),
    .din2(g38_p)
  );


  LA
  g_g41_p
  (
    .dout(g41_p),
    .din1(g39_n_spl_),
    .din2(g40_n)
  );


  LA
  g_g42_p
  (
    .dout(g42_p),
    .din1(ffc_17_n_spl_),
    .din2(ffc_18_p)
  );


  FA
  g_g42_n
  (
    .dout(g42_n),
    .din1(ffc_17_p),
    .din2(ffc_18_n)
  );


  FA
  g_g43_n
  (
    .dout(g43_n),
    .din1(ffc_13_n),
    .din2(g42_n)
  );


  FA
  g_g44_n
  (
    .dout(g44_n),
    .din1(ffc_13_p),
    .din2(g42_p)
  );


  LA
  g_g45_p
  (
    .dout(g45_p),
    .din1(g43_n_spl_),
    .din2(g44_n)
  );


  LA
  g_g46_p
  (
    .dout(g46_p),
    .din1(ffc_15_n_spl_),
    .din2(g39_n_spl_)
  );


  LA
  g_g47_p
  (
    .dout(g47_p),
    .din1(ffc_17_n_spl_),
    .din2(g43_n_spl_)
  );


  LA
  g_g48_p
  (
    .dout(g48_p),
    .din1(X_1_p_spl_),
    .din2(Y_1_p_spl_)
  );


  FA
  g_g49_n
  (
    .dout(g49_n),
    .din1(X_1_p_spl_),
    .din2(Y_1_p_spl_)
  );


  LA
  g_g50_p
  (
    .dout(g50_p),
    .din1(ffc_0_p_spl_),
    .din2(ffc_3_p_spl_)
  );


  FA
  g_g51_n
  (
    .dout(g51_n),
    .din1(ffc_0_p_spl_),
    .din2(ffc_3_p_spl_)
  );


  LA
  g_g52_p
  (
    .dout(g52_p),
    .din1(ffc_2_p_spl_),
    .din2(ffc_5_p_spl_)
  );


  FA
  g_g53_n
  (
    .dout(g53_n),
    .din1(ffc_2_p_spl_),
    .din2(ffc_5_p_spl_)
  );


  buf

  (
    S_0_p,
    ffc_6_p
  );


  buf

  (
    S_1_p,
    ffc_9_p
  );


  buf

  (
    S_2_p,
    ffc_11_p
  );


  buf

  (
    S_3_p,
    g33_p
  );


  buf

  (
    Co_n,
    g34_p
  );


  DROC
  ffc_0_0
  (
    .doutp(ffc_0_p),
    .doutn(ffc_0_n),
    .din(X_2_p)
  );


  DROC
  ffc_1_0
  (
    .doutp(ffc_1_p),
    .doutn(ffc_1_n),
    .din(X_3_p)
  );


  DROC
  ffc_2_1
  (
    .doutp(ffc_2_p),
    .doutn(ffc_2_n),
    .din(ffc_1_p)
  );


  DROC
  ffc_3_0
  (
    .doutp(ffc_3_p),
    .doutn(ffc_3_n),
    .din(Y_2_p)
  );


  DROC
  ffc_4_0
  (
    .doutp(ffc_4_p),
    .doutn(ffc_4_n),
    .din(Y_3_p)
  );


  DROC
  ffc_5_1
  (
    .doutp(ffc_5_p),
    .doutn(ffc_5_n),
    .din(ffc_4_p)
  );


  DROC
  ffc_6_2
  (
    .doutp(ffc_6_p),
    .doutn(ffc_6_n),
    .din(ffc_7_p)
  );


  DROC
  ffc_7_1
  (
    .doutp(ffc_7_p),
    .doutn(ffc_7_n),
    .din(ffc_8_p)
  );


  DROC
  ffc_8_0
  (
    .doutp(ffc_8_p),
    .doutn(ffc_8_n),
    .din(g37_p)
  );


  DROC
  ffc_9_2
  (
    .doutp(ffc_9_p),
    .doutn(ffc_9_n),
    .din(ffc_10_p)
  );


  DROC
  ffc_10_1
  (
    .doutp(ffc_10_p),
    .doutn(ffc_10_n),
    .din(g41_p)
  );


  DROC
  ffc_11_2
  (
    .doutp(ffc_11_p),
    .doutn(ffc_11_n),
    .din(g45_p)
  );


  DROC
  ffc_12_0
  (
    .doutp(ffc_12_n),
    .doutn(ffc_12_p),
    .din(g35_n_spl_)
  );


  DROC
  ffc_13_1
  (
    .doutp(ffc_13_n),
    .doutn(ffc_13_p),
    .din(g46_p)
  );


  DROC
  ffc_14_2
  (
    .doutp(ffc_14_n),
    .doutn(ffc_14_p),
    .din(g47_p)
  );


  DROC
  ffc_15_0
  (
    .doutp(ffc_15_p),
    .doutn(ffc_15_n),
    .din(g48_p)
  );


  DROC
  ffc_16_0
  (
    .doutp(ffc_16_p),
    .doutn(ffc_16_n),
    .din(g49_n)
  );


  DROC
  ffc_17_1
  (
    .doutp(ffc_17_p),
    .doutn(ffc_17_n),
    .din(g50_p)
  );


  DROC
  ffc_18_1
  (
    .doutp(ffc_18_p),
    .doutn(ffc_18_n),
    .din(g51_n)
  );


  DROC
  ffc_19_2
  (
    .doutp(ffc_19_p),
    .doutn(ffc_19_n),
    .din(g52_p)
  );


  DROC
  ffc_20_2
  (
    .doutp(ffc_20_p),
    .doutn(ffc_20_n),
    .din(g53_n)
  );


  buf

  (
    ffc_19_n_spl_,
    ffc_19_n
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
    ffc_15_n_spl_,
    ffc_15_n
  );


  buf

  (
    g39_n_spl_,
    g39_n
  );


  buf

  (
    ffc_17_n_spl_,
    ffc_17_n
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
    ffc_0_p_spl_,
    ffc_0_p
  );


  buf

  (
    ffc_3_p_spl_,
    ffc_3_p
  );


  buf

  (
    ffc_2_p_spl_,
    ffc_2_p
  );


  buf

  (
    ffc_5_p_spl_,
    ffc_5_p
  );


endmodule
