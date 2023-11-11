// Benchmark "mymod" written by ABC on Thu Nov  2 00:21:40 2023

module mymod (  
    X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3,
    S_0, S_1, S_2, S_3, Co  );
  
  input  X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3;
  output S_0, S_1, S_2, S_3, Co;
  reg \rippe_adder|xw1 , \rippe_adder|xw2 , \rippe_adder|xw3 ;
  wire new_n20_, new_n21_, new_n22_, new_n23_, new_n24_, new_n25_, new_n26_,
    new_n27_, new_n28_, new_n29_, new_n30_, new_n31_, new_n32_, new_n33_,
    new_n34_, new_n35_, new_n36_, new_n37_, new_n38_, new_n39_, new_n40_,
    new_n41_, new_n42_, new_n43_, new_n44_, new_n45_, new_n46_, new_n47_,
    new_n48_, new_n49_, new_n50_, new_n51_, new_n52_, new_n53_, new_n54_,
    new_n55_, new_n56_, new_n57_, new_n58_, new_n59_, new_n60_, new_n61_,
    new_n62_, new_n63_, new_n64_, new_n65_, new_n66_, new_n67_, new_n68_,
    new_n69_, new_n70_, new_n71_, new_n72_, new_n73_, new_n74_, new_n83_,
    new_n84_, new_n85_, new_n86_, new_n87_, new_n88_, new_n89_, new_n90_,
    new_n91_, new_n92_, new_n93_, new_n94_, new_n95_, new_n96_, new_n97_,
    new_n98_, new_n99_, new_n100_, new_n101_, n34_li0_li0, n37_li1_li1,
    n40_li2_li2;
  assign new_n20_ = X_0;
  assign new_n21_ = ~X_0;
  assign new_n22_ = Y_0;
  assign new_n23_ = ~Y_0;
  assign new_n24_ = X_1;
  assign new_n25_ = ~X_1;
  assign new_n26_ = Y_1;
  assign new_n27_ = ~Y_1;
  assign new_n28_ = X_2;
  assign new_n29_ = ~X_2;
  assign new_n30_ = Y_2;
  assign new_n31_ = ~Y_2;
  assign new_n32_ = X_3;
  assign new_n33_ = ~X_3;
  assign new_n34_ = Y_3;
  assign new_n35_ = ~Y_3;
  assign new_n36_ = \rippe_adder|xw1 ;
  assign new_n37_ = ~\rippe_adder|xw1 ;
  assign new_n38_ = \rippe_adder|xw2 ;
  assign new_n39_ = ~\rippe_adder|xw2 ;
  assign new_n40_ = \rippe_adder|xw3 ;
  assign new_n41_ = ~\rippe_adder|xw3 ;
  assign new_n42_ = new_n21_ | new_n23_;
  assign new_n43_ = new_n20_ | new_n22_;
  assign new_n44_ = new_n83_ & new_n43_;
  assign new_n45_ = new_n84_ & new_n85_;
  assign new_n46_ = new_n86_ | new_n87_;
  assign new_n47_ = new_n86_ & new_n87_;
  assign new_n48_ = new_n84_ | new_n85_;
  assign new_n49_ = new_n88_ & new_n48_;
  assign new_n50_ = new_n45_ | new_n47_;
  assign new_n51_ = new_n37_ | new_n50_;
  assign new_n52_ = new_n36_ | new_n49_;
  assign new_n53_ = new_n89_ & new_n52_;
  assign new_n54_ = new_n90_ & new_n91_;
  assign new_n55_ = new_n92_ | new_n93_;
  assign new_n56_ = new_n92_ & new_n93_;
  assign new_n57_ = new_n90_ | new_n91_;
  assign new_n58_ = new_n94_ & new_n57_;
  assign new_n59_ = new_n54_ | new_n56_;
  assign new_n60_ = new_n39_ | new_n59_;
  assign new_n61_ = new_n38_ | new_n58_;
  assign new_n62_ = new_n95_ & new_n61_;
  assign new_n63_ = new_n96_ & new_n97_;
  assign new_n64_ = new_n98_ | new_n99_;
  assign new_n65_ = new_n98_ & new_n99_;
  assign new_n66_ = new_n96_ | new_n97_;
  assign new_n67_ = new_n100_ & new_n66_;
  assign new_n68_ = new_n63_ | new_n65_;
  assign new_n69_ = new_n41_ | new_n68_;
  assign new_n70_ = new_n40_ | new_n67_;
  assign new_n71_ = new_n101_ & new_n70_;
  assign new_n72_ = new_n100_ & new_n101_;
  assign new_n73_ = new_n88_ & new_n89_;
  assign new_n74_ = new_n94_ & new_n95_;
  assign S_0 = new_n44_;
  assign S_1 = new_n53_;
  assign S_2 = new_n62_;
  assign S_3 = new_n71_;
  assign Co = ~new_n72_;
  assign n34_li0_li0 = ~new_n83_;
  assign n37_li1_li1 = ~new_n73_;
  assign n40_li2_li2 = ~new_n74_;
  assign new_n83_ = new_n42_;
  assign new_n84_ = new_n24_;
  assign new_n85_ = new_n26_;
  assign new_n86_ = new_n25_;
  assign new_n87_ = new_n27_;
  assign new_n88_ = new_n46_;
  assign new_n89_ = new_n51_;
  assign new_n90_ = new_n28_;
  assign new_n91_ = new_n30_;
  assign new_n92_ = new_n29_;
  assign new_n93_ = new_n31_;
  assign new_n94_ = new_n55_;
  assign new_n95_ = new_n60_;
  assign new_n96_ = new_n32_;
  assign new_n97_ = new_n34_;
  assign new_n98_ = new_n33_;
  assign new_n99_ = new_n35_;
  assign new_n100_ = new_n64_;
  assign new_n101_ = new_n69_;
  always  begin
    \rippe_adder|xw1  <= n34_li0_li0;
    \rippe_adder|xw2  <= n37_li1_li1;
    \rippe_adder|xw3  <= n40_li2_li2;
  end
  initial begin
    \rippe_adder|xw1  <= 1'b0;
    \rippe_adder|xw2  <= 1'b0;
    \rippe_adder|xw3  <= 1'b0;
  end
endmodule


