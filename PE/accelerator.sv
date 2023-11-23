
// Define the top-level accelerator module
module accelerator(
    input signed [7:0] input_fmap, // Input feature map
    input signed [7:0] input_weights [31:0], // Input weight
    input enable,
    input reset,
    input clk,
    output signed [7:0] output_fmap [31:0] // Output feature map
);

    // Instantiate the processing element array
    pe_array pe_array1(
        .input_fmap(input_fmap),
        .input_weights(input_weights),
        .input_valid(enable),
        .done(reset),
        .clk(clk),
        .output_fmap(output_fmap)
    );

endmodule

module pe_array(
    input signed [7:0] input_fmap, // Input feature map
    input signed [7:0] input_weights [31:0], // Input weight
    input input_valid,
    input done,
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
                .input_valid(input_valid),
                .done(done),
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
    input done,
    input clk,
    output signed [7:0] output_f // Output feature
);

    // Define the partial sum register
    logic signed [7:0] partial_sum_reg;
    logic signed [7:0] partial_sum_next;

    // On the rising edge of the clock, update the partial sum register
    always @(posedge clk) begin
        if (done) begin
            // Reset the partial sum register
            partial_sum_reg <= 8'sh00;
        end else begin
            partial_sum_reg <= partial_sum_next;
        end
    end

    logic signed [7:0] relu_out;

    // Instantiate the ReLU activation function
    relu relu1(.input_f(partial_sum_reg), .output_f(relu_out));

    // Connect the output feature to the ReLU of the partial sum register
    assign output_f = relu_out;

    // Define the output of the multiplier
    logic signed [7:0] mult_out;

    // Instantiate the multiplier
    mult mult1(.a(input_f), .b(input_w), .product(mult_out));

    // Define the output of the adder
    logic signed [7:0] adder_out;

    // Instantiate the adder
    adder8 adder1(.A(mult_out), .B(partial_sum_reg), .SUM(adder_out));
    
    // Define the next partial sum based on the input conditions
    assign partial_sum_next = (input_valid & ~done) ? adder_out : 8'sh00;


endmodule

// Define ReLU activation function
module relu(
    input signed [7:0] input_f,   // Input feature
    output signed [7:0] output_f // Output feature
);

    // If the input feature is negative, set the output feature to 0
    assign output_f = (input_f < 8'sh00) ? 8'sh00 : input_f;

endmodule


// Signed multiplication two 8-bit integers in 2's complement form
module mult(
    input  signed [7:0] a,  // First 8-bit signed input
    input  signed [7:0] b,  // Second 8-bit signed input
    output logic signed [7:0] product  // 8-bit signed output for the product
);

    // Intermediate full-width product
    logic signed [15:0] full_product;

    // Perform multiplication
    assign full_product = a * b;

    // Saturating logic
    always_comb begin
        if (full_product > 16'sh007F) begin
            product = 8'sh7F; // Saturate to max positive value
        end else if (full_product < 16'shFF80) begin
            product = 8'sh80; // Saturate to max negative value
        end else begin
            product = full_product[7:0]; // Truncate to lower 8 bits
        end
    end

endmodule


module adder8(A, B, SUM);
    input [7:0] A;
    input [7:0] B;
    output [7:0] SUM;

    // A saturating signed 8-bit integer Carry Look Ahead Adder
    wire [1:0] C;
    wire [7:0] int_sum;
    wire overflow;
    wire [7:0] sat_sum;
    cla4 cla1(.A(A[3:0]), .B(B[3:0]), .CIN(1'b0), .SUM(int_sum[3:0]), .COUT(C[0]));
    cla4 cla2(.A(A[7:4]), .B(B[7:4]), .CIN(C[0]), .SUM(int_sum[7:4]), .COUT(C[1]));

    // Overflow detection
    assign overflow = (A[7] == B[7]) & (A[7] != int_sum[7]);
    // assign sat_sum = (A[7]) ? 8'b01111111 : 8'b10000000;
    assign sat_sum = (A[7]) ? 8'b10000000 : 8'b01111111;
    assign SUM = (overflow) ? sat_sum : int_sum;

endmodule


module cla4(A, B, CIN, SUM, COUT);
    input [3:0] A;
    input [3:0] B;
    input CIN;
    output [3:0] SUM;
    output COUT;
    
    wire [3:0] G, P;
    wire [2:0] C;

    full_adder fa0(.a(A[0]), .b(B[0]), .cin(CIN), .sum(SUM[0]), .cout(C[0]));
    full_adder fa1(.a(A[1]), .b(B[1]), .cin(C[0]), .sum(SUM[1]), .cout(C[1]));
    full_adder fa2(.a(A[2]), .b(B[2]), .cin(C[1]), .sum(SUM[2]), .cout(C[2]));
    full_adder fa3(.a(A[3]), .b(B[3]), .cin(C[2]), .sum(SUM[3]), .cout());

    assign G[0] = A[0] & B[0];
    assign P[0] = A[0] | B[0];
    assign G[1] = A[1] & B[1];
    assign P[1] = A[1] | B[1];
    assign G[2] = A[2] & B[2];
    assign P[2] = A[2] | B[2];
    assign G[3] = A[3] & B[3];
    assign P[3] = A[3] | B[3];


    wire G_f;
    assign G_f = G[3] | (P[3] & (G[2] | (P[2] & (G[1] | (P[1] & G[0])))));

    assign COUT = G_f | ((P[0] & P[1] & P[2] & P[3]) & CIN);

endmodule



module full_adder(a,b,cin,sum,cout);
    input a,b,cin;
    output sum,cout;

    wire axorb;
    assign axorb = a ^ b;
    assign sum = axorb ^ cin;
    assign cout = (a & b) | (axorb & cin);

endmodule