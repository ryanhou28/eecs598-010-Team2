module testbench;

    // Clock
    logic clock;

    // 4-bit Adder Test
    logic signed [7:0] a;
    logic signed [7:0] b;
    logic signed [7:0] sum;
    adder8 adder_(.A(a), .B(b), .SUM(sum));

    logic adder_correct;
    logic signed [7:0] correct_sum;
    assign correct_sum = a + b;
    assign adder_correct = (sum == correct_sum);

    // 4-bit Carry Lookahead Adder Test
    logic [3:0] cla_a;
    logic [3:0] cla_b;
    logic cla_cin;
    logic [3:0] cla_sum;
    logic cla_cout;
    cla4 cla_(.A(cla_a), .B(cla_b), .CIN(cla_cin), .SUM(cla_sum), .COUT(cla_cout));

    // Full Adder Test
    logic fa_a;
    logic fa_b;
    logic fa_cin;
    logic fa_sum;
    logic fa_cout;
    full_adder fa_(.a(fa_a), .b(fa_b), .cin(fa_cin), .sum(fa_sum), .cout(fa_cout));


    always begin
        #5;
        clock=~clock;
    end

    always@(adder_correct)
    begin
        #2
        if(!adder_correct)
        begin
            $display("@@@ Incorrect at time %4.0f", $time);
            $display("@@@ Time:%4.0f clock:%b A:%d B:%d SUM:%d", 
                $time, clock, a, b, sum);
            $display("@@@ expected sum=%d", a + b);
        end
    end

    initial begin

        $monitor("Time:%4.0f clock:%b | A:%d B:%d SUM:%d = %b | A:%d B:%d CIN:%d SUM:%d COUT:%d | A:%b B:%b CIN:%b SUM:%b COUT:%b",
                $time, clock, a, b, sum, sum, cla_a, cla_b, cla_cin, cla_sum, cla_cout, fa_a, fa_b, fa_cin, fa_sum, fa_cout);

        clock = 1'b0;
        a = 2;
        b = 3;

        cla_a = 2;
        cla_b = 3;
        cla_cin = 1'b0;

        fa_a = 1'b0;
        fa_b = 1'b0;
        fa_cin = 1'b0;
        @(negedge clock);
        @(negedge clock);
        fa_a = 1'b1;
        @(negedge clock);
        fa_b = 1'b1;
        @(negedge clock);
        fa_cin = 1'b1;
        @(negedge clock);
        fa_a = 1'b0;
        @(negedge clock);
        fa_b = 1'b0;
        @(negedge clock);
        a = 4;
        b = -5;
        @(negedge clock);
        a = -128;
        b = 127;
        @(negedge clock);
        a = 127;
        b = -2;
        @(negedge clock);
        a = -2;
        b = -100;
        @(negedge clock);
        a = 50;
        b = 60;
        @(negedge clock);
        a = -30;
        b = -20;
        @(negedge clock);
        a = 40;
        b = -20;
        @(negedge clock);
        a = 0;
        b = 44;
        @(negedge clock);
        a = -40;
        b = 0;
        @(negedge clock);
        a = -1;
        b = 1;
        @(negedge clock);
        // OVERFLOW CHECKS: Ignore the error printouts since they don't account for overflows
        $display("@@@ Overflow checks. Ignore error printouts.");
        @(negedge clock);
        a = 100;
        b = 50;
        @(negedge clock);
        a = -70;
        b = -90;
        @(negedge clock);
        a = 127;
        b = 127;
        @(negedge clock);
        a = -128;
        b = -128;
        @(negedge clock);
        a = 114;
        b = 60;
        @(negedge clock);


        $finish;
        

    end

endmodule