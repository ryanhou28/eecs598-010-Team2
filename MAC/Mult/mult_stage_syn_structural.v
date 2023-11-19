



module mult_stage( reset, start, mplier_in_0_, mplier_in_1_, mplier_in_2_, mplier_in_3_, mplier_in_4_, mplier_in_5_, mplier_in_6_, mplier_in_7_, mcand_in_0_, mcand_in_1_, mcand_in_2_, mcand_in_3_, mcand_in_4_, mcand_in_5_, mcand_in_6_, mcand_in_7_, product_in_0_, product_in_1_, product_in_2_, product_in_3_, product_in_4_, product_in_5_, product_in_6_, product_in_7_, done, mplier_out_0_, mplier_out_1_, mplier_out_2_, mplier_out_3_, mplier_out_4_, mplier_out_5_, mplier_out_6_, mplier_out_7_, mcand_out_0_, mcand_out_1_, mcand_out_2_, mcand_out_3_, mcand_out_4_, mcand_out_5_, mcand_out_6_, mcand_out_7_, product_out_0_, product_out_1_, product_out_2_, product_out_3_, product_out_4_, product_out_5_, product_out_6_, product_out_7_);
  output done;
  
  input mcand_in_0_;
  input mcand_in_1_;
  input reset;
  input start;
  input mcand_in_2_;
  input mcand_in_3_;
  input mcand_in_4_;
  input mcand_in_5_;
  input mcand_in_6_;
  input mcand_in_7_;
  input mplier_in_0_;
  input mplier_in_1_;
  input mplier_in_2_;
  input mplier_in_3_;
  input mplier_in_4_;
  input mplier_in_5_;
  input mplier_in_6_;
  input mplier_in_7_;
  input product_in_0_;
  input product_in_1_;
  input product_in_2_;
  input product_in_3_;
  input product_in_4_;
  input product_in_5_;
  input product_in_6_;
  input product_in_7_;
  output mcand_out_0_;
  output mcand_out_1_;
  output mcand_out_2_;
  output mcand_out_3_;
  output mcand_out_4_;
  output mcand_out_5_;
  output mcand_out_6_;
  output mcand_out_7_;
  output product_out_0_;
  output product_out_1_;
  output product_out_2_;
  output product_out_3_;
  output product_out_4_;
  output product_out_5_;
  output product_out_6_;
  output product_out_7_;
  output mplier_out_0_;
  output mplier_out_1_;
  output mplier_out_2_;
  output mplier_out_3_;
  output mplier_out_4_;
  output mplier_out_5_;
  output mplier_out_6_;
  output mplier_out_7_;
  reg partial_prod_0_;
  reg partial_prod_1_;
  reg partial_prod_2_;
  reg partial_prod_3_;
  reg partial_prod_4_;
  reg partial_prod_5_;
  reg partial_prod_6_;
  reg partial_prod_7_;
  
  reg prod_in_reg_0_;
  reg prod_in_reg_1_;
  reg prod_in_reg_2_;
  reg prod_in_reg_3_;
  reg prod_in_reg_4_;
  reg prod_in_reg_5_;
  reg prod_in_reg_6_;
  reg prod_in_reg_7_;
  reg _mplier_out_reg_3_ ;
  
  reg _mplier_out_reg_2_ ;
  reg _mplier_out_reg_1_ ;
  reg _mplier_out_reg_5_ ;

  reg _mplier_out_reg_0_ ;
  reg _mplier_out_reg_4_ ;
  reg done;
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
  wire _099_;
  wire _100_;
  wire _101_;
  wire _102_;
  wire _103_;
  wire _104_;
  wire _105_;
  wire _106_;
  wire _107_;
  wire _108_;
  wire _109_;
  wire _110_;
  wire _111_;
  wire _112_;
  wire _113_;
  wire _114_;
  wire _115_;
  wire _116_;
  wire _117_;
  wire _118_;
  wire _119_;
  wire _120_;
  wire _121_;
  wire _122_;
  wire _123_;
  wire _124_;
  wire _125_;
  wire _126_;
  wire _127_;
  wire _128_;
  wire _129_;
  wire _130_;
  wire _131_;
  wire _132_;
  wire _133_;
  wire _134_;
  wire _135_;
  wire _136_;
  wire _137_;
  wire _138_;
  wire _139_;
  wire _140_;
  wire _141_;
  wire _142_;
  wire _143_;
  wire _144_;
  wire _145_;
  wire _146_;
  wire _147_;
  wire _148_;
  wire _149_;
  wire _150_;
  wire _151_;
  wire _152_;
  wire _153_;
  wire _154_;
  wire _155_;
  wire _156_;
  wire _157_;
  wire _158_;
  wire _159_;
  wire _160_;
  wire _161_;
  wire _162_;
  wire _163_;
  
  wire clock;
  
  
  wire mcand_in_0_;
  wire mcand_in_1_;
  wire mcand_in_2_;
  wire mcand_in_3_;
  wire mcand_in_4_;
  wire mcand_in_5_;
  wire mcand_in_6_;
  wire mcand_in_7_;
  
  wire mcand_out_0_;
  wire mcand_out_1_;
  wire mcand_out_2_;
  wire mcand_out_3_;
  wire mcand_out_4_;
  wire mcand_out_5_;
  wire mcand_out_6_;
  wire mcand_out_7_;
  
  wire mplier_in_0_;
  wire mplier_in_1_;
  wire mplier_in_2_;
  wire mplier_in_3_;
  wire mplier_in_4_;
  wire mplier_in_5_;
  wire mplier_in_6_;
  wire mplier_in_7_;
  
  wire mplier_out_0_;
  wire mplier_out_1_;
  wire mplier_out_2_;
  wire mplier_out_3_;
  wire mplier_out_4_;
  wire mplier_out_5_;
  wire mplier_out_6_;
  wire mplier_out_7_;
  
  wire next_mcand_0_;
  wire next_mcand_1_;
  wire next_mcand_2_;
  wire next_mcand_3_;
  wire next_mcand_4_;
  wire next_mcand_5_;
  wire next_mcand_6_;
  wire next_mcand_7_;
  
  wire next_mplier_0_;
  wire next_mplier_1_;
  wire next_mplier_2_;
  wire next_mplier_3_;
  wire next_mplier_4_;
  wire next_mplier_5_;
  wire next_mplier_6_;
  wire next_mplier_7_;
  
  wire next_partial_product_0_;
  wire next_partial_product_1_;
  wire next_partial_product_2_;
  wire next_partial_product_3_;
  wire next_partial_product_4_;
  wire next_partial_product_5_;
  wire next_partial_product_6_;
  wire next_partial_product_7_;
  
  wire product_in_0_;
  wire product_in_1_;
  wire product_in_2_;
  wire product_in_3_;
  wire product_in_4_;
  wire product_in_5_;
  wire product_in_6_;
  wire product_in_7_;
  
  wire product_out_0_;
  wire product_out_1_;
  wire product_out_2_;
  wire product_out_3_;
  wire product_out_4_;
  wire product_out_5_;
  wire product_out_6_;
  wire product_out_7_;
  
  wire reset;
  
  wire start;
  
  
  nand (_115_, reset, reset);
  
  
  nand (_116_, prod_in_reg_0_, prod_in_reg_0_);
  
  
  nand (_117_, partial_prod_0_, partial_prod_0_);
  
  
  nand (_118_, prod_in_reg_1_, prod_in_reg_1_);
  
  
  nand (_119_, partial_prod_1_, partial_prod_1_);
  
  
  nand (_120_, prod_in_reg_2_, prod_in_reg_2_);
  
  
  nand (_121_, partial_prod_2_, partial_prod_2_);
  
  
  nand (_122_, prod_in_reg_3_, prod_in_reg_3_);
  
  
  nand (_123_, partial_prod_3_, partial_prod_3_);
  
  
  nand (_124_, prod_in_reg_4_, prod_in_reg_4_);
  
  
  nand (_125_, partial_prod_4_, partial_prod_4_);
  
  
  nand (_126_, prod_in_reg_5_, prod_in_reg_5_);
  
  
  nand (_127_, partial_prod_5_, partial_prod_5_);
  
  
  nand (_128_, prod_in_reg_6_, prod_in_reg_6_);
  
  
  nand (_129_, partial_prod_6_, partial_prod_6_);
  
  
  nand (_130_, prod_in_reg_7_, prod_in_reg_7_);
  
  
  nand (_131_, partial_prod_7_, partial_prod_7_);
  nand (_132_, start, _115_);
  
  
  nand (_000_, _132_, _132_);
  nand (_133_, mcand_in_0_, mplier_in_0_);
  
  
  nand (next_partial_product_0_, _133_, _133_);
  nand (_134_, prod_in_reg_0_, partial_prod_0_);
  
  
  nand (_135_, _134_, _134_);
  nand (_136_, prod_in_reg_1_, partial_prod_1_);
  nand (_137_, _118_, _119_);
  nand (_138_, _136_, _137_);
  
  
  nand (_139_, _138_, _138_);
  nand (_140_, _135_, _139_);
  nand (_141_, _134_, _138_);
  nand (_142_, _140_, _141_);
  
  
  nand (product_out_1_, _142_, _142_);
  nand (_143_, _136_, _140_);
  
  
  nand (_144_, _143_, _143_);
  nand (_145_, prod_in_reg_2_, partial_prod_2_);
  nand (_146_, _120_, _121_);
  nand (_147_, _145_, _146_);
  
  
  nand (_148_, _147_, _147_);
  nand (_149_, _143_, _148_);
  nand (_150_, _144_, _147_);
  nand (_151_, _149_, _150_);
  
  
  nand (product_out_2_, _151_, _151_);
  nand (_152_, _145_, _149_);
  
  
  nand (_153_, _152_, _152_);
  nand (_154_, prod_in_reg_3_, partial_prod_3_);
  nand (_155_, _122_, _123_);
  nand (_156_, _154_, _155_);
  
  
  nand (_157_, _156_, _156_);
  nand (_158_, _152_, _157_);
  nand (_159_, _153_, _156_);
  nand (_160_, _158_, _159_);
  
  
  nand (product_out_3_, _160_, _160_);
  nand (_161_, _154_, _158_);
  
  
  nand (_162_, _161_, _161_);
  nand (_163_, prod_in_reg_4_, partial_prod_4_);
  nand (_001_, _124_, _125_);
  nand (_002_, _163_, _001_);
  
  
  nand (_003_, _002_, _002_);
  nand (_004_, _161_, _003_);
  nand (_005_, _162_, _002_);
  nand (_006_, _004_, _005_);
  
  
  nand (product_out_4_, _006_, _006_);
  nand (_007_, _163_, _004_);
  
  
  nand (_008_, _007_, _007_);
  nand (_009_, prod_in_reg_5_, partial_prod_5_);
  nand (_010_, _126_, _127_);
  nand (_011_, _009_, _010_);
  
  
  nand (_012_, _011_, _011_);
  nand (_013_, _007_, _012_);
  nand (_014_, _008_, _011_);
  nand (_015_, _013_, _014_);
  
  
  nand (product_out_5_, _015_, _015_);
  nand (_016_, _009_, _013_);
  
  
  nand (_017_, _016_, _016_);
  nand (_018_, prod_in_reg_6_, partial_prod_6_);
  nand (_019_, _128_, _129_);
  nand (_020_, _018_, _019_);
  
  
  nand (_021_, _020_, _020_);
  nand (_022_, _016_, _021_);
  nand (_023_, _017_, _020_);
  nand (_024_, _022_, _023_);
  
  
  nand (product_out_6_, _024_, _024_);
  nand (_025_, _018_, _022_);
  
  
  nand (_026_, _025_, _025_);
  nand (_027_, prod_in_reg_7_, _131_);
  nand (_028_, _130_, partial_prod_7_);
  nand (_029_, _130_, _131_);
  nand (_030_, prod_in_reg_7_, partial_prod_7_);
  nand (_031_, _029_, _030_);
  nand (_032_, _027_, _028_);
  nand (_033_, _026_, _032_);
  nand (_034_, _025_, _031_);
  nand (product_out_7_, _033_, _034_);
  nand (_035_, _116_, _117_);
  nand (_036_, _134_, _035_);
  
  
  nand (product_out_0_, _036_, _036_);
  nand (_037_, mplier_in_0_, mcand_in_1_);
  nand (_038_, mcand_in_0_, mplier_in_1_);
  nand (_039_, mcand_in_1_, mplier_in_1_);
  
  
  nand (_040_, _039_, _039_);
  nand (_041_, next_partial_product_0_, _040_);
  
  
  nand (_042_, _041_, _041_);
  nand (_043_, mplier_in_0_, mcand_in_2_);
  
  
  nand (_044_, _043_, _043_);
  nand (_045_, mcand_in_2_, mplier_in_1_);
  
  
  nand (_046_, _045_, _045_);
  nand (_047_, _040_, _044_);
  nand (_048_, _039_, _043_);
  nand (_049_, _047_, _048_);
  
  
  nand (_050_, _049_, _049_);
  nand (_051_, _042_, _050_);
  nand (_052_, _041_, _049_);
  nand (_053_, _051_, _052_);
  
  
  nand (next_partial_product_2_, _053_, _053_);
  nand (_054_, _047_, _051_);
  
  
  nand (_055_, _054_, _054_);
  nand (_056_, mplier_in_0_, mcand_in_3_);
  
  
  nand (_057_, _056_, _056_);
  nand (_058_, mcand_in_3_, mplier_in_1_);
  nand (_059_, _046_, _057_);
  nand (_060_, _045_, _056_);
  nand (_061_, _059_, _060_);
  
  
  nand (_062_, _061_, _061_);
  nand (_063_, _054_, _062_);
  nand (_064_, _055_, _061_);
  nand (_065_, _063_, _064_);
  
  
  nand (next_partial_product_3_, _065_, _065_);
  nand (_066_, _059_, _063_);
  
  
  nand (_067_, _066_, _066_);
  nand (_068_, mplier_in_0_, mcand_in_4_);
  nand (_069_, mcand_in_4_, mplier_in_1_);
  
  
  nand (_070_, _069_, _069_);
  nand (_071_, _057_, _070_);
  nand (_072_, _058_, _068_);
  nand (_073_, _071_, _072_);
  
  
  nand (_074_, _073_, _073_);
  nand (_075_, _066_, _074_);
  nand (_076_, _067_, _073_);
  nand (_077_, _075_, _076_);
  
  
  nand (next_partial_product_4_, _077_, _077_);
  nand (_078_, _071_, _075_);
  
  
  nand (_079_, _078_, _078_);
  nand (_080_, mplier_in_0_, mcand_in_5_);
  
  
  nand (_081_, _080_, _080_);
  nand (_082_, mcand_in_5_, mplier_in_1_);
  nand (_083_, _070_, _081_);
  nand (_084_, _069_, _080_);
  nand (_085_, _083_, _084_);
  
  
  nand (_086_, _085_, _085_);
  nand (_087_, _078_, _086_);
  nand (_088_, _079_, _085_);
  nand (_089_, _087_, _088_);
  
  
  nand (next_partial_product_5_, _089_, _089_);
  nand (_090_, _083_, _087_);
  
  
  nand (_091_, _090_, _090_);
  nand (_092_, mplier_in_0_, mcand_in_6_);
  nand (_093_, mcand_in_6_, mplier_in_1_);
  
  
  nand (_094_, _093_, _093_);
  nand (_095_, _081_, _094_);
  nand (_096_, _082_, _092_);
  nand (_097_, _095_, _096_);
  
  
  nand (_098_, _097_, _097_);
  nand (_099_, _090_, _098_);
  nand (_100_, _091_, _097_);
  nand (_101_, _099_, _100_);
  
  
  nand (next_partial_product_6_, _101_, _101_);
  nand (_102_, _095_, _099_);
  
  
  nand (_103_, _102_, _102_);
  nand (_104_, mplier_in_0_, mcand_in_7_);
  
  
  nand (_105_, _104_, _104_);
  nand (_106_, _093_, _105_);
  nand (_107_, _094_, _104_);
  nand (_108_, _106_, _107_);
  
  
  nand (_109_, _108_, _108_);
  nand (_110_, _103_, _109_);
  nand (_111_, _102_, _108_);
  nand (_112_, _110_, _111_);
  
  
  nand (next_partial_product_7_, _112_, _112_);
  nand (_113_, _037_, _038_);
  nand (_114_, _041_, _113_);
  
  
  nand (next_partial_product_1_, _114_, _114_);
  
  always @(posedge clock)
    _mplier_out_reg_3_  <= mplier_in_5_;
  assign mplier_out_3_ = _mplier_out_reg_3_ ;
  
  always @(posedge clock)
    _mplier_out_reg_4_  <= mplier_in_6_;
  assign mplier_out_4_ = _mplier_out_reg_4_ ;
  
  always @(posedge clock)
    _mplier_out_reg_5_  <= mplier_in_7_;
  assign mplier_out_5_ = _mplier_out_reg_5_ ;
  
  always @(posedge clock)
    prod_in_reg_0_ <= product_in_0_;
  
  always @(posedge clock)
    prod_in_reg_1_ <= product_in_1_;
  
  always @(posedge clock)
    prod_in_reg_2_ <= product_in_2_;
  
  always @(posedge clock)
    prod_in_reg_3_ <= product_in_3_;
  
  always @(posedge clock)
    prod_in_reg_4_ <= product_in_4_;
  
  always @(posedge clock)
    prod_in_reg_5_ <= product_in_5_;
  
  always @(posedge clock)
    prod_in_reg_6_ <= product_in_6_;
  
  always @(posedge clock)
    prod_in_reg_7_ <= product_in_7_;
  
  always @(posedge clock)
    partial_prod_0_ <= next_partial_product_0_;
  
  always @(posedge clock)
    partial_prod_1_ <= next_partial_product_1_;
  
  always @(posedge clock)
    partial_prod_2_ <= next_partial_product_2_;
  
  always @(posedge clock)
    partial_prod_3_ <= next_partial_product_3_;
  
  always @(posedge clock)
    partial_prod_4_ <= next_partial_product_4_;
  
  always @(posedge clock)
    partial_prod_5_ <= next_partial_product_5_;
  
  always @(posedge clock)
    partial_prod_6_ <= next_partial_product_6_;
  
  always @(posedge clock)
    partial_prod_7_ <= next_partial_product_7_;
  
  always @(posedge clock)
    done <= _000_;
  
  always @(posedge clock)
    _mplier_out_reg_0_  <= mplier_in_2_;
  assign mplier_out_0_ = _mplier_out_reg_0_ ;
  
  always @(posedge clock)
    _mplier_out_reg_1_  <= mplier_in_3_;
  assign mplier_out_1_ = _mplier_out_reg_1_ ;
  
  always @(posedge clock)
    _mplier_out_reg_2_  <= mplier_in_4_;
  assign mplier_out_2_ = _mplier_out_reg_2_ ;

  assign mcand_out_0_ = 1'h0;
  assign mcand_out_1_ = 1'h0;
  assign mcand_out_2_ = 1'h0;
  assign mcand_out_3_ = 1'h0;
  assign mcand_out_4_ = 1'h0;
  assign mcand_out_5_ = 1'h0;
  assign mcand_out_6_ = 1'h0;
  assign mcand_out_7_ = 1'h0;

  assign mplier_out_6_ = 1'h0;
  assign mplier_out_7_ = 1'h0;

  assign next_mcand_0_ = 1'h0;
  assign next_mcand_1_ = 1'h0;
  assign next_mcand_2_ = 1'h0;
  assign next_mcand_3_ = 1'h0;
  assign next_mcand_4_ = 1'h0;
  assign next_mcand_5_ = 1'h0;
  assign next_mcand_6_ = 1'h0;
  assign next_mcand_7_ = 1'h0;

  assign next_mplier_0_ = mplier_in_2_;
  assign next_mplier_1_ = mplier_in_3_;
  assign next_mplier_2_ = mplier_in_4_;
  assign next_mplier_3_ = mplier_in_5_;
  assign next_mplier_4_ = mplier_in_6_;
  assign next_mplier_5_ = mplier_in_7_;
  assign next_mplier_6_ = 1'h0;
  assign next_mplier_7_ = 1'h0;
endmodule
