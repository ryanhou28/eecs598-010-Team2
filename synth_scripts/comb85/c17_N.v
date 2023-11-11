
module mymod
(
  G1,
  G2,
  G3,
  G4,
  G5,
  G16,
  G17
);

  input G1;input G2;input G3;input G4;input G5;
  output G16;output G17;
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

  buf

  (
    G1_p,
    G1
  );


  not

  (
    G1_n,
    G1
  );


  buf

  (
    G2_p,
    G2
  );


  not

  (
    G2_n,
    G2
  );


  buf

  (
    G3_p,
    G3
  );


  not

  (
    G3_n,
    G3
  );


  buf

  (
    G4_p,
    G4
  );


  not

  (
    G4_n,
    G4
  );


  buf

  (
    G5_p,
    G5
  );


  not

  (
    G5_n,
    G5
  );


  or

  (
    g6_n,
    G1_n,
    G3_n
  );


  and

  (
    g7_p,
    G3_p,
    G4_p
  );


  or

  (
    g8_n,
    G2_n,
    g7_p_spl_
  );


  and

  (
    g9_p,
    g6_n,
    g8_n_spl_
  );


  or

  (
    g10_n,
    G5_n,
    g7_p_spl_
  );


  and

  (
    g11_p,
    g8_n_spl_,
    g10_n
  );


  not

  (
    G16,
    g9_p
  );


  not

  (
    G17,
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
