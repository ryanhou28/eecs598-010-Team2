



module adder8(A, B, SUM);
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
  wire _099_;
  wire _100_;
  wire _101_;
  wire _102_;
  
  input [7:0] A;
  wire [7:0] A;
  
  input [7:0] B;
  wire [7:0] B;
  
  output [7:0] SUM;
  wire [7:0] SUM;
  
  
  wire [3:0] hcla1_A ;
  
  
  wire [3:0] hcla1_B ;
  
  
  wire hcla1_CIN ;
  
  
  wire hcla1_fa0_a ;
  
  
  wire hcla1_fa0_b ;
  
  
  wire hcla1_fa0_cin ;
  
  
  wire hcla1_fa1_a ;
  
  
  wire hcla1_fa1_b ;
  
  
  wire hcla1_fa2_a ;
  
  
  wire hcla1_fa2_b ;
  
  
  wire hcla1_fa3_a ;
  
  
  wire hcla1_fa3_b ;
  
  
  wire [3:0] hcla2_A ;
  
  
  wire [3:0] hcla2_B ;
  
  
  wire hcla2_fa0_a ;
  
  
  wire hcla2_fa0_b ;
  
  
  wire hcla2_fa1_a ;
  
  
  wire hcla2_fa1_b ;
  
  
  wire hcla2_fa2_a ;
  
  
  wire hcla2_fa2_b ;
  
  
  wire hcla2_fa3_a ;
  
  
  wire hcla2_fa3_b ;
  
  
  wire [7:0] sat_sum;
  
  
  nand (_029_, A[3], A[3]);
  
  
  nand (_030_, B[3], B[3]);
  
  
  nand (_031_, A[2], A[2]);
  
  
  nand (_032_, B[2], B[2]);
  
  
  nand (_033_, A[1], A[1]);
  
  
  nand (_034_, B[1], B[1]);
  
  
  nand (_035_, A[0], A[0]);
  
  
  nand (_036_, B[0], B[0]);
  
  
  nand (_037_, A[7], A[7]);
  
  
  nand (_038_, B[7], B[7]);
  
  
  nand (_039_, A[6], A[6]);
  
  
  nand (_040_, B[6], B[6]);
  
  
  nand (_041_, A[5], A[5]);
  
  
  nand (_042_, B[5], B[5]);
  
  
  nand (_043_, A[4], A[4]);
  
  
  nand (_044_, B[4], B[4]);
  nand (_045_, A[7], _038_);
  nand (_046_, A[6], B[6]);
  nand (_047_, A[5], B[5]);
  nand (_048_, A[4], B[4]);
  nand (_049_, _043_, _044_);
  nand (_050_, _048_, _049_);
  
  
  nand (_051_, _050_, _050_);
  nand (_052_, A[3], B[3]);
  nand (_053_, _029_, _030_);
  nand (_054_, A[2], B[2]);
  nand (_055_, _031_, _032_);
  nand (_056_, A[1], B[1]);
  nand (_057_, _033_, _034_);
  nand (_058_, A[0], B[0]);
  
  
  nand (_059_, _058_, _058_);
  nand (_060_, _057_, _059_);
  nand (_061_, _056_, _058_);
  nand (_062_, _057_, _061_);
  nand (_063_, _056_, _060_);
  nand (_064_, _055_, _063_);
  nand (_065_, _054_, _062_);
  nand (_066_, _055_, _065_);
  nand (_067_, _054_, _064_);
  nand (_068_, _053_, _067_);
  nand (_069_, _052_, _066_);
  nand (_070_, _053_, _069_);
  nand (_071_, _052_, _068_);
  nand (_072_, _051_, _071_);
  nand (_073_, _048_, _072_);
  
  
  nand (_074_, _073_, _073_);
  nand (_075_, _041_, _042_);
  nand (_076_, _047_, _075_);
  
  
  nand (_077_, _076_, _076_);
  nand (_078_, _073_, _077_);
  nand (_079_, _047_, _078_);
  
  
  nand (_080_, _079_, _079_);
  nand (_081_, _039_, _040_);
  nand (_082_, _046_, _081_);
  
  
  nand (_083_, _082_, _082_);
  nand (_084_, _079_, _083_);
  nand (_085_, _046_, _084_);
  
  
  nand (_086_, _085_, _085_);
  nand (_087_, B[7], _085_);
  nand (_088_, _045_, _087_);
  
  
  nand (_089_, _088_, _088_);
  nand (_090_, A[7], _089_);
  nand (_091_, _037_, _086_);
  nand (_092_, _089_, _091_);
  nand (_093_, _035_, _036_);
  nand (_094_, _058_, _093_);
  
  
  nand (_095_, _094_, _094_);
  nand (_096_, _092_, _095_);
  nand (SUM[0], _090_, _096_);
  nand (_097_, _056_, _057_);
  
  
  nand (_098_, _097_, _097_);
  nand (_099_, _058_, _098_);
  nand (_100_, _059_, _097_);
  nand (_101_, _099_, _100_);
  nand (_102_, _092_, _101_);
  nand (SUM[1], _090_, _102_);
  nand (_000_, _054_, _055_);
  
  
  nand (_001_, _000_, _000_);
  nand (_002_, _062_, _001_);
  nand (_003_, _063_, _000_);
  nand (_004_, _002_, _003_);
  nand (_005_, _092_, _004_);
  nand (SUM[2], _090_, _005_);
  nand (_006_, _052_, _053_);
  
  
  nand (_007_, _006_, _006_);
  nand (_008_, _066_, _007_);
  nand (_009_, _067_, _006_);
  nand (_010_, _008_, _009_);
  nand (_011_, _092_, _010_);
  nand (SUM[3], _090_, _011_);
  nand (_012_, _050_, _070_);
  nand (_013_, _072_, _012_);
  
  
  nand (_014_, _013_, _013_);
  nand (_015_, _092_, _014_);
  nand (SUM[4], _090_, _015_);
  nand (_016_, _074_, _076_);
  nand (_017_, _078_, _016_);
  
  
  nand (_018_, _017_, _017_);
  nand (_019_, _092_, _018_);
  nand (SUM[5], _090_, _019_);
  nand (_020_, _080_, _082_);
  nand (_021_, _084_, _020_);
  
  
  nand (_022_, _021_, _021_);
  nand (_023_, _092_, _022_);
  nand (SUM[6], _090_, _023_);
  nand (_024_, _037_, B[7]);
  nand (_025_, _045_, _024_);
  
  
  nand (_026_, _025_, _025_);
  nand (_027_, _086_, _025_);
  nand (_028_, _085_, _026_);
  nand (SUM[7], _027_, _028_);
  assign hcla1_CIN  = 1'h0;
  assign hcla1_B[0] = B[0];
  assign hcla1_B[1] = B[1];
  assign hcla1_B[2] = B[2];
  assign hcla1_B[3] = B[3];
  assign hcla1_A[0] = A[0];
  assign hcla1_A[1] = A[1];
  assign hcla1_A[2] = A[2];
  assign hcla1_A[3] = A[3];
  assign hcla1_fa3_a  = A[3];
  assign hcla1_fa3_b  = B[3];
  assign hcla1_fa2_a  = A[2];
  assign hcla1_fa2_b  = B[2];
  assign hcla1_fa1_a  = A[1];
  assign hcla1_fa1_b  = B[1];
  assign hcla1_fa0_a  = A[0];
  assign hcla1_fa0_b  = B[0];
  assign hcla1_fa0_cin  = 1'h0;
  assign hcla2_B[0] = B[4];
  assign hcla2_B[1] = B[5];
  assign hcla2_B[2] = B[6];
  assign hcla2_B[3] = B[7];
  assign hcla2_A[0] = A[4];
  assign hcla2_A[1] = A[5];
  assign hcla2_A[2] = A[6];
  assign hcla2_A[3] = A[7];
  assign hcla2_fa3_a  = A[7];
  assign hcla2_fa3_b  = B[7];
  assign hcla2_fa2_a  = A[6];
  assign hcla2_fa2_b  = B[6];
  assign hcla2_fa1_a  = A[5];
  assign hcla2_fa1_b  = B[5];
  assign hcla2_fa0_a  = A[4];
  assign hcla2_fa0_b  = B[4];
  assign sat_sum[0] = A[7];
  assign sat_sum[1] = A[7];
  assign sat_sum[2] = A[7];
  assign sat_sum[3] = A[7];
  assign sat_sum[4] = A[7];
  assign sat_sum[5] = A[7];
  assign sat_sum[6] = A[7];
endmodule
