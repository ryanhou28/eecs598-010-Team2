// Define ReLU activation function
module relu(
    input signed [7:0] input_f,
    output signed [7:0] output_f
);
    // If the input feature is negative, set the output feature to 0
    assign output_f = (input_f < 8'sh00) ? 8'sh00 : input_f;
endmodule