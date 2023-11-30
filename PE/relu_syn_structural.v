



module relu(input_f, output_f);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  wire _06_;
  wire _07_;
  
  input [7:0] input_f;
  wire [7:0] input_f;
  
  output [7:0] output_f;
  wire [7:0] output_f;
  
  
  nand (_00_, input_f[7], input_f[7]);
  nand (_01_, _00_, input_f[0]);
  
  
  nand (output_f[0], _01_, _01_);
  nand (_02_, _00_, input_f[1]);
  
  
  nand (output_f[1], _02_, _02_);
  nand (_03_, _00_, input_f[2]);
  
  
  nand (output_f[2], _03_, _03_);
  nand (_04_, _00_, input_f[3]);
  
  
  nand (output_f[3], _04_, _04_);
  nand (_05_, input_f[4], _00_);
  
  
  nand (output_f[4], _05_, _05_);
  nand (_06_, input_f[5], _00_);
  
  
  nand (output_f[5], _06_, _06_);
  nand (_07_, input_f[6], _00_);
  
  
  nand (output_f[6], _07_, _07_);
  assign output_f[7] = 1'h0;
endmodule
