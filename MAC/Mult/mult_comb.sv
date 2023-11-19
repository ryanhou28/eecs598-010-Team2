// Signed multiplication two 8-bit integers in 2's complement form
module mult(
    input  signed [7:0] a,  // First 8-bit signed input
    input  signed [7:0] b,  // Second 8-bit signed input
    output signed [7:0] product  // 8-bit signed output for the product
);

    // Intermediate full-width product
    logic signed [15:0] full_product;

    // Perform multiplication
    assign full_product = a * b;

    // Saturating logic
    always @(*) begin
        if (full_product > 16'sh007F) begin
            product = 8'sh7F; // Saturate to max positive value
        end else if (full_product < 16'shFF80) begin
            product = 8'sh80; // Saturate to max negative value
        end else begin
            product = full_product[7:0]; // Truncate to lower 8 bits
        end
    end

endmodule