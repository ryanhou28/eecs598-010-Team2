
module mymod
(
  input_f[0],
  input_f[1],
  input_f[2],
  input_f[3],
  input_f[4],
  input_f[5],
  input_f[6],
  input_f[7],
  output_f[0],
  output_f[1],
  output_f[2],
  output_f[3],
  output_f[4],
  output_f[5],
  output_f[6],
  output_f[7]
);

  input input_f[0];input input_f[1];input input_f[2];input input_f[3];input input_f[4];input input_f[5];input input_f[6];input input_f[7];
  output output_f[0];output output_f[1];output output_f[2];output output_f[3];output output_f[4];output output_f[5];output output_f[6];output output_f[7];
  wire input_f[0]_p;
  wire input_f[0]_n;
  wire input_f[1]_p;
  wire input_f[1]_n;
  wire input_f[2]_p;
  wire input_f[2]_n;
  wire input_f[3]_p;
  wire input_f[3]_n;
  wire input_f[4]_p;
  wire input_f[4]_n;
  wire input_f[5]_p;
  wire input_f[5]_n;
  wire input_f[6]_p;
  wire input_f[6]_n;
  wire input_f[7]_p;
  wire input_f[7]_n;
  wire g9_p;
  wire g9_n;
  wire g10_p;
  wire g10_n;
  wire g11_p;
  wire g11_n;
  wire g12_p;
  wire g12_n;
  wire g13_p;
  wire g13_n;
  wire g14_p;
  wire g14_n;
  wire g15_p;
  wire g15_n;
  wire input_f[7]_p_spl_;
  wire input_f[7]_p_spl_0;
  wire input_f[7]_p_spl_00;
  wire input_f[7]_p_spl_01;
  wire input_f[7]_p_spl_1;
  wire input_f[7]_p_spl_10;

  buf

  (
    input_f[0]_p,
    input_f[0]
  );


  not

  (
    input_f[0]_n,
    input_f[0]
  );


  buf

  (
    input_f[1]_p,
    input_f[1]
  );


  not

  (
    input_f[1]_n,
    input_f[1]
  );


  buf

  (
    input_f[2]_p,
    input_f[2]
  );


  not

  (
    input_f[2]_n,
    input_f[2]
  );


  buf

  (
    input_f[3]_p,
    input_f[3]
  );


  not

  (
    input_f[3]_n,
    input_f[3]
  );


  buf

  (
    input_f[4]_p,
    input_f[4]
  );


  not

  (
    input_f[4]_n,
    input_f[4]
  );


  buf

  (
    input_f[5]_p,
    input_f[5]
  );


  not

  (
    input_f[5]_n,
    input_f[5]
  );


  buf

  (
    input_f[6]_p,
    input_f[6]
  );


  not

  (
    input_f[6]_n,
    input_f[6]
  );


  buf

  (
    input_f[7]_p,
    input_f[7]
  );


  not

  (
    input_f[7]_n,
    input_f[7]
  );


  or

  (
    g9_n,
    input_f[0]_n,
    input_f[7]_p_spl_00
  );


  or

  (
    g10_n,
    input_f[1]_n,
    input_f[7]_p_spl_00
  );


  or

  (
    g11_n,
    input_f[2]_n,
    input_f[7]_p_spl_01
  );


  or

  (
    g12_n,
    input_f[3]_n,
    input_f[7]_p_spl_01
  );


  or

  (
    g13_n,
    input_f[4]_n,
    input_f[7]_p_spl_10
  );


  or

  (
    g14_n,
    input_f[5]_n,
    input_f[7]_p_spl_10
  );


  or

  (
    g15_n,
    input_f[6]_n,
    input_f[7]_p_spl_1
  );


  not

  (
    output_f[0],
    g9_n
  );


  not

  (
    output_f[1],
    g10_n
  );


  not

  (
    output_f[2],
    g11_n
  );


  not

  (
    output_f[3],
    g12_n
  );


  not

  (
    output_f[4],
    g13_n
  );


  not

  (
    output_f[5],
    g14_n
  );


  not

  (
    output_f[6],
    g15_n
  );


  not

  (
    output_f[7],
    1'b1
  );


  buf

  (
    input_f[7]_p_spl_,
    input_f[7]_p
  );


  buf

  (
    input_f[7]_p_spl_0,
    input_f[7]_p_spl_
  );


  buf

  (
    input_f[7]_p_spl_00,
    input_f[7]_p_spl_0
  );


  buf

  (
    input_f[7]_p_spl_01,
    input_f[7]_p_spl_0
  );


  buf

  (
    input_f[7]_p_spl_1,
    input_f[7]_p_spl_
  );


  buf

  (
    input_f[7]_p_spl_10,
    input_f[7]_p_spl_1
  );


endmodule
