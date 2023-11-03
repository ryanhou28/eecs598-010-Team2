
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
  wire new_n8_;wire new_n9_;wire new_n10_;wire new_n12_;
  wire G3_spl_;
  wire new_n9__spl_;
  wire new_n10__spl_;

  and1
  g0
  (
    .dina(G1),
    .dinb(G3_spl_),
    .dout(new_n8_)
  );


  and1
  g1
  (
    .dina(G3_spl_),
    .dinb(G4),
    .dout(new_n9_)
  );


  anb2
  g2
  (
    .dina(new_n9__spl_),
    .dinb(G2),
    .dout(new_n10_)
  );


  anb2
  g3
  (
    .dina(new_n8_),
    .dinb(new_n10__spl_),
    .dout(G16)
  );


  anb1
  g4
  (
    .dina(G5),
    .dinb(new_n9__spl_),
    .dout(new_n12_)
  );


  nab2
  g5
  (
    .dina(new_n10__spl_),
    .dinb(new_n12_),
    .dout(G17)
  );


  splt
  gG3
  (
    .dout(G3_spl_),
    .din(G3)
  );


  splt
  gnew_n9_
  (
    .dout(new_n9__spl_),
    .din(new_n9_)
  );


  splt
  gnew_n10_
  (
    .dout(new_n10__spl_),
    .din(new_n10_)
  );


endmodule
