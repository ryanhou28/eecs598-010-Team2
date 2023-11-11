
module mymod
(
  G1_p,
  G1_n,
  G2_p,
  G2_n,
  G3_p,
  G3_n,
  G4_p,
  G4_n,
  G5_p,
  G5_n,
  G16_n,
  G17_n
);

  input G1_p;input G1_n;input G2_p;input G2_n;input G3_p;input G3_n;input G4_p;input G4_n;input G5_p;input G5_n;
  output G16_n;output G17_n;
  wire G1_p;
  wire G1_n;
  wire G2_p;
  wire G2_n;
  wire G3_p;
  wire G3_n;
  wire G4_p;
  wire G4_n;
  wire G5_p;
  wire G5_n;
  wire g6_p;
  wire g6_n;
  wire g7_p;
  wire g7_n;
  wire g8_p;
  wire g8_n;
  wire g9_p;
  wire g9_n;
  wire g10_p;
  wire g10_n;
  wire g11_p;
  wire g11_n;
  wire g7_p_spl_;
  wire g8_n_spl_;

  FA
  g_g6_n
  (
    .dout(g6_n),
    .din1(G1_n),
    .din2(G3_n)
  );


  LA
  g_g7_p
  (
    .dout(g7_p),
    .din1(G3_p),
    .din2(G4_p)
  );


  FA
  g_g8_n
  (
    .dout(g8_n),
    .din1(G2_n),
    .din2(g7_p_spl_)
  );


  LA
  g_g9_p
  (
    .dout(g9_p),
    .din1(g6_n),
    .din2(g8_n_spl_)
  );


  FA
  g_g10_n
  (
    .dout(g10_n),
    .din1(G5_n),
    .din2(g7_p_spl_)
  );


  LA
  g_g11_p
  (
    .dout(g11_p),
    .din1(g8_n_spl_),
    .din2(g10_n)
  );


  buf

  (
    G16_n,
    g9_p
  );


  buf

  (
    G17_n,
    g11_p
  );


  buf

  (
    g7_p_spl_,
    g7_p
  );


  buf

  (
    g8_n_spl_,
    g8_n
  );


endmodule
