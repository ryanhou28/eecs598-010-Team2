
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

  orX
  g_g12_n
  (
    .dout(g12_n),
    .din1(X_0_n),
    .din2(Y_0_n)
  );


  orX
  g_g13_n
  (
    .dout(g13_n),
    .din1(X_0_p),
    .din2(Y_0_p)
  );


  andX
  g_g14_p
  (
    .dout(g14_p),
    .din1(g12_n_spl_),
    .din2(g13_n)
  );


  andX
  g_g15_p
  (
    .dout(g15_p),
    .din1(X_1_p_spl_),
    .din2(Y_1_p_spl_)
  );


  orX
  g_g15_n
  (
    .dout(g15_n),
    .din1(X_1_n_spl_),
    .din2(Y_1_n_spl_)
  );


  andX
  g_g16_p
  (
    .dout(g16_p),
    .din1(X_1_n_spl_),
    .din2(Y_1_n_spl_)
  );


  orX
  g_g16_n
  (
    .dout(g16_n),
    .din1(X_1_p_spl_),
    .din2(Y_1_p_spl_)
  );


  andX
  g_g17_p
  (
    .dout(g17_p),
    .din1(g15_n_spl_),
    .din2(g16_n)
  );


  orX
  g_g17_n
  (
    .dout(g17_n),
    .din1(g15_p),
    .din2(g16_p)
  );


  orX
  g_g18_n
  (
    .dout(g18_n),
    .din1(ffc_0_n),
    .din2(g17_n)
  );


  orX
  g_g19_n
  (
    .dout(g19_n),
    .din1(ffc_0_p),
    .din2(g17_p)
  );


  andX
  g_g20_p
  (
    .dout(g20_p),
    .din1(g18_n_spl_),
    .din2(g19_n)
  );


  andX
  g_g21_p
  (
    .dout(g21_p),
    .din1(X_2_p_spl_),
    .din2(Y_2_p_spl_)
  );


  orX
  g_g21_n
  (
    .dout(g21_n),
    .din1(X_2_n_spl_),
    .din2(Y_2_n_spl_)
  );


  andX
  g_g22_p
  (
    .dout(g22_p),
    .din1(X_2_n_spl_),
    .din2(Y_2_n_spl_)
  );


  orX
  g_g22_n
  (
    .dout(g22_n),
    .din1(X_2_p_spl_),
    .din2(Y_2_p_spl_)
  );


  andX
  g_g23_p
  (
    .dout(g23_p),
    .din1(g21_n_spl_),
    .din2(g22_n)
  );


  orX
  g_g23_n
  (
    .dout(g23_n),
    .din1(g21_p),
    .din2(g22_p)
  );


  orX
  g_g24_n
  (
    .dout(g24_n),
    .din1(ffc_1_n),
    .din2(g23_n)
  );


  orX
  g_g25_n
  (
    .dout(g25_n),
    .din1(ffc_1_p),
    .din2(g23_p)
  );


  andX
  g_g26_p
  (
    .dout(g26_p),
    .din1(g24_n_spl_),
    .din2(g25_n)
  );


  andX
  g_g27_p
  (
    .dout(g27_p),
    .din1(X_3_p_spl_),
    .din2(Y_3_p_spl_)
  );


  orX
  g_g27_n
  (
    .dout(g27_n),
    .din1(X_3_n_spl_),
    .din2(Y_3_n_spl_)
  );


  andX
  g_g28_p
  (
    .dout(g28_p),
    .din1(X_3_n_spl_),
    .din2(Y_3_n_spl_)
  );


  orX
  g_g28_n
  (
    .dout(g28_n),
    .din1(X_3_p_spl_),
    .din2(Y_3_p_spl_)
  );


  andX
  g_g29_p
  (
    .dout(g29_p),
    .din1(g27_n_spl_),
    .din2(g28_n)
  );


  orX
  g_g29_n
  (
    .dout(g29_n),
    .din1(g27_p),
    .din2(g28_p)
  );


  orX
  g_g30_n
  (
    .dout(g30_n),
    .din1(ffc_2_n),
    .din2(g29_n)
  );


  orX
  g_g31_n
  (
    .dout(g31_n),
    .din1(ffc_2_p),
    .din2(g29_p)
  );


  andX
  g_g32_p
  (
    .dout(g32_p),
    .din1(g30_n_spl_),
    .din2(g31_n)
  );


  andX
  g_g33_p
  (
    .dout(g33_p),
    .din1(g27_n_spl_),
    .din2(g30_n_spl_)
  );


  andX
  g_g34_p
  (
    .dout(g34_p),
    .din1(g15_n_spl_),
    .din2(g18_n_spl_)
  );


  andX
  g_g35_p
  (
    .dout(g35_p),
    .din1(g21_n_spl_),
    .din2(g24_n_spl_)
  );


  buf

  (
    S_0_p,
    g14_p
  );


  buf

  (
    S_1_p,
    g20_p
  );


  buf

  (
    S_2_p,
    g26_p
  );


  buf

  (
    S_3_p,
    g32_p
  );


  buf

  (
    Co_n,
    g33_p
  );


  DROC
  ffc_0
  (
    .doutp(ffc_0_n),
    .doutn(ffc_0_p),
    .din(g12_n_spl_)
  );


  DROC
  ffc_1
  (
    .doutp(ffc_1_n),
    .doutn(ffc_1_p),
    .din(g34_p)
  );


  DROC
  ffc_2
  (
    .doutp(ffc_2_n),
    .doutn(ffc_2_p),
    .din(g35_p)
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
