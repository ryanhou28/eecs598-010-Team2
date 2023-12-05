module shift_reg_mem(
    input signed [7:0] write_data [31:0],
    input write_enable,
    input clk,
    input reset,
    output signed [7:0] read_data,
    output [4:0] addr
);
    // A shift register of 32 8-bit values
    logic signed [7:0] shift_reg [31:0];
    logic signed [7:0] shift_reg_next [31:0];
    logic [4:0] addr_reg;

    // Write to the shift register
    always_comb begin
        // Shift the data down
        for (int i = 1; i < 32; i = i + 1) begin
            shift_reg_next[i] = shift_reg[i - 1];
        end
        if (write_enable) begin
            // If input is valid, write to the first register
            // shift_reg_next = write_data;

            // Reverse the order of the data
            for (int i = 0; i < 32; i = i + 1) begin
                shift_reg_next[i] = write_data[31 - i];
            end
        end else begin
            // Otherwise put a 0 in the first register
            shift_reg_next[0] = 0;
        end
        
        if (reset) begin
            for (int i = 0; i < 32; i = i + 1) begin
                shift_reg_next[i] = 0;
            end
        end
    end

    // Read from the shift register
    assign read_data = shift_reg[31];
    assign addr = addr_reg;

    // Update the address
    always_ff @(posedge clk) begin
        if (reset || write_enable) begin
            // If reset or write is enabled, reset the address since we're outputting from the start
            addr_reg <= 0;
        end else begin
            addr_reg <= addr_reg + 1;
        end

        shift_reg <= shift_reg_next;
    end


endmodule