`include "pe_comb.sv"

// Define the top-level accelerator module
module accelerator(
    input signed [7:0] input_fmap, // Input feature map
    input signed [7:0] input_weights [31:0], // Input weight
    input enable,
    input reset,
    input clk,
    output signed [7:0] output_fmap [31:0] // Output feature map
);

    // Instantiate the array of processing elements
    genvar i;
    generate
        for (i = 0; i < 32; i = i + 1) begin
            processing_element pe1(
                .input_f(input_fmap),
                .input_w(input_weights[i]),
                .input_valid(enable),
                .reset(reset),
                .clk(clk),
                .output_f(output_fmap[i])
            );
        end
    endgenerate

endmodule

// Define a processing element
module processing_element(
    input signed [7:0] input_f,   // Input feature
    input signed [7:0] input_w,   // Input weight
    input input_valid,
    input reset,
    input clk,
    output signed [7:0] output_f // Output feature
);

    // Define variables
    logic signed [7:0] partial_sum_reg;
    logic signed [7:0] partial_sum_next;

    // On the rising edge of the clock, update the partial sum register
    always @(posedge clk) begin
        partial_sum_reg <= partial_sum_next;
    end

    // Instantiate the combinational part of the processing element
    pe_comb pe_comb1(
        .input_f(input_f),
        .input_w(input_w),
        .psum_reg(partial_sum_reg),
        .enable(input_valid),
        .reset(reset),
        .psum_next(partial_sum_next),
        .output_f(output_f)
    );

endmodule