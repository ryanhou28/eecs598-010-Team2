module tb();

reg [0:49] in_ram [0:9];
reg [0:49] inz;
wire [0:21] outz;
reg clk=0;
c3540_clk dup(clk,
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
inz[36],
inz[37],
inz[38],
inz[39],
inz[40],
inz[41],
inz[42],
inz[43],
inz[44],
inz[45],
inz[46],
inz[47],
inz[48],
inz[49],
outz[0],
outz[1],
outz[2],
outz[3],
outz[4],
outz[5],
outz[6],
outz[7],
outz[8],
outz[9],
outz[10],
outz[11],
outz[12],
outz[13],
outz[14],
outz[15],
outz[16],
outz[17],
outz[18],
outz[19],
outz[20],
outz[21]
);

initial begin 
  $readmemb("l3540.txt", in_ram);
  for (integer i = 0; i < 10; i=i+1) begin
  inz <= in_ram[i];
  #10 clk<=~clk;
  #10 clk<=~clk;
  $displayb(outz);
  end
end

endmodule
