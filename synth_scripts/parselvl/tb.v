module tb();

reg [0:7] in_ram [0:4];
reg [0:7] inz;
wire [0:4] outz;
reg clk=0;
rrr xxx(clk, inz[0], inz[1], inz[2], inz[3], inz[4], inz[5], inz[6], inz[7], outz[0], outz[1], outz[2], outz[3], outz[4]);

initial begin 
  $readmemb("lol.txt", in_ram);
  for (integer i = 0; i < 5; i=i+1) begin
  inz <= in_ram[i];
  #10 clk<=~clk;
  #10 clk<=~clk;
  $displayb(outz);
  end
end

endmodule
