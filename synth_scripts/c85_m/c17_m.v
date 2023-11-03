// Benchmark "c17" written by ABC on Sun Oct 29 22:18:02 2023

module c17 ( 
    G1, G2, G3, G4, G5,
    G16, G17  );
  input  G1, G2, G3, G4, G5;
  output G16, G17;
  wire new_n8_, new_n9_, new_n10_, new_n12_;
  and1 g0(.dina(G1), .dinb(G3), .dout(new_n8_));
  and1 g1(.dina(G3), .dinb(G4), .dout(new_n9_));
  anb2 g2(.dina(new_n9_), .dinb(G2), .dout(new_n10_));
  anb2 g3(.dina(new_n8_), .dinb(new_n10_), .dout(G16));
  anb1 g4(.dina(G5), .dinb(new_n9_), .dout(new_n12_));
  nab2 g5(.dina(new_n10_), .dinb(new_n12_), .dout(G17));
endmodule


