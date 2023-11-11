module tb();

reg [0:35] in_ram [0:9];
reg [0:35] inz;
wire [0:6] outz;
reg clk=0;
c432_pipe dup(clk,
inz[0],
inz[1],
inz[2],
inz[3],
inz[4],
inz[5],
inz[6],
inz[7],
inz[8],
inz[9],
inz[10],
inz[11],
inz[12],
inz[13],
inz[14],
inz[15],
inz[16],
inz[17],
inz[18],
inz[19],
inz[20],
inz[21],
inz[22],
inz[23],
inz[24],
inz[25],
inz[26],
inz[27],
inz[28],
inz[29],
inz[30],
inz[31],
inz[32],
inz[33],
inz[34],
inz[35],
outz[0],
outz[1],
outz[2],
outz[3],
outz[4],
outz[5],
outz[6]);

initial begin 
  $readmemb("lll.txt", in_ram);
  for (integer i = 0; i < 10; i=i+1) begin
  inz <= in_ram[i];
  #10 clk<=~clk;
  #10 clk<=~clk;
  $displayb(outz);
  end
end

endmodule
