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
  wire new_new_n56__, new_new_n57__, new_new_n58__, new_new_n59__,
    new_new_n60__, new_new_n62__, new_new_n64__, new_new_n66__,
    new_new_n68__, new_new_n70__, new_new_n72__, new_new_n74__,
    new_new_n76__, new_new_n78__, new_new_n80__, new_new_n82__,
    new_new_n84__, new_new_n86__, new_new_n88__, new_new_n90__,
    new_new_n92__, new_new_n94__, new_new_n96__, new_new_n97__,
    new_new_n98__, new_new_n99__, new_new_n100__, new_new_n101__,
    new_new_n102__, new_new_n103__, new_new_n104__, new_new_n105__,
    new_new_n106__, new_new_n107__, new_new_n108__, new_new_n109__,
    new_new_n110__, new_new_n111__, new_new_n112__, new_new_n113__,
    new_new_n114__, new_new_n115__, new_new_n116__, new_new_n117__,
    new_new_n118__, new_new_n119__, new_new_n120__, new_new_n121__,
    new_new_n122__, new_new_n123__, new_new_n124__, new_new_n125__,
    new_new_n126__, new_new_n127__, new_new_n128__, new_new_n129__,
    new_new_n130__, new_new_n131__, new_new_n132__, new_new_n133__,
    new_new_n134__, new_new_n135__, new_new_n136__, new_new_n137__,
    new_new_n138__, new_new_n139__, new_new_n140__, new_new_n167__,
    new_new_n168__, new_new_n169__, new_new_n170__, new_new_n171__,
    new_new_n172__, new_new_n173__, new_new_n174__, new_new_n175__,
    new_new_n176__, new_new_n177__, new_new_n178__, new_new_n179__, n255,
    n258, n261, n264, n267, n270, n273, n276, n279, n282, n285, n288, n291,
    n294, n297, n300, n303, n306, n309, n312, n315;
  buf1  g000(.din(X_0), .dout(new_new_n56__));
  not1  g001(.din(X_0), .dout(new_new_n57__));
  buf1  g002(.din(Y_0), .dout(new_new_n58__));
  not1  g003(.din(Y_0), .dout(new_new_n59__));
  buf1  g004(.din(X_1), .dout(new_new_n60__));
  buf1  g005(.din(Y_1), .dout(new_new_n62__));
  buf1  g006(.din(X_2), .dout(new_new_n64__));
  buf1  g007(.din(Y_2), .dout(new_new_n66__));
  buf1  g008(.din(X_3), .dout(new_new_n68__));
  buf1  g009(.din(Y_3), .dout(new_new_n70__));
  buf1  g010(.din(\rippe_adder|XX_2 ), .dout(new_new_n72__));
  buf1  g011(.din(\rippe_adder|XX_3 ), .dout(new_new_n74__));
  buf1  g012(.din(\rippe_adder|XXX_3 ), .dout(new_new_n76__));
  buf1  g013(.din(\rippe_adder|YY_2 ), .dout(new_new_n78__));
  buf1  g014(.din(\rippe_adder|YY_3 ), .dout(new_new_n80__));
  buf1  g015(.din(\rippe_adder|YYY_3 ), .dout(new_new_n82__));
  buf1  g016(.din(\rippe_adder|sS_0 ), .dout(new_new_n84__));
  buf1  g017(.din(\rippe_adder|SS_0 ), .dout(new_new_n86__));
  buf1  g018(.din(\rippe_adder|SSS_0 ), .dout(new_new_n88__));
  buf1  g019(.din(\rippe_adder|sS_1 ), .dout(new_new_n90__));
  buf1  g020(.din(\rippe_adder|SS_1 ), .dout(new_new_n92__));
  buf1  g021(.din(\rippe_adder|sS_2 ), .dout(new_new_n94__));
  buf1  g022(.din(\rippe_adder|xw1 ), .dout(new_new_n96__));
  not1  g023(.din(\rippe_adder|xw1 ), .dout(new_new_n97__));
  buf1  g024(.din(\rippe_adder|xw2 ), .dout(new_new_n98__));
  not1  g025(.din(\rippe_adder|xw2 ), .dout(new_new_n99__));
  buf1  g026(.din(\rippe_adder|xw3 ), .dout(new_new_n100__));
  not1  g027(.din(\rippe_adder|xw3 ), .dout(new_new_n101__));
  buf1  g028(.din(n87_o2), .dout(new_new_n102__));
  not1  g029(.din(n87_o2), .dout(new_new_n103__));
  buf1  g030(.din(n88_o2), .dout(new_new_n104__));
  not1  g031(.din(n88_o2), .dout(new_new_n105__));
  buf1  g032(.din(n93_o2), .dout(new_new_n106__));
  not1  g033(.din(n93_o2), .dout(new_new_n107__));
  buf1  g034(.din(n94_o2), .dout(new_new_n108__));
  not1  g035(.din(n94_o2), .dout(new_new_n109__));
  buf1  g036(.din(n77_o2), .dout(new_new_n110__));
  not1  g037(.din(n77_o2), .dout(new_new_n111__));
  buf1  g038(.din(n78_o2), .dout(new_new_n112__));
  not1  g039(.din(n78_o2), .dout(new_new_n113__));
  and1  g040(.dina(new_new_n167__), .dinb(new_new_n112__), .dout(new_new_n114__));
  or1   g041(.dina(new_new_n110__), .dinb(new_new_n113__), .dout(new_new_n115__));
  or1   g042(.dina(new_new_n101__), .dinb(new_new_n115__), .dout(new_new_n116__));
  or1   g043(.dina(new_new_n100__), .dinb(new_new_n114__), .dout(new_new_n117__));
  and1  g044(.dina(new_new_n168__), .dinb(new_new_n117__), .dout(new_new_n118__));
  and1  g045(.dina(new_new_n167__), .dinb(new_new_n168__), .dout(new_new_n119__));
  or1   g046(.dina(new_new_n57__), .dinb(new_new_n59__), .dout(new_new_n120__));
  or1   g047(.dina(new_new_n56__), .dinb(new_new_n58__), .dout(new_new_n121__));
  and1  g048(.dina(new_new_n169__), .dinb(new_new_n121__), .dout(new_new_n122__));
  and1  g049(.dina(new_new_n170__), .dinb(new_new_n104__), .dout(new_new_n123__));
  or1   g050(.dina(new_new_n102__), .dinb(new_new_n105__), .dout(new_new_n124__));
  or1   g051(.dina(new_new_n97__), .dinb(new_new_n124__), .dout(new_new_n125__));
  or1   g052(.dina(new_new_n96__), .dinb(new_new_n123__), .dout(new_new_n126__));
  and1  g053(.dina(new_new_n171__), .dinb(new_new_n126__), .dout(new_new_n127__));
  and1  g054(.dina(new_new_n172__), .dinb(new_new_n108__), .dout(new_new_n128__));
  or1   g055(.dina(new_new_n106__), .dinb(new_new_n109__), .dout(new_new_n129__));
  or1   g056(.dina(new_new_n99__), .dinb(new_new_n129__), .dout(new_new_n130__));
  or1   g057(.dina(new_new_n98__), .dinb(new_new_n128__), .dout(new_new_n131__));
  and1  g058(.dina(new_new_n173__), .dinb(new_new_n131__), .dout(new_new_n132__));
  and1  g059(.dina(new_new_n170__), .dinb(new_new_n171__), .dout(new_new_n133__));
  and1  g060(.dina(new_new_n172__), .dinb(new_new_n173__), .dout(new_new_n134__));
  and1  g061(.dina(new_new_n174__), .dinb(new_new_n175__), .dout(new_new_n135__));
  or1   g062(.dina(new_new_n174__), .dinb(new_new_n175__), .dout(new_new_n136__));
  and1  g063(.dina(new_new_n176__), .dinb(new_new_n177__), .dout(new_new_n137__));
  or1   g064(.dina(new_new_n176__), .dinb(new_new_n177__), .dout(new_new_n138__));
  and1  g065(.dina(new_new_n178__), .dinb(new_new_n179__), .dout(new_new_n139__));
  or1   g066(.dina(new_new_n178__), .dinb(new_new_n179__), .dout(new_new_n140__));
  buf1  g067(.din(new_new_n84__), .dout(S_0));
  buf1  g068(.din(new_new_n90__), .dout(S_1));
  buf1  g069(.din(new_new_n94__), .dout(S_2));
  buf1  g070(.din(new_new_n118__), .dout(S_3));
  not1  g071(.din(new_new_n119__), .dout(Co));
  buf1  g072(.din(new_new_n64__), .dout(n255));
  buf1  g073(.din(new_new_n68__), .dout(n258));
  buf1  g074(.din(new_new_n74__), .dout(n261));
  buf1  g075(.din(new_new_n66__), .dout(n264));
  buf1  g076(.din(new_new_n70__), .dout(n267));
  buf1  g077(.din(new_new_n80__), .dout(n270));
  buf1  g078(.din(new_new_n86__), .dout(n273));
  buf1  g079(.din(new_new_n88__), .dout(n276));
  buf1  g080(.din(new_new_n122__), .dout(n279));
  buf1  g081(.din(new_new_n92__), .dout(n282));
  buf1  g082(.din(new_new_n127__), .dout(n285));
  buf1  g083(.din(new_new_n132__), .dout(n288));
  not1  g084(.din(new_new_n169__), .dout(n291));
  not1  g085(.din(new_new_n133__), .dout(n294));
  not1  g086(.din(new_new_n134__), .dout(n297));
  buf1  g087(.din(new_new_n135__), .dout(n300));
  buf1  g088(.din(new_new_n136__), .dout(n303));
  buf1  g089(.din(new_new_n137__), .dout(n306));
  buf1  g090(.din(new_new_n138__), .dout(n309));
  buf1  g091(.din(new_new_n139__), .dout(n312));
  buf1  g092(.din(new_new_n140__), .dout(n315));
  buf1  g093(.din(new_new_n111__), .dout(new_new_n167__));
  buf1  g094(.din(new_new_n116__), .dout(new_new_n168__));
  buf1  g095(.din(new_new_n120__), .dout(new_new_n169__));
  buf1  g096(.din(new_new_n103__), .dout(new_new_n170__));
  buf1  g097(.din(new_new_n125__), .dout(new_new_n171__));
  buf1  g098(.din(new_new_n107__), .dout(new_new_n172__));
  buf1  g099(.din(new_new_n130__), .dout(new_new_n173__));
  buf1  g100(.din(new_new_n60__), .dout(new_new_n174__));
  buf1  g101(.din(new_new_n62__), .dout(new_new_n175__));
  buf1  g102(.din(new_new_n72__), .dout(new_new_n176__));
  buf1  g103(.din(new_new_n78__), .dout(new_new_n177__));
  buf1  g104(.din(new_new_n76__), .dout(new_new_n178__));
  buf1  g105(.din(new_new_n82__), .dout(new_new_n179__));
  always @ (posedge clock) begin
    \rippe_adder|XX_2  <= n255;
    \rippe_adder|XX_3  <= n258;
    \rippe_adder|XXX_3  <= n261;
    \rippe_adder|YY_2  <= n264;
    \rippe_adder|YY_3  <= n267;
    \rippe_adder|YYY_3  <= n270;
    \rippe_adder|sS_0  <= n273;
    \rippe_adder|SS_0  <= n276;
    \rippe_adder|SSS_0  <= n279;
    \rippe_adder|sS_1  <= n282;
    \rippe_adder|SS_1  <= n285;
    \rippe_adder|sS_2  <= n288;
    \rippe_adder|xw1  <= n291;
    \rippe_adder|xw2  <= n294;
    \rippe_adder|xw3  <= n297;
    n87_o2 <= n300;
    n88_o2 <= n303;
    n93_o2 <= n306;
    n94_o2 <= n309;
    n77_o2 <= n312;
    n78_o2 <= n315;
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


