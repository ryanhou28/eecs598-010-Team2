module shift_reg_mem_comb(
    input singed [7:0] write_data [31:0],
    input signed [7:0] shift_reg [31:0],
    input write_enable,
    output signed [7:0] shift_reg_next
);

    always_comb begin
        // Shift the data down
        for (int i = 1; i < 32; i = i + 1) begin
            shift_reg_next[i] = shift_reg[i - 1];
        end

        // On write
        if (write_enable) begin
            for (int i = 0; i < 32; i = i + 1) begin
                shift_reg_next[i] = write_data[i];
            end
        end else begin
            shift_reg_next[0] = 0;
        end
    end

endmodule