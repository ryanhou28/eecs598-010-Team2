// Benchmark "c432" written by ABC on Sun Oct 29 22:18:03 2023

module c432 ( 
    G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16,
    G17, G18, G19, G20, G21, G22, G23, G24, G25, G26, G27, G28, G29, G30,
    G31, G32, G33, G34, G35, G36,
    G426, G427, G428, G429, G430, G431, G432  );
  input  G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14,
    G15, G16, G17, G18, G19, G20, G21, G22, G23, G24, G25, G26, G27, G28,
    G29, G30, G31, G32, G33, G34, G35, G36;
  output G426, G427, G428, G429, G430, G431, G432;
  wire new_n44_, new_n45_, new_n46_, new_n47_, new_n48_, new_n49_, new_n50_,
    new_n51_, new_n52_, new_n53_, new_n54_, new_n55_, new_n56_, new_n57_,
    new_n58_, new_n59_, new_n60_, new_n62_, new_n63_, new_n64_, new_n65_,
    new_n66_, new_n67_, new_n68_, new_n69_, new_n70_, new_n71_, new_n72_,
    new_n73_, new_n74_, new_n75_, new_n76_, new_n77_, new_n78_, new_n79_,
    new_n80_, new_n81_, new_n82_, new_n83_, new_n84_, new_n85_, new_n86_,
    new_n87_, new_n88_, new_n89_, new_n90_, new_n91_, new_n92_, new_n93_,
    new_n94_, new_n95_, new_n96_, new_n98_, new_n99_, new_n100_, new_n101_,
    new_n102_, new_n103_, new_n104_, new_n105_, new_n106_, new_n107_,
    new_n108_, new_n109_, new_n110_, new_n111_, new_n112_, new_n113_,
    new_n114_, new_n115_, new_n116_, new_n117_, new_n118_, new_n119_,
    new_n120_, new_n121_, new_n122_, new_n123_, new_n124_, new_n125_,
    new_n126_, new_n127_, new_n128_, new_n129_, new_n130_, new_n131_,
    new_n132_, new_n134_, new_n135_, new_n136_, new_n137_, new_n138_,
    new_n139_, new_n140_, new_n141_, new_n142_, new_n143_, new_n144_,
    new_n145_, new_n147_, new_n148_, new_n149_, new_n150_, new_n151_,
    new_n152_, new_n153_, new_n154_, new_n155_, new_n156_, new_n157_,
    new_n158_, new_n160_, new_n161_, new_n162_, new_n163_, new_n165_,
    new_n166_, new_n167_, new_n168_;
  anb1 g000(.dina(G30), .dinb(G28), .dout(new_n44_));
  anb2 g001(.dina(G16), .dinb(G18), .dout(new_n45_));
  anb2 g002(.dina(G20), .dinb(G22), .dout(new_n46_));
  anb2 g003(.dina(G1), .dinb(G2), .dout(new_n47_));
  anb2 g004(.dina(G4), .dinb(G6), .dout(new_n48_));
  anb1 g005(.dina(G26), .dinb(G24), .dout(new_n49_));
  anb1 g006(.dina(G34), .dinb(G32), .dout(new_n50_));
  anb1 g007(.dina(G14), .dinb(G12), .dout(new_n51_));
  anb1 g008(.dina(G10), .dinb(G8), .dout(new_n52_));
  anb1 g009(.dina(new_n48_), .dinb(new_n49_), .dout(new_n53_));
  anb2 g010(.dina(new_n52_), .dinb(new_n53_), .dout(new_n54_));
  anb1 g011(.dina(new_n45_), .dinb(new_n51_), .dout(new_n55_));
  anb2 g012(.dina(new_n44_), .dinb(new_n47_), .dout(new_n56_));
  anb1 g013(.dina(new_n46_), .dinb(new_n50_), .dout(new_n57_));
  anb2 g014(.dina(new_n56_), .dinb(new_n57_), .dout(new_n58_));
  anb1 g015(.dina(new_n55_), .dinb(new_n58_), .dout(new_n59_));
  nab1 g016(.dina(new_n54_), .dinb(new_n59_), .dout(new_n60_));
  anb2 g017(.dina(new_n54_), .dinb(new_n59_), .dout(G426));
  anb1 g018(.dina(G20), .dinb(new_n60_), .dout(new_n62_));
  anb1 g019(.dina(G22), .dinb(new_n62_), .dout(new_n63_));
  anb1 g020(.dina(new_n63_), .dinb(G23), .dout(new_n64_));
  anb1 g021(.dina(G8), .dinb(new_n60_), .dout(new_n65_));
  anb1 g022(.dina(G10), .dinb(new_n65_), .dout(new_n66_));
  anb2 g023(.dina(G11), .dinb(new_n66_), .dout(new_n67_));
  anb1 g024(.dina(G1), .dinb(new_n60_), .dout(new_n68_));
  anb1 g025(.dina(G2), .dinb(new_n68_), .dout(new_n69_));
  anb2 g026(.dina(G3), .dinb(new_n69_), .dout(new_n70_));
  anb1 g027(.dina(G4), .dinb(new_n60_), .dout(new_n71_));
  anb1 g028(.dina(G6), .dinb(new_n71_), .dout(new_n72_));
  anb2 g029(.dina(G7), .dinb(new_n72_), .dout(new_n73_));
  anb1 g030(.dina(G28), .dinb(new_n60_), .dout(new_n74_));
  anb1 g031(.dina(G30), .dinb(new_n74_), .dout(new_n75_));
  anb2 g032(.dina(G31), .dinb(new_n75_), .dout(new_n76_));
  anb1 g033(.dina(G16), .dinb(new_n60_), .dout(new_n77_));
  anb1 g034(.dina(G18), .dinb(new_n77_), .dout(new_n78_));
  anb1 g035(.dina(new_n78_), .dinb(G19), .dout(new_n79_));
  anb1 g036(.dina(G12), .dinb(new_n60_), .dout(new_n80_));
  anb1 g037(.dina(G14), .dinb(new_n80_), .dout(new_n81_));
  anb1 g038(.dina(new_n81_), .dinb(G15), .dout(new_n82_));
  anb1 g039(.dina(G32), .dinb(new_n60_), .dout(new_n83_));
  anb1 g040(.dina(G34), .dinb(new_n83_), .dout(new_n84_));
  anb1 g041(.dina(new_n84_), .dinb(G35), .dout(new_n85_));
  anb1 g042(.dina(G24), .dinb(new_n60_), .dout(new_n86_));
  anb1 g043(.dina(G26), .dinb(new_n86_), .dout(new_n87_));
  anb1 g044(.dina(new_n87_), .dinb(G27), .dout(new_n88_));
  anb1 g045(.dina(new_n76_), .dinb(new_n79_), .dout(new_n89_));
  anb2 g046(.dina(new_n88_), .dinb(new_n89_), .dout(new_n90_));
  anb1 g047(.dina(new_n67_), .dinb(new_n85_), .dout(new_n91_));
  anb2 g048(.dina(new_n64_), .dinb(new_n73_), .dout(new_n92_));
  anb1 g049(.dina(new_n70_), .dinb(new_n82_), .dout(new_n93_));
  anb2 g050(.dina(new_n92_), .dinb(new_n93_), .dout(new_n94_));
  anb1 g051(.dina(new_n91_), .dinb(new_n94_), .dout(new_n95_));
  nab1 g052(.dina(new_n90_), .dinb(new_n95_), .dout(new_n96_));
  anb2 g053(.dina(new_n90_), .dinb(new_n95_), .dout(G427));
  anb1 g054(.dina(G23), .dinb(new_n96_), .dout(new_n98_));
  anb1 g055(.dina(new_n63_), .dinb(new_n98_), .dout(new_n99_));
  anb1 g056(.dina(new_n99_), .dinb(G25), .dout(new_n100_));
  anb1 g057(.dina(G11), .dinb(new_n96_), .dout(new_n101_));
  anb1 g058(.dina(new_n66_), .dinb(new_n101_), .dout(new_n102_));
  anb2 g059(.dina(G13), .dinb(new_n102_), .dout(new_n103_));
  anb1 g060(.dina(G3), .dinb(new_n96_), .dout(new_n104_));
  anb1 g061(.dina(new_n69_), .dinb(new_n104_), .dout(new_n105_));
  anb2 g062(.dina(G5), .dinb(new_n105_), .dout(new_n106_));
  anb1 g063(.dina(G7), .dinb(new_n96_), .dout(new_n107_));
  anb1 g064(.dina(new_n72_), .dinb(new_n107_), .dout(new_n108_));
  anb2 g065(.dina(G9), .dinb(new_n108_), .dout(new_n109_));
  anb1 g066(.dina(G31), .dinb(new_n96_), .dout(new_n110_));
  anb1 g067(.dina(new_n75_), .dinb(new_n110_), .dout(new_n111_));
  anb2 g068(.dina(G33), .dinb(new_n111_), .dout(new_n112_));
  anb1 g069(.dina(G19), .dinb(new_n96_), .dout(new_n113_));
  anb1 g070(.dina(new_n78_), .dinb(new_n113_), .dout(new_n114_));
  anb1 g071(.dina(new_n114_), .dinb(G21), .dout(new_n115_));
  anb1 g072(.dina(G15), .dinb(new_n96_), .dout(new_n116_));
  anb1 g073(.dina(new_n81_), .dinb(new_n116_), .dout(new_n117_));
  anb1 g074(.dina(new_n117_), .dinb(G17), .dout(new_n118_));
  anb1 g075(.dina(G35), .dinb(new_n96_), .dout(new_n119_));
  anb1 g076(.dina(new_n84_), .dinb(new_n119_), .dout(new_n120_));
  anb1 g077(.dina(new_n120_), .dinb(G36), .dout(new_n121_));
  anb1 g078(.dina(G27), .dinb(new_n96_), .dout(new_n122_));
  anb1 g079(.dina(new_n87_), .dinb(new_n122_), .dout(new_n123_));
  anb1 g080(.dina(new_n123_), .dinb(G29), .dout(new_n124_));
  anb1 g081(.dina(new_n112_), .dinb(new_n115_), .dout(new_n125_));
  anb2 g082(.dina(new_n124_), .dinb(new_n125_), .dout(new_n126_));
  anb1 g083(.dina(new_n103_), .dinb(new_n121_), .dout(new_n127_));
  anb2 g084(.dina(new_n100_), .dinb(new_n109_), .dout(new_n128_));
  anb1 g085(.dina(new_n106_), .dinb(new_n118_), .dout(new_n129_));
  anb2 g086(.dina(new_n128_), .dinb(new_n129_), .dout(new_n130_));
  anb1 g087(.dina(new_n127_), .dinb(new_n130_), .dout(new_n131_));
  nab1 g088(.dina(new_n126_), .dinb(new_n131_), .dout(new_n132_));
  anb2 g089(.dina(new_n126_), .dinb(new_n131_), .dout(G428));
  anb1 g090(.dina(G5), .dinb(new_n132_), .dout(new_n134_));
  anb2 g091(.dina(new_n134_), .dinb(new_n105_), .dout(new_n135_));
  anb1 g092(.dina(G9), .dinb(new_n132_), .dout(new_n136_));
  anb2 g093(.dina(new_n136_), .dinb(new_n108_), .dout(new_n137_));
  anb1 g094(.dina(G13), .dinb(new_n132_), .dout(new_n138_));
  anb1 g095(.dina(new_n102_), .dinb(new_n138_), .dout(new_n139_));
  anb1 g096(.dina(new_n137_), .dinb(new_n139_), .dout(new_n140_));
  anb1 g097(.dina(G21), .dinb(new_n132_), .dout(new_n141_));
  anb2 g098(.dina(new_n141_), .dinb(new_n114_), .dout(new_n142_));
  anb1 g099(.dina(G17), .dinb(new_n132_), .dout(new_n143_));
  anb2 g100(.dina(new_n143_), .dinb(new_n117_), .dout(new_n144_));
  and1 g101(.dina(new_n142_), .dinb(new_n144_), .dout(new_n145_));
  nor2 g102(.dina(new_n140_), .dinb(new_n145_), .dout(G430));
  anb1 g103(.dina(G36), .dinb(new_n132_), .dout(new_n147_));
  anb2 g104(.dina(new_n147_), .dinb(new_n120_), .dout(new_n148_));
  anb1 g105(.dina(G33), .dinb(new_n132_), .dout(new_n149_));
  anb2 g106(.dina(new_n149_), .dinb(new_n111_), .dout(new_n150_));
  and1 g107(.dina(new_n148_), .dinb(new_n150_), .dout(new_n151_));
  anb1 g108(.dina(G29), .dinb(new_n132_), .dout(new_n152_));
  anb2 g109(.dina(new_n152_), .dinb(new_n123_), .dout(new_n153_));
  anb1 g110(.dina(G25), .dinb(new_n132_), .dout(new_n154_));
  anb1 g111(.dina(new_n99_), .dinb(new_n154_), .dout(new_n155_));
  nab2 g112(.dina(new_n153_), .dinb(new_n155_), .dout(new_n156_));
  anb1 g113(.dina(new_n151_), .dinb(new_n156_), .dout(new_n157_));
  nab1 g114(.dina(G430), .dinb(new_n157_), .dout(new_n158_));
  anb1 g115(.dina(new_n135_), .dinb(new_n158_), .dout(G429));
  anb2 g116(.dina(new_n139_), .dinb(new_n155_), .dout(new_n160_));
  anb1 g117(.dina(new_n145_), .dinb(new_n160_), .dout(new_n161_));
  anb1 g118(.dina(new_n145_), .dinb(new_n153_), .dout(new_n162_));
  anb1 g119(.dina(new_n140_), .dinb(new_n162_), .dout(new_n163_));
  anb2 g120(.dina(new_n161_), .dinb(new_n163_), .dout(G431));
  anb1 g121(.dina(new_n153_), .dinb(new_n150_), .dout(new_n165_));
  nab2 g122(.dina(new_n144_), .dinb(new_n165_), .dout(new_n166_));
  nab1 g123(.dina(new_n139_), .dinb(new_n166_), .dout(new_n167_));
  anb1 g124(.dina(new_n137_), .dinb(new_n161_), .dout(new_n168_));
  anb2 g125(.dina(new_n167_), .dinb(new_n168_), .dout(G432));
endmodule


