
module crca_XS
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

  LA
  #("g_g9_p") g_g9_p
  (
    .dout(g9_p),
    .din1(X_0_p_spl_),
    .din2(Y_0_p_spl_)
  );


  FA
  #("g_g9_n") g_g9_n
  (
    .dout(g9_n),
    .din1(X_0_n),
    .din2(Y_0_n)
  );


  FA
  #("g_g10_n") g_g10_n
  (
    .dout(g10_n),
    .din1(X_0_p_spl_),
    .din2(Y_0_p_spl_)
  );


  LA
  #("g_g11_p") g_g11_p
  (
    .dout(g11_p),
    .din1(g9_n_spl_),
    .din2(g10_n)
  );


  LA
  #("g_g12_p") g_g12_p
  (
    .dout(g12_p),
    .din1(X_1_p_spl_),
    .din2(Y_1_p_spl_)
  );


  FA
  #("g_g12_n") g_g12_n
  (
    .dout(g12_n),
    .din1(X_1_n_spl_),
    .din2(Y_1_n_spl_)
  );


  LA
  #("g_g13_p") g_g13_p
  (
    .dout(g13_p),
    .din1(X_1_n_spl_),
    .din2(Y_1_n_spl_)
  );


  FA
  #("g_g13_n") g_g13_n
  (
    .dout(g13_n),
    .din1(X_1_p_spl_),
    .din2(Y_1_p_spl_)
  );


  LA
  #("g_g14_p") g_g14_p
  (
    .dout(g14_p),
    .din1(g12_n_spl_),
    .din2(g13_n)
  );


  FA
  #("g_g14_n") g_g14_n
  (
    .dout(g14_n),
    .din1(g12_p_spl_),
    .din2(g13_p)
  );


  LA
  #("g_g15_p") g_g15_p
  (
    .dout(g15_p),
    .din1(g9_p_spl_),
    .din2(g14_p_spl_)
  );


  FA
  #("g_g15_n") g_g15_n
  (
    .dout(g15_n),
    .din1(g9_n_spl_),
    .din2(g14_n)
  );


  FA
  #("g_g16_n") g_g16_n
  (
    .dout(g16_n),
    .din1(g9_p_spl_),
    .din2(g14_p_spl_)
  );


  LA
  #("g_g17_p") g_g17_p
  (
    .dout(g17_p),
    .din1(g15_n_spl_),
    .din2(g16_n)
  );


  LA
  #("g_g18_p") g_g18_p
  (
    .dout(g18_p),
    .din1(g12_n_spl_),
    .din2(g15_n_spl_)
  );


  FA
  #("g_g18_n") g_g18_n
  (
    .dout(g18_n),
    .din1(g12_p_spl_),
    .din2(g15_p)
  );


  LA
  #("g_g19_p") g_g19_p
  (
    .dout(g19_p),
    .din1(X_2_p_spl_),
    .din2(Y_2_p_spl_)
  );


  FA
  #("g_g19_n") g_g19_n
  (
    .dout(g19_n),
    .din1(X_2_n_spl_),
    .din2(Y_2_n_spl_)
  );


  LA
  #("g_g20_p") g_g20_p
  (
    .dout(g20_p),
    .din1(X_2_n_spl_),
    .din2(Y_2_n_spl_)
  );


  FA
  #("g_g20_n") g_g20_n
  (
    .dout(g20_n),
    .din1(X_2_p_spl_),
    .din2(Y_2_p_spl_)
  );


  LA
  #("g_g21_p") g_g21_p
  (
    .dout(g21_p),
    .din1(g19_n_spl_),
    .din2(g20_n)
  );


  FA
  #("g_g21_n") g_g21_n
  (
    .dout(g21_n),
    .din1(g19_p_spl_),
    .din2(g20_p)
  );


  LA
  #("g_g22_p") g_g22_p
  (
    .dout(g22_p),
    .din1(g18_n_spl_),
    .din2(g21_p_spl_)
  );


  FA
  #("g_g22_n") g_g22_n
  (
    .dout(g22_n),
    .din1(g18_p),
    .din2(g21_n)
  );


  FA
  #("g_g23_n") g_g23_n
  (
    .dout(g23_n),
    .din1(g18_n_spl_),
    .din2(g21_p_spl_)
  );


  LA
  #("g_g24_p") g_g24_p
  (
    .dout(g24_p),
    .din1(g22_n_spl_),
    .din2(g23_n)
  );


  LA
  #("g_g25_p") g_g25_p
  (
    .dout(g25_p),
    .din1(g19_n_spl_),
    .din2(g22_n_spl_)
  );


  FA
  #("g_g25_n") g_g25_n
  (
    .dout(g25_n),
    .din1(g19_p_spl_),
    .din2(g22_p)
  );


  LA
  #("g_g26_p") g_g26_p
  (
    .dout(g26_p),
    .din1(X_3_p_spl_),
    .din2(Y_3_p_spl_)
  );


  FA
  #("g_g26_n") g_g26_n
  (
    .dout(g26_n),
    .din1(X_3_n_spl_),
    .din2(Y_3_n_spl_)
  );


  LA
  #("g_g27_p") g_g27_p
  (
    .dout(g27_p),
    .din1(X_3_n_spl_),
    .din2(Y_3_n_spl_)
  );


  FA
  #("g_g27_n") g_g27_n
  (
    .dout(g27_n),
    .din1(X_3_p_spl_),
    .din2(Y_3_p_spl_)
  );


  LA
  #("g_g28_p") g_g28_p
  (
    .dout(g28_p),
    .din1(g26_n_spl_),
    .din2(g27_n)
  );


  FA
  #("g_g28_n") g_g28_n
  (
    .dout(g28_n),
    .din1(g26_p),
    .din2(g27_p)
  );


  FA
  #("g_g29_n") g_g29_n
  (
    .dout(g29_n),
    .din1(g25_p),
    .din2(g28_n)
  );


  FA
  #("g_g30_n") g_g30_n
  (
    .dout(g30_n),
    .din1(g25_n),
    .din2(g28_p)
  );


  LA
  #("g_g31_p") g_g31_p
  (
    .dout(g31_p),
    .din1(g29_n_spl_),
    .din2(g30_n)
  );


  LA
  #("g_g32_p") g_g32_p
  (
    .dout(g32_p),
    .din1(g26_n_spl_),
    .din2(g29_n_spl_)
  );


  buf

  (
    S_0_p,
    g11_p
  );


  buf

  (
    S_1_p,
    g17_p
  );


  buf

  (
    S_2_p,
    g24_p
  );


  buf

  (
    S_3_p,
    g31_p
  );


  buf

  (
    Co_n,
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
