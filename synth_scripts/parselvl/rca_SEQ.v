// Benchmark "mymod" written by ABC on Sun Nov  5 20:38:26 2023

module mymod (  
    X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3,
    S_0, S_1, S_2, S_3, Co  );
  
  input  X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3;
  output S_0, S_1, S_2, S_3, Co;
  reg \rippe_adder|XX_2 , \rippe_adder|XX_3 , \rippe_adder|XXX_3 ,
    \rippe_adder|YY_2 , \rippe_adder|YY_3 , \rippe_adder|YYY_3 ,
    \rippe_adder|sS_0 , \rippe_adder|SS_0 , \rippe_adder|SSS_0 ,
    \rippe_adder|sS_1 , \rippe_adder|SS_1 , \rippe_adder|sS_2 ,
    \rippe_adder|xw1 , \rippe_adder|xw2 , \rippe_adder|xw3 , n87_o2,
    n88_o2, n93_o2, n94_o2, n77_o2, n78_o2;
  wire new_n56_, new_n57_, new_n58_, new_n59_, new_n60_, new_n62_, new_n64_,
    new_n66_, new_n68_, new_n70_, new_n72_, new_n74_, new_n76_, new_n78_,
    new_n80_, new_n82_, new_n84_, new_n86_, new_n88_, new_n90_, new_n92_,
    new_n94_, new_n96_, new_n97_, new_n98_, new_n99_, new_n100_, new_n101_,
    new_n102_, new_n103_, new_n104_, new_n105_, new_n106_, new_n107_,
    new_n108_, new_n109_, new_n110_, new_n111_, new_n112_, new_n113_,
    new_n114_, new_n115_, new_n116_, new_n117_, new_n118_, new_n119_,
    new_n120_, new_n121_, new_n122_, new_n123_, new_n124_, new_n125_,
    new_n126_, new_n127_, new_n128_, new_n129_, new_n130_, new_n131_,
    new_n132_, new_n133_, new_n134_, new_n135_, new_n136_, new_n137_,
    new_n138_, new_n139_, new_n140_, new_n167_, new_n168_, new_n169_,
    new_n170_, new_n171_, new_n172_, new_n173_, new_n174_, new_n175_,
    new_n176_, new_n177_, new_n178_, new_n179_, n61_li01_li01,
    n67_li03_li03, n70_li04_li04, n79_li07_li07, n85_li09_li09,
    n88_li10_li10, n94_li12_li12, n97_li13_li13, n100_li14_li14,
    n103_li15_li15, n106_li16_li16, n109_li17_li17, n112_li18_li18,
    n115_li19_li19, n118_li20_li20, n87_i2, n88_i2, n93_i2, n94_i2, n77_i2,
    n78_i2;
  assign new_n56_ = X_0;
  assign new_n57_ = ~X_0;
  assign new_n58_ = Y_0;
  assign new_n59_ = ~Y_0;
  assign new_n60_ = X_1;
  assign new_n62_ = Y_1;
  assign new_n64_ = X_2;
  assign new_n66_ = Y_2;
  assign new_n68_ = X_3;
  assign new_n70_ = Y_3;
  assign new_n72_ = \rippe_adder|XX_2 ;
  assign new_n74_ = \rippe_adder|XX_3 ;
  assign new_n76_ = \rippe_adder|XXX_3 ;
  assign new_n78_ = \rippe_adder|YY_2 ;
  assign new_n80_ = \rippe_adder|YY_3 ;
  assign new_n82_ = \rippe_adder|YYY_3 ;
  assign new_n84_ = \rippe_adder|sS_0 ;
  assign new_n86_ = \rippe_adder|SS_0 ;
  assign new_n88_ = \rippe_adder|SSS_0 ;
  assign new_n90_ = \rippe_adder|sS_1 ;
  assign new_n92_ = \rippe_adder|SS_1 ;
  assign new_n94_ = \rippe_adder|sS_2 ;
  assign new_n96_ = \rippe_adder|xw1 ;
  assign new_n97_ = ~\rippe_adder|xw1 ;
  assign new_n98_ = \rippe_adder|xw2 ;
  assign new_n99_ = ~\rippe_adder|xw2 ;
  assign new_n100_ = \rippe_adder|xw3 ;
  assign new_n101_ = ~\rippe_adder|xw3 ;
  assign new_n102_ = n87_o2;
  assign new_n103_ = ~n87_o2;
  assign new_n104_ = n88_o2;
  assign new_n105_ = ~n88_o2;
  assign new_n106_ = n93_o2;
  assign new_n107_ = ~n93_o2;
  assign new_n108_ = n94_o2;
  assign new_n109_ = ~n94_o2;
  assign new_n110_ = n77_o2;
  assign new_n111_ = ~n77_o2;
  assign new_n112_ = n78_o2;
  assign new_n113_ = ~n78_o2;
  assign new_n114_ = new_n167_ & new_n112_;
  assign new_n115_ = new_n110_ | new_n113_;
  assign new_n116_ = new_n101_ | new_n115_;
  assign new_n117_ = new_n100_ | new_n114_;
  assign new_n118_ = new_n168_ & new_n117_;
  assign new_n119_ = new_n167_ & new_n168_;
  assign new_n120_ = new_n57_ | new_n59_;
  assign new_n121_ = new_n56_ | new_n58_;
  assign new_n122_ = new_n169_ & new_n121_;
  assign new_n123_ = new_n170_ & new_n104_;
  assign new_n124_ = new_n102_ | new_n105_;
  assign new_n125_ = new_n97_ | new_n124_;
  assign new_n126_ = new_n96_ | new_n123_;
  assign new_n127_ = new_n171_ & new_n126_;
  assign new_n128_ = new_n172_ & new_n108_;
  assign new_n129_ = new_n106_ | new_n109_;
  assign new_n130_ = new_n99_ | new_n129_;
  assign new_n131_ = new_n98_ | new_n128_;
  assign new_n132_ = new_n173_ & new_n131_;
  assign new_n133_ = new_n170_ & new_n171_;
  assign new_n134_ = new_n172_ & new_n173_;
  assign new_n135_ = new_n174_ & new_n175_;
  assign new_n136_ = new_n174_ | new_n175_;
  assign new_n137_ = new_n176_ & new_n177_;
  assign new_n138_ = new_n176_ | new_n177_;
  assign new_n139_ = new_n178_ & new_n179_;
  assign new_n140_ = new_n178_ | new_n179_;
  assign S_0 = new_n84_;
  assign S_1 = new_n90_;
  assign S_2 = new_n94_;
  assign S_3 = new_n118_;
  assign Co = ~new_n119_;
  assign n61_li01_li01 = new_n64_;
  assign n67_li03_li03 = new_n68_;
  assign n70_li04_li04 = new_n74_;
  assign n79_li07_li07 = new_n66_;
  assign n85_li09_li09 = new_n70_;
  assign n88_li10_li10 = new_n80_;
  assign n94_li12_li12 = new_n86_;
  assign n97_li13_li13 = new_n88_;
  assign n100_li14_li14 = new_n122_;
  assign n103_li15_li15 = new_n92_;
  assign n106_li16_li16 = new_n127_;
  assign n109_li17_li17 = new_n132_;
  assign n112_li18_li18 = ~new_n169_;
  assign n115_li19_li19 = ~new_n133_;
  assign n118_li20_li20 = ~new_n134_;
  assign n87_i2 = new_n135_;
  assign n88_i2 = new_n136_;
  assign n93_i2 = new_n137_;
  assign n94_i2 = new_n138_;
  assign n77_i2 = new_n139_;
  assign n78_i2 = new_n140_;
  assign new_n167_ = new_n111_;
  assign new_n168_ = new_n116_;
  assign new_n169_ = new_n120_;
  assign new_n170_ = new_n103_;
  assign new_n171_ = new_n125_;
  assign new_n172_ = new_n107_;
  assign new_n173_ = new_n130_;
  assign new_n174_ = new_n60_;
  assign new_n175_ = new_n62_;
  assign new_n176_ = new_n72_;
  assign new_n177_ = new_n78_;
  assign new_n178_ = new_n76_;
  assign new_n179_ = new_n82_;
  always @ (posedge clock) begin
    \rippe_adder|XX_2  <= n61_li01_li01;
    \rippe_adder|XX_3  <= n67_li03_li03;
    \rippe_adder|XXX_3  <= n70_li04_li04;
    \rippe_adder|YY_2  <= n79_li07_li07;
    \rippe_adder|YY_3  <= n85_li09_li09;
    \rippe_adder|YYY_3  <= n88_li10_li10;
    \rippe_adder|sS_0  <= n94_li12_li12;
    \rippe_adder|SS_0  <= n97_li13_li13;
    \rippe_adder|SSS_0  <= n100_li14_li14;
    \rippe_adder|sS_1  <= n103_li15_li15;
    \rippe_adder|SS_1  <= n106_li16_li16;
    \rippe_adder|sS_2  <= n109_li17_li17;
    \rippe_adder|xw1  <= n112_li18_li18;
    \rippe_adder|xw2  <= n115_li19_li19;
    \rippe_adder|xw3  <= n118_li20_li20;
    n87_o2 <= n87_i2;
    n88_o2 <= n88_i2;
    n93_o2 <= n93_i2;
    n94_o2 <= n94_i2;
    n77_o2 <= n77_i2;
    n78_o2 <= n78_i2;
  end
  initial begin
    \rippe_adder|XX_2  <= 1'b0;
    \rippe_adder|XX_3  <= 1'b0;
    \rippe_adder|XXX_3  <= 1'b0;
    \rippe_adder|YY_2  <= 1'b0;
    \rippe_adder|YY_3  <= 1'b0;
    \rippe_adder|YYY_3  <= 1'b0;
    \rippe_adder|sS_0  <= 1'b0;
    \rippe_adder|SS_0  <= 1'b0;
    \rippe_adder|SSS_0  <= 1'b0;
    \rippe_adder|sS_1  <= 1'b0;
    \rippe_adder|SS_1  <= 1'b0;
    \rippe_adder|sS_2  <= 1'b0;
    \rippe_adder|xw1  <= 1'b0;
    \rippe_adder|xw2  <= 1'b0;
    \rippe_adder|xw3  <= 1'b0;
    n87_o2 <= 1'b0;
    n88_o2 <= 1'b0;
    n93_o2 <= 1'b0;
    n94_o2 <= 1'b0;
    n77_o2 <= 1'b0;
    n78_o2 <= 1'b0;
  end
endmodule


