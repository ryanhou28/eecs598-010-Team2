module rippe_adder(X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3, S_0, S_1, S_2, S_3, Co);
 input X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3;
 output S_0, S_1, S_2, S_3;
 output Co;
 wire w1, w2, w3;
 reg xw1, xw2, xw3;
 // instantiating 4 1-bit full adders in Verilog
 fulladder u1(X_0, Y_0, 1'b0, S_0, w1);
 fulladder u2(X_1, Y_1, xw1, S_1, w2);
 fulladder u3(X_2, Y_2, xw2, S_2, w3);
 fulladder u4(X_3, Y_3, xw3, S_3, Co);
 always begin
   xw1 <= w1;
   xw2 <= w2;
   xw3 <= w3;
 end
 initial begin
   xw1 <= 1'b0;
   xw2 <= 1'b0;
   xw3 <= 1'b0;
 end
endmodule

module fulladder(X, Y, Ci, S, Co);
  input X, Y, Ci;
  output S, Co;
  wire w1,w2,w3;
  //Structural code for one bit full adder
  xor (w1, X, Y);
  xor (S, w1, Ci);
  and (w2, w1, Ci);
  and (w3, X, Y);
  or (Co, w2, w3);
endmodule
