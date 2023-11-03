module c17(G1,G16,G17,G2,G3,G4,G5);
input G1,G2,G3,G4,G5;
output G16,G17;

  wire G8,G9,G12,G15;

  nand (G8,G1,G3);
  nand (G9,G3,G4);
  nand (G12,G2,G9);
  nand (G15,G9,G5);
  nand (G16,G8,G12);
  nand (G17,G12,G15);

endmodule
