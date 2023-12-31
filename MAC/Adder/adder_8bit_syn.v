/* Generated by Yosys 0.25+99 (git sha1 54bf15a5b, x86_64-apple-darwin20.2-clang 10.0.0-4ubuntu1 -fPIC -Os) */

(* top =  1  *)
(* src = "adder_8bit.v:1.1-19.10" *)
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
  (* src = "adder_8bit.v:2.17-2.18" *)
  input [7:0] A;
  wire [7:0] A;
  (* src = "adder_8bit.v:3.17-3.18" *)
  input [7:0] B;
  wire [7:0] B;
  (* src = "adder_8bit.v:4.18-4.21" *)
  output [7:0] SUM;
  wire [7:0] SUM;
  (* hdlname = "cla1 A" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:23.17-23.18" *)
  wire [3:0] \cla1.A ;
  (* hdlname = "cla1 B" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:24.17-24.18" *)
  wire [3:0] \cla1.B ;
  (* hdlname = "cla1 CIN" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:25.11-25.14" *)
  wire \cla1.CIN ;
  (* hdlname = "cla1 fa0 a" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.11-57.12|adder_8bit.v:32.16-32.77" *)
  wire \cla1.fa0.a ;
  (* hdlname = "cla1 fa0 b" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.13-57.14|adder_8bit.v:32.16-32.77" *)
  wire \cla1.fa0.b ;
  (* hdlname = "cla1 fa0 cin" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.15-57.18|adder_8bit.v:32.16-32.77" *)
  wire \cla1.fa0.cin ;
  (* hdlname = "cla1 fa1 a" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.11-57.12|adder_8bit.v:33.16-33.78" *)
  wire \cla1.fa1.a ;
  (* hdlname = "cla1 fa1 b" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.13-57.14|adder_8bit.v:33.16-33.78" *)
  wire \cla1.fa1.b ;
  (* hdlname = "cla1 fa2 a" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.11-57.12|adder_8bit.v:34.16-34.78" *)
  wire \cla1.fa2.a ;
  (* hdlname = "cla1 fa2 b" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.13-57.14|adder_8bit.v:34.16-34.78" *)
  wire \cla1.fa2.b ;
  (* hdlname = "cla1 fa3 a" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.11-57.12|adder_8bit.v:35.16-35.74" *)
  wire \cla1.fa3.a ;
  (* hdlname = "cla1 fa3 b" *)
  (* src = "adder_8bit.v:11.10-11.83|adder_8bit.v:57.13-57.14|adder_8bit.v:35.16-35.74" *)
  wire \cla1.fa3.b ;
  (* hdlname = "cla2 A" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:23.17-23.18" *)
  wire [3:0] \cla2.A ;
  (* hdlname = "cla2 B" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:24.17-24.18" *)
  wire [3:0] \cla2.B ;
  (* hdlname = "cla2 fa0 a" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.11-57.12|adder_8bit.v:32.16-32.77" *)
  wire \cla2.fa0.a ;
  (* hdlname = "cla2 fa0 b" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.13-57.14|adder_8bit.v:32.16-32.77" *)
  wire \cla2.fa0.b ;
  (* hdlname = "cla2 fa1 a" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.11-57.12|adder_8bit.v:33.16-33.78" *)
  wire \cla2.fa1.a ;
  (* hdlname = "cla2 fa1 b" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.13-57.14|adder_8bit.v:33.16-33.78" *)
  wire \cla2.fa1.b ;
  (* hdlname = "cla2 fa2 a" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.11-57.12|adder_8bit.v:34.16-34.78" *)
  wire \cla2.fa2.a ;
  (* hdlname = "cla2 fa2 b" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.13-57.14|adder_8bit.v:34.16-34.78" *)
  wire \cla2.fa2.b ;
  (* hdlname = "cla2 fa3 a" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.11-57.12|adder_8bit.v:35.16-35.74" *)
  wire \cla2.fa3.a ;
  (* hdlname = "cla2 fa3 b" *)
  (* src = "adder_8bit.v:12.10-12.83|adder_8bit.v:57.13-57.14|adder_8bit.v:35.16-35.74" *)
  wire \cla2.fa3.b ;
  (* src = "adder_8bit.v:10.16-10.23" *)
  (* unused_bits = "0 1 2 3 4 5 6" *)
  wire [7:0] sat_sum;
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _099_ (
    .A(A[3]),
    .B(A[3]),
    .Y(_025_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _100_ (
    .A(B[3]),
    .B(B[3]),
    .Y(_026_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _101_ (
    .A(A[2]),
    .B(A[2]),
    .Y(_027_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _102_ (
    .A(B[2]),
    .B(B[2]),
    .Y(_028_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _103_ (
    .A(A[1]),
    .B(A[1]),
    .Y(_029_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _104_ (
    .A(B[1]),
    .B(B[1]),
    .Y(_030_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _105_ (
    .A(A[0]),
    .B(A[0]),
    .Y(_031_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _106_ (
    .A(B[0]),
    .B(B[0]),
    .Y(_032_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _107_ (
    .A(A[7]),
    .B(A[7]),
    .Y(_033_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _108_ (
    .A(B[7]),
    .B(B[7]),
    .Y(_034_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _109_ (
    .A(A[6]),
    .B(A[6]),
    .Y(_035_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _110_ (
    .A(B[6]),
    .B(B[6]),
    .Y(_036_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _111_ (
    .A(A[5]),
    .B(A[5]),
    .Y(_037_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _112_ (
    .A(B[5]),
    .B(B[5]),
    .Y(_038_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _113_ (
    .A(A[4]),
    .B(A[4]),
    .Y(_039_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _114_ (
    .A(B[4]),
    .B(B[4]),
    .Y(_040_)
  );
  NAND _115_ (
    .A(A[6]),
    .B(B[6]),
    .Y(_041_)
  );
  NAND _116_ (
    .A(A[5]),
    .B(B[5]),
    .Y(_042_)
  );
  NAND _117_ (
    .A(A[4]),
    .B(B[4]),
    .Y(_043_)
  );
  NAND _118_ (
    .A(_039_),
    .B(_040_),
    .Y(_044_)
  );
  NAND _119_ (
    .A(_043_),
    .B(_044_),
    .Y(_045_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _120_ (
    .A(_045_),
    .B(_045_),
    .Y(_046_)
  );
  NAND _121_ (
    .A(A[3]),
    .B(B[3]),
    .Y(_047_)
  );
  NAND _122_ (
    .A(_025_),
    .B(_026_),
    .Y(_048_)
  );
  NAND _123_ (
    .A(A[2]),
    .B(B[2]),
    .Y(_049_)
  );
  NAND _124_ (
    .A(_027_),
    .B(_028_),
    .Y(_050_)
  );
  NAND _125_ (
    .A(A[1]),
    .B(B[1]),
    .Y(_051_)
  );
  NAND _126_ (
    .A(_029_),
    .B(_030_),
    .Y(_052_)
  );
  NAND _127_ (
    .A(A[0]),
    .B(B[0]),
    .Y(_053_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _128_ (
    .A(_053_),
    .B(_053_),
    .Y(_054_)
  );
  NAND _129_ (
    .A(_052_),
    .B(_054_),
    .Y(_055_)
  );
  NAND _130_ (
    .A(_051_),
    .B(_053_),
    .Y(_056_)
  );
  NAND _131_ (
    .A(_052_),
    .B(_056_),
    .Y(_057_)
  );
  NAND _132_ (
    .A(_051_),
    .B(_055_),
    .Y(_058_)
  );
  NAND _133_ (
    .A(_050_),
    .B(_058_),
    .Y(_059_)
  );
  NAND _134_ (
    .A(_049_),
    .B(_057_),
    .Y(_060_)
  );
  NAND _135_ (
    .A(_050_),
    .B(_060_),
    .Y(_061_)
  );
  NAND _136_ (
    .A(_049_),
    .B(_059_),
    .Y(_062_)
  );
  NAND _137_ (
    .A(_048_),
    .B(_062_),
    .Y(_063_)
  );
  NAND _138_ (
    .A(_047_),
    .B(_061_),
    .Y(_064_)
  );
  NAND _139_ (
    .A(_048_),
    .B(_064_),
    .Y(_065_)
  );
  NAND _140_ (
    .A(_047_),
    .B(_063_),
    .Y(_066_)
  );
  NAND _141_ (
    .A(_046_),
    .B(_066_),
    .Y(_067_)
  );
  NAND _142_ (
    .A(_043_),
    .B(_067_),
    .Y(_068_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _143_ (
    .A(_068_),
    .B(_068_),
    .Y(_069_)
  );
  NAND _144_ (
    .A(_037_),
    .B(_038_),
    .Y(_070_)
  );
  NAND _145_ (
    .A(_042_),
    .B(_070_),
    .Y(_071_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _146_ (
    .A(_071_),
    .B(_071_),
    .Y(_072_)
  );
  NAND _147_ (
    .A(_068_),
    .B(_072_),
    .Y(_073_)
  );
  NAND _148_ (
    .A(_042_),
    .B(_073_),
    .Y(_074_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _149_ (
    .A(_074_),
    .B(_074_),
    .Y(_075_)
  );
  NAND _150_ (
    .A(_035_),
    .B(_036_),
    .Y(_076_)
  );
  NAND _151_ (
    .A(_041_),
    .B(_076_),
    .Y(_077_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _152_ (
    .A(_077_),
    .B(_077_),
    .Y(_078_)
  );
  NAND _153_ (
    .A(_074_),
    .B(_078_),
    .Y(_079_)
  );
  NAND _154_ (
    .A(_041_),
    .B(_079_),
    .Y(_080_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _155_ (
    .A(_080_),
    .B(_080_),
    .Y(_081_)
  );
  NAND _156_ (
    .A(_033_),
    .B(_034_),
    .Y(_082_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _157_ (
    .A(_082_),
    .B(_082_),
    .Y(_083_)
  );
  NAND _158_ (
    .A(_080_),
    .B(_083_),
    .Y(_084_)
  );
  NAND _159_ (
    .A(_031_),
    .B(_032_),
    .Y(_085_)
  );
  NAND _160_ (
    .A(_053_),
    .B(_085_),
    .Y(_086_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _161_ (
    .A(_086_),
    .B(_086_),
    .Y(_087_)
  );
  NAND _162_ (
    .A(A[7]),
    .B(B[7]),
    .Y(_088_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _163_ (
    .A(_088_),
    .B(_088_),
    .Y(_089_)
  );
  NAND _164_ (
    .A(_081_),
    .B(_089_),
    .Y(_090_)
  );
  NAND _165_ (
    .A(_087_),
    .B(_090_),
    .Y(_091_)
  );
  NAND _166_ (
    .A(_084_),
    .B(_091_),
    .Y(SUM[0])
  );
  NAND _167_ (
    .A(_051_),
    .B(_052_),
    .Y(_092_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _168_ (
    .A(_092_),
    .B(_092_),
    .Y(_093_)
  );
  NAND _169_ (
    .A(_054_),
    .B(_093_),
    .Y(_094_)
  );
  NAND _170_ (
    .A(_053_),
    .B(_092_),
    .Y(_095_)
  );
  NAND _171_ (
    .A(_094_),
    .B(_095_),
    .Y(_096_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _172_ (
    .A(_096_),
    .B(_096_),
    .Y(_097_)
  );
  NAND _173_ (
    .A(_090_),
    .B(_097_),
    .Y(_098_)
  );
  NAND _174_ (
    .A(_084_),
    .B(_098_),
    .Y(SUM[1])
  );
  NAND _175_ (
    .A(_049_),
    .B(_050_),
    .Y(_000_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _176_ (
    .A(_000_),
    .B(_000_),
    .Y(_001_)
  );
  NAND _177_ (
    .A(_057_),
    .B(_001_),
    .Y(_002_)
  );
  NAND _178_ (
    .A(_058_),
    .B(_000_),
    .Y(_003_)
  );
  NAND _179_ (
    .A(_002_),
    .B(_003_),
    .Y(_004_)
  );
  NAND _180_ (
    .A(_090_),
    .B(_004_),
    .Y(_005_)
  );
  NAND _181_ (
    .A(_084_),
    .B(_005_),
    .Y(SUM[2])
  );
  NAND _182_ (
    .A(_047_),
    .B(_048_),
    .Y(_006_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _183_ (
    .A(_006_),
    .B(_006_),
    .Y(_007_)
  );
  NAND _184_ (
    .A(_062_),
    .B(_006_),
    .Y(_008_)
  );
  NAND _185_ (
    .A(_061_),
    .B(_007_),
    .Y(_009_)
  );
  NAND _186_ (
    .A(_008_),
    .B(_009_),
    .Y(_010_)
  );
  NAND _187_ (
    .A(_090_),
    .B(_010_),
    .Y(_011_)
  );
  NAND _188_ (
    .A(_084_),
    .B(_011_),
    .Y(SUM[3])
  );
  NAND _189_ (
    .A(_045_),
    .B(_065_),
    .Y(_012_)
  );
  NAND _190_ (
    .A(_067_),
    .B(_012_),
    .Y(_013_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _191_ (
    .A(_013_),
    .B(_013_),
    .Y(_014_)
  );
  NAND _192_ (
    .A(_090_),
    .B(_014_),
    .Y(_015_)
  );
  NAND _193_ (
    .A(_084_),
    .B(_015_),
    .Y(SUM[4])
  );
  NAND _194_ (
    .A(_069_),
    .B(_071_),
    .Y(_016_)
  );
  NAND _195_ (
    .A(_073_),
    .B(_016_),
    .Y(_017_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _196_ (
    .A(_017_),
    .B(_017_),
    .Y(_018_)
  );
  NAND _197_ (
    .A(_090_),
    .B(_018_),
    .Y(_019_)
  );
  NAND _198_ (
    .A(_084_),
    .B(_019_),
    .Y(SUM[5])
  );
  NAND _199_ (
    .A(_075_),
    .B(_077_),
    .Y(_020_)
  );
  NAND _200_ (
    .A(_079_),
    .B(_020_),
    .Y(_021_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../../Cells/all2nand.v:3.7-3.31" *)
  NAND _201_ (
    .A(_021_),
    .B(_021_),
    .Y(_022_)
  );
  NAND _202_ (
    .A(_090_),
    .B(_022_),
    .Y(_023_)
  );
  NAND _203_ (
    .A(_084_),
    .B(_023_),
    .Y(SUM[6])
  );
  NAND _204_ (
    .A(_081_),
    .B(_082_),
    .Y(_024_)
  );
  NAND _205_ (
    .A(_088_),
    .B(_024_),
    .Y(SUM[7])
  );
  assign \cla1.CIN  = 1'h0;
  assign \cla1.B  = B[3:0];
  assign \cla1.A  = A[3:0];
  assign \cla1.fa3.a  = A[3];
  assign \cla1.fa3.b  = B[3];
  assign \cla1.fa2.a  = A[2];
  assign \cla1.fa2.b  = B[2];
  assign \cla1.fa1.a  = A[1];
  assign \cla1.fa1.b  = B[1];
  assign \cla1.fa0.a  = A[0];
  assign \cla1.fa0.b  = B[0];
  assign \cla1.fa0.cin  = 1'h0;
  assign \cla2.B  = B[7:4];
  assign \cla2.A  = A[7:4];
  assign \cla2.fa3.a  = A[7];
  assign \cla2.fa3.b  = B[7];
  assign \cla2.fa2.a  = A[6];
  assign \cla2.fa2.b  = B[6];
  assign \cla2.fa1.a  = A[5];
  assign \cla2.fa1.b  = B[5];
  assign \cla2.fa0.a  = A[4];
  assign \cla2.fa0.b  = B[4];
  assign { sat_sum[7], sat_sum[5:0] } = { A[7], sat_sum[6], sat_sum[6], sat_sum[6], sat_sum[6], sat_sum[6], sat_sum[6] };
endmodule
