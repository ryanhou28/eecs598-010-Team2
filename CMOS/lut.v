// Control interface with memory for LUT
`timescale 1ns/1ps

module mux_tree #(
    parameter integer DATA_WIDTH = 4,
    parameter integer CONTROL_WIDTH = 4
) (
    input clock,
    input  logic unsigned [CONTROL_WIDTH-1:0] S,
    input  logic unsigned [DATA_WIDTH-1:0] data_in,
    output logic unsigned [ADRESS_WIDTH-1:0] addr,
    output logic unsigned [DATA_WIDTH-1:0] out
);

always_ff (@posedge clock) begin
    out <= data_in;
end



  

endmodule
