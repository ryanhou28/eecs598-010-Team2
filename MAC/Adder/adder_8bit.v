module adder8(
    input [7:0] A,
    input [7:0] B,
    output [7:0] SUM
);

always @(*) begin
    // Perform the addition
    SUM = A + B;

    // Check for overflow
    if (A > 127 && B > 127) begin
        if (SUM < 128) begin
            SUM = 127; // Saturate to the maximum value
        end
    end else if (A < -128 && B < -128) begin
        if (SUM > -129) begin
            SUM = -128; // Saturate to the minimum value
        end
    end
end


endmodule