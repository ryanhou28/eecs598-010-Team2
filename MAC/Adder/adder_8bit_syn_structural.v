



module adder8(A_0_, A_1_, A_2_, A_3_, A_4_, A_5_, A_6_, A_7_, B_0_, B_1_, B_2_, B_3_, B_4_, B_5_, B_6_, B_7_, SUM_0_, SUM_1_, SUM_2_, SUM_3_, SUM_4_, SUM_5_, SUM_6_, SUM_7_);input A_0_;
  input A_1_;
  input A_2_;
  input A_3_;
  input A_4_;
  input A_5_;
  input A_6_;
  input A_7_;
  input B_0_;
  input B_1_;
  input B_2_;
  input B_3_;
  input B_4_;
  input B_5_;
  input B_6_;
  input B_7_;
  output SUM_0_;
  output SUM_1_;
  output SUM_2_;
  output SUM_3_;
  output SUM_4_;
  output SUM_5_;
  output SUM_6_;
  output SUM_7_;
  
  wire wire_zeros;
  assign wire_zeros = 1'b0;
  wire _000_;
  wire _001_;
  wire _002_;
  wire _003_;
  wire _004_;
  wire _005_;
  wire _006_;
  wire _007_;
  wire _008_;
  wire _009_;
  wire _010_;
  wire _011_;
  wire _012_;
  wire _013_;
  wire _014_;
  wire _015_;
  wire _016_;
  wire _017_;
  wire _018_;
  wire _019_;
  wire _020_;
  wire _021_;
  wire _022_;
  wire _023_;
  wire _024_;
  wire _025_;
  wire _026_;
  wire _027_;
  wire _028_;
  wire _029_;
  wire _030_;
  wire _031_;
  wire _032_;
  wire _033_;
  wire _034_;
  wire _035_;
  wire _036_;
  wire _037_;
  wire _038_;
  wire _039_;
  wire _040_;
  wire _041_;
  wire _042_;
  wire _043_;
  wire _044_;
  wire _045_;
  wire _046_;
  wire _047_;
  wire _048_;
  wire _049_;
  wire _050_;
  wire _051_;
  wire _052_;
  wire _053_;
  wire _054_;
  wire _055_;
  wire _056_;
  wire _057_;
  wire _058_;
  wire _059_;
  wire _060_;
  wire _061_;
  wire _062_;
  wire _063_;
  wire _064_;
  wire _065_;
  wire _066_;
  wire _067_;
  wire _068_;
  wire _069_;
  wire _070_;
  wire _071_;
  wire _072_;
  wire _073_;
  wire _074_;
  wire _075_;
  wire _076_;
  wire _077_;
  wire _078_;
  wire _079_;
  wire _080_;
  wire _081_;
  wire _082_;
  wire _083_;
  wire _084_;
  wire _085_;
  wire _086_;
  wire _087_;
  wire _088_;
  wire _089_;
  wire _090_;
  wire _091_;
  wire _092_;
  wire _093_;
  wire _094_;
  wire _095_;
  wire _096_;
  wire _097_;
  wire _098_;
  
  
  
  
  
  
  
  
  
  wire A_0_;
  wire A_1_;
  wire A_2_;
  wire A_3_;
  wire A_4_;
  wire A_5_;
  wire A_6_;
  wire A_7_;
  
  
  
  
  
  
  
  
  
  wire B_0_;
  wire B_1_;
  wire B_2_;
  wire B_3_;
  wire B_4_;
  wire B_5_;
  wire B_6_;
  wire B_7_;
  
  
  
  
  
  
  
  
  
  wire SUM_0_;
  wire SUM_1_;
  wire SUM_2_;
  wire SUM_3_;
  wire SUM_4_;
  wire SUM_5_;
  wire SUM_6_;
  wire SUM_7_;
  
  
  wire _cla1.A_0_;
  wire _cla1.A_1_;
  wire _cla1.A_2_;
  wire _cla1.A_3_;
  
  
  wire _cla1.B_0_ ;
  wire _cla1.B_1_;
  wire _cla1.B_2_;
  wire _cla1.B_3_;

  
  
  wire _cla1.CIN ;
  
  
  wire _cla1.fa0.a ;
  
  
  wire _cla1.fa0.b ;
  
  
  wire _cla1.fa0.cin ;
  
  
  wire _cla1.fa1.a ;
  
  
  wire _cla1.fa1.b ;
  
  
  wire _cla1.fa2.a ;
  
  
  wire _cla1.fa2.b ;
  
  
  wire _cla1.fa3.a ;
  
  
  wire _cla1.fa3.b ;
  
  
  wire _cla2.A_0_;
  wire _cla2.A_1_;
  wire _cla2.A_2_;
  wire _cla2.A_3_;
  
  wire _cla2.B_0_;
  wire _cla2.B_1_;
  wire _cla2.B_2_;
  wire _cla2.B_3_;
  
  
  wire _cla2.fa0.a ;
  
  
  wire _cla2.fa0.b ;
  
  
  wire _cla2.fa1.a ;
  
  
  wire _cla2.fa1.b ;
  
  
  wire _cla2.fa2.a ;
  
  
  wire _cla2.fa2.b ;
  
  
  wire _cla2.fa3.a ;
  
  
  wire _cla2.fa3.b ;
  
  
  wire sat_sum_0_;
  wire sat_sum_1_;
  wire sat_sum_2_;
  wire sat_sum_3_;
  wire sat_sum_4_;
  wire sat_sum_5_;
  wire sat_sum_6_;
  wire sat_sum_7_;
  
  
  nand (_025_, A_3_, A_3_);
  
  
  nand (_026_, B_3_, B_3_);
  
  
  nand (_027_, A_2_, A_2_);
  
  
  nand (_028_, B_2_, B_2_);
  
  
  nand (_029_, A_1_, A_1_);
  
  
  nand (_030_, B_1_, B_1_);
  
  
  nand (_031_, A_0_, A_0_);
  
  
  nand (_032_, B_0_, B_0_);
  
  
  nand (_033_, A_7_, A_7_);
  
  
  nand (_034_, B_7_, B_7_);
  
  
  nand (_035_, A_6_, A_6_);
  
  
  nand (_036_, B_6_, B_6_);
  
  
  nand (_037_, A_5_, A_5_);
  
  
  nand (_038_, B_5_, B_5_);
  
  
  nand (_039_, A_4_, A_4_);
  
  
  nand (_040_, B_4_, B_4_);
  nand (_041_, A_6_, B_6_);
  nand (_042_, A_5_, B_5_);
  nand (_043_, A_4_, B_4_);
  nand (_044_, _039_, _040_);
  nand (_045_, _043_, _044_);
  
  
  nand (_046_, _045_, _045_);
  nand (_047_, A_3_, B_3_);
  nand (_048_, _025_, _026_);
  nand (_049_, A_2_, B_2_);
  nand (_050_, _027_, _028_);
  nand (_051_, A_1_, B_1_);
  nand (_052_, _029_, _030_);
  nand (_053_, A_0_, B_0_);
  
  
  nand (_054_, _053_, _053_);
  nand (_055_, _052_, _054_);
  nand (_056_, _051_, _053_);
  nand (_057_, _052_, _056_);
  nand (_058_, _051_, _055_);
  nand (_059_, _050_, _058_);
  nand (_060_, _049_, _057_);
  nand (_061_, _050_, _060_);
  nand (_062_, _049_, _059_);
  nand (_063_, _048_, _062_);
  nand (_064_, _047_, _061_);
  nand (_065_, _048_, _064_);
  nand (_066_, _047_, _063_);
  nand (_067_, _046_, _066_);
  nand (_068_, _043_, _067_);
  
  
  nand (_069_, _068_, _068_);
  nand (_070_, _037_, _038_);
  nand (_071_, _042_, _070_);
  
  
  nand (_072_, _071_, _071_);
  nand (_073_, _068_, _072_);
  nand (_074_, _042_, _073_);
  
  
  nand (_075_, _074_, _074_);
  nand (_076_, _035_, _036_);
  nand (_077_, _041_, _076_);
  
  
  nand (_078_, _077_, _077_);
  nand (_079_, _074_, _078_);
  nand (_080_, _041_, _079_);
  
  
  nand (_081_, _080_, _080_);
  nand (_082_, _033_, _034_);
  
  
  nand (_083_, _082_, _082_);
  nand (_084_, _080_, _083_);
  nand (_085_, _031_, _032_);
  nand (_086_, _053_, _085_);
  
  
  nand (_087_, _086_, _086_);
  nand (_088_, A_7_, B_7_);
  
  
  nand (_089_, _088_, _088_);
  nand (_090_, _081_, _089_);
  nand (_091_, _087_, _090_);
  nand (SUM_0_, _084_, _091_);
  nand (_092_, _051_, _052_);
  
  
  nand (_093_, _092_, _092_);
  nand (_094_, _054_, _093_);
  nand (_095_, _053_, _092_);
  nand (_096_, _094_, _095_);
  
  
  nand (_097_, _096_, _096_);
  nand (_098_, _090_, _097_);
  nand (SUM_1_, _084_, _098_);
  nand (_000_, _049_, _050_);
  
  
  nand (_001_, _000_, _000_);
  nand (_002_, _057_, _001_);
  nand (_003_, _058_, _000_);
  nand (_004_, _002_, _003_);
  nand (_005_, _090_, _004_);
  nand (SUM_2_, _084_, _005_);
  nand (_006_, _047_, _048_);
  
  
  nand (_007_, _006_, _006_);
  nand (_008_, _062_, _006_);
  nand (_009_, _061_, _007_);
  nand (_010_, _008_, _009_);
  nand (_011_, _090_, _010_);
  nand (SUM_3_, _084_, _011_);
  nand (_012_, _045_, _065_);
  nand (_013_, _067_, _012_);
  
  
  nand (_014_, _013_, _013_);
  nand (_015_, _090_, _014_);
  nand (SUM_4_, _084_, _015_);
  nand (_016_, _069_, _071_);
  nand (_017_, _073_, _016_);
  
  
  nand (_018_, _017_, _017_);
  nand (_019_, _090_, _018_);
  nand (SUM_5_, _084_, _019_);
  nand (_020_, _075_, _077_);
  nand (_021_, _079_, _020_);
  
  
  nand (_022_, _021_, _021_);
  nand (_023_, _090_, _022_);
  nand (SUM_6_, _084_, _023_);
  nand (_024_, _081_, _082_);
  nand (SUM_7_, _088_, _024_);
  assign _cla1.CIN  = 1'h0;
  assign _cla1.B_0_ = B_0_;
  assign _cla1.B_1_ = B_1_;
  assign _cla1.B_2_ = B_2_;
  assign _cla1.B_3_ = B_3_;
  assign _cla1.A_0_ = A_0_;
  assign _cla1.A_1_ = A_1_;
  assign _cla1.A_2_ = A_2_;
  assign _cla1.A_3_ = A_3_;
  assign _cla1.fa3.a  = A_3_;
  assign _cla1.fa3.b  = B_3_;
  assign _cla1.fa2.a  = A_2_;
  assign _cla1.fa2.b  = B_2_;
  assign _cla1.fa1.a  = A_1_;
  assign _cla1.fa1.b  = B_1_;
  assign _cla1.fa0.a  = A_0_;
  assign _cla1.fa0.b  = B_0_;
  assign _cla1.fa0.cin  = 1'h0;
  assign _cla2.B_0_ = B_4_;
  assign _cla2.B_1_ = B_5_;
  assign _cla2.B_2_ = B_6_;
  assign _cla2.B_3_ = B_7_;
  assign _cla2.A_0_ = A_4_;
  assign _cla2.A_1_ = A_5_;
  assign _cla2.A_2_ = A_6_;
  assign _cla2.A_3_ = A_7_;
  assign _cla2.fa3.a  = A_7_;
  assign _cla2.fa3.b  = B_7_;
  assign _cla2.fa2.a  = A_6_;
  assign _cla2.fa2.b  = B_6_;
  assign _cla2.fa1.a  = A_5_;
  assign _cla2.fa1.b  = B_5_;
  assign _cla2.fa0.a  = A_4_;
  assign _cla2.fa0.b  = B_4_;
  assign sat_sum_7_ = A_7_;
  assign sat_sum_5_ = sat_sum_6_;
  assign sat_sum_4_ = sat_sum_6_;
  assign sat_sum_3_ = sat_sum_6_;
  assign sat_sum_2_ = sat_sum_6_;
  assign sat_sum_1_ = sat_sum_6_;
  assign sat_sum_0_ = sat_sum_6_;
endmodule
