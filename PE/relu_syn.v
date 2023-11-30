/* Generated by Yosys 0.25+99 (git sha1 54bf15a5b, x86_64-apple-darwin20.2-clang 10.0.0-4ubuntu1 -fPIC -Os) */

(* top =  1  *)
(* src = "relu.sv:1.1-6.10" *)
module relu(input_f, output_f);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  wire _06_;
  wire _07_;
  (* src = "relu.sv:2.24-2.31" *)
  input [7:0] input_f;
  wire [7:0] input_f;
  (* src = "relu.sv:3.25-3.33" *)
  output [7:0] output_f;
  wire [7:0] output_f;
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _08_ (
    .A(input_f[7]),
    .B(input_f[7]),
    .Y(_00_)
  );
  NAND _09_ (
    .A(_00_),
    .B(input_f[0]),
    .Y(_01_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _10_ (
    .A(_01_),
    .B(_01_),
    .Y(output_f[0])
  );
  NAND _11_ (
    .A(_00_),
    .B(input_f[1]),
    .Y(_02_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _12_ (
    .A(_02_),
    .B(_02_),
    .Y(output_f[1])
  );
  NAND _13_ (
    .A(_00_),
    .B(input_f[2]),
    .Y(_03_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _14_ (
    .A(_03_),
    .B(_03_),
    .Y(output_f[2])
  );
  NAND _15_ (
    .A(_00_),
    .B(input_f[3]),
    .Y(_04_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _16_ (
    .A(_04_),
    .B(_04_),
    .Y(output_f[3])
  );
  NAND _17_ (
    .A(input_f[4]),
    .B(_00_),
    .Y(_05_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _18_ (
    .A(_05_),
    .B(_05_),
    .Y(output_f[4])
  );
  NAND _19_ (
    .A(input_f[5]),
    .B(_00_),
    .Y(_06_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _20_ (
    .A(_06_),
    .B(_06_),
    .Y(output_f[5])
  );
  NAND _21_ (
    .A(input_f[6]),
    .B(_00_),
    .Y(_07_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "../Cells/all2nand.v:3.7-3.31" *)
  NAND _22_ (
    .A(_07_),
    .B(_07_),
    .Y(output_f[6])
  );
  assign output_f[7] = 1'h0;
endmodule