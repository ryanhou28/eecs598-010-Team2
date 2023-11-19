`define XLEN 8
`define MULT_DEFAULT_N_STAGES 4
`define SD #1

module mult_stage #(parameter NUM_STAGES = `MULT_DEFAULT_N_STAGES) (
	input                 clock, reset, start,
	input [2*`XLEN-1:0] mplier_in, mcand_in,
	input [2*`XLEN-1:0] product_in,

	output logic                 done,
	output logic [2*`XLEN-1:0] mplier_out, mcand_out,
	output logic [2*`XLEN-1:0] product_out
);

	parameter NUM_BITS = (2*`XLEN)/NUM_STAGES;

	logic [2*`XLEN-1:0] prod_in_reg, partial_prod, next_partial_product;
	logic [2*`XLEN-1:0] next_mplier, next_mcand;

	assign product_out = prod_in_reg + partial_prod;

	assign next_partial_product = mplier_in[NUM_BITS-1:0] * mcand_in;

	assign next_mplier = {NUM_BITS'('b0), mplier_in[2*`XLEN-1:NUM_BITS]};
	assign next_mcand  = {mcand_in[(2*`XLEN-1-NUM_BITS):0], NUM_BITS'('b0)};

	//synopsys sync_set_reset "reset"
	always_ff @(posedge clock) begin
		prod_in_reg  <= `SD product_in;
		partial_prod <= `SD next_partial_product;
		mplier_out   <= `SD next_mplier;
		mcand_out    <= `SD next_mcand;
	end

	// synopsys sync_set_reset "reset"
	always_ff @(posedge clock) begin
		if(reset) begin
			done <= `SD 1'b0;
		end else begin
			done <= `SD start;
		end
	end

endmodule // module mult_stage