// Benchmark "mymod" written by ABC on Thu Nov  2 00:21:40 2023

module mymod (  
    X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3,
    S_0, S_1, S_2, S_3, Co  );
  
  input  X_0, Y_0, X_1, Y_1, X_2, Y_2, X_3, Y_3;
  output S_0, S_1, S_2, S_3, Co;
  reg \rippe_adder|xw1 , \rippe_adder|xw2 , \rippe_adder|xw3 ;
  wire new_new_n20__, new_new_n21__, new_new_n22__, new_new_n23__,
    new_new_n24__, new_new_n25__, new_new_n26__, new_new_n27__,
    new_new_n28__, new_new_n29__, new_new_n30__, new_new_n31__,
    new_new_n32__, new_new_n33__, new_new_n34__, new_new_n35__,
    new_new_n36__, new_new_n37__, new_new_n38__, new_new_n39__,
    new_new_n40__, new_new_n41__, new_new_n42__, new_new_n43__,
    new_new_n44__, new_new_n45__, new_new_n46__, new_new_n47__,
    new_new_n48__, new_new_n49__, new_new_n50__, new_new_n51__,
    new_new_n52__, new_new_n53__, new_new_n54__, new_new_n55__,
    new_new_n56__, new_new_n57__, new_new_n58__, new_new_n59__,
    new_new_n60__, new_new_n61__, new_new_n62__, new_new_n63__,
    new_new_n64__, new_new_n65__, new_new_n66__, new_new_n67__,
    new_new_n68__, new_new_n69__, new_new_n70__, new_new_n71__,
    new_new_n72__, new_new_n73__, new_new_n74__, new_new_n83__,
    new_new_n84__, new_new_n85__, new_new_n86__, new_new_n87__,
    new_new_n88__, new_new_n89__, new_new_n90__, new_new_n91__,
    new_new_n92__, new_new_n93__, new_new_n94__, new_new_n95__,
    new_new_n96__, new_new_n97__, new_new_n98__, new_new_n99__,
    new_new_n100__, new_new_n101__, n189, n192, n195;
  buf1  g00(.din(X_0), .dout(new_new_n20__));
  not1  g01(.din(X_0), .dout(new_new_n21__));
  buf1  g02(.din(Y_0), .dout(new_new_n22__));
  not1  g03(.din(Y_0), .dout(new_new_n23__));
  buf1  g04(.din(X_1), .dout(new_new_n24__));
  not1  g05(.din(X_1), .dout(new_new_n25__));
  buf1  g06(.din(Y_1), .dout(new_new_n26__));
  not1  g07(.din(Y_1), .dout(new_new_n27__));
  buf1  g08(.din(X_2), .dout(new_new_n28__));
  not1  g09(.din(X_2), .dout(new_new_n29__));
  buf1  g10(.din(Y_2), .dout(new_new_n30__));
  not1  g11(.din(Y_2), .dout(new_new_n31__));
  buf1  g12(.din(X_3), .dout(new_new_n32__));
  not1  g13(.din(X_3), .dout(new_new_n33__));
  buf1  g14(.din(Y_3), .dout(new_new_n34__));
  not1  g15(.din(Y_3), .dout(new_new_n35__));
  buf1  g16(.din(\rippe_adder|xw1 ), .dout(new_new_n36__));
  not1  g17(.din(\rippe_adder|xw1 ), .dout(new_new_n37__));
  buf1  g18(.din(\rippe_adder|xw2 ), .dout(new_new_n38__));
  not1  g19(.din(\rippe_adder|xw2 ), .dout(new_new_n39__));
  buf1  g20(.din(\rippe_adder|xw3 ), .dout(new_new_n40__));
  not1  g21(.din(\rippe_adder|xw3 ), .dout(new_new_n41__));
  or1   g22(.dina(new_new_n21__), .dinb(new_new_n23__), .dout(new_new_n42__));
  or1   g23(.dina(new_new_n20__), .dinb(new_new_n22__), .dout(new_new_n43__));
  and1  g24(.dina(new_new_n83__), .dinb(new_new_n43__), .dout(new_new_n44__));
  and1  g25(.dina(new_new_n84__), .dinb(new_new_n85__), .dout(new_new_n45__));
  or1   g26(.dina(new_new_n86__), .dinb(new_new_n87__), .dout(new_new_n46__));
  and1  g27(.dina(new_new_n86__), .dinb(new_new_n87__), .dout(new_new_n47__));
  or1   g28(.dina(new_new_n84__), .dinb(new_new_n85__), .dout(new_new_n48__));
  and1  g29(.dina(new_new_n88__), .dinb(new_new_n48__), .dout(new_new_n49__));
  or1   g30(.dina(new_new_n45__), .dinb(new_new_n47__), .dout(new_new_n50__));
  or1   g31(.dina(new_new_n37__), .dinb(new_new_n50__), .dout(new_new_n51__));
  or1   g32(.dina(new_new_n36__), .dinb(new_new_n49__), .dout(new_new_n52__));
  and1  g33(.dina(new_new_n89__), .dinb(new_new_n52__), .dout(new_new_n53__));
  and1  g34(.dina(new_new_n90__), .dinb(new_new_n91__), .dout(new_new_n54__));
  or1   g35(.dina(new_new_n92__), .dinb(new_new_n93__), .dout(new_new_n55__));
  and1  g36(.dina(new_new_n92__), .dinb(new_new_n93__), .dout(new_new_n56__));
  or1   g37(.dina(new_new_n90__), .dinb(new_new_n91__), .dout(new_new_n57__));
  and1  g38(.dina(new_new_n94__), .dinb(new_new_n57__), .dout(new_new_n58__));
  or1   g39(.dina(new_new_n54__), .dinb(new_new_n56__), .dout(new_new_n59__));
  or1   g40(.dina(new_new_n39__), .dinb(new_new_n59__), .dout(new_new_n60__));
  or1   g41(.dina(new_new_n38__), .dinb(new_new_n58__), .dout(new_new_n61__));
  and1  g42(.dina(new_new_n95__), .dinb(new_new_n61__), .dout(new_new_n62__));
  and1  g43(.dina(new_new_n96__), .dinb(new_new_n97__), .dout(new_new_n63__));
  or1   g44(.dina(new_new_n98__), .dinb(new_new_n99__), .dout(new_new_n64__));
  and1  g45(.dina(new_new_n98__), .dinb(new_new_n99__), .dout(new_new_n65__));
  or1   g46(.dina(new_new_n96__), .dinb(new_new_n97__), .dout(new_new_n66__));
  and1  g47(.dina(new_new_n100__), .dinb(new_new_n66__), .dout(new_new_n67__));
  or1   g48(.dina(new_new_n63__), .dinb(new_new_n65__), .dout(new_new_n68__));
  or1   g49(.dina(new_new_n41__), .dinb(new_new_n68__), .dout(new_new_n69__));
  or1   g50(.dina(new_new_n40__), .dinb(new_new_n67__), .dout(new_new_n70__));
  and1  g51(.dina(new_new_n101__), .dinb(new_new_n70__), .dout(new_new_n71__));
  and1  g52(.dina(new_new_n100__), .dinb(new_new_n101__), .dout(new_new_n72__));
  and1  g53(.dina(new_new_n88__), .dinb(new_new_n89__), .dout(new_new_n73__));
  and1  g54(.dina(new_new_n94__), .dinb(new_new_n95__), .dout(new_new_n74__));
  buf1  g55(.din(new_new_n44__), .dout(S_0));
  buf1  g56(.din(new_new_n53__), .dout(S_1));
  buf1  g57(.din(new_new_n62__), .dout(S_2));
  buf1  g58(.din(new_new_n71__), .dout(S_3));
  not1  g59(.din(new_new_n72__), .dout(Co));
  not1  g60(.din(new_new_n83__), .dout(n189));
  not1  g61(.din(new_new_n73__), .dout(n192));
  not1  g62(.din(new_new_n74__), .dout(n195));
  buf1  g63(.din(new_new_n42__), .dout(new_new_n83__));
  buf1  g64(.din(new_new_n24__), .dout(new_new_n84__));
  buf1  g65(.din(new_new_n26__), .dout(new_new_n85__));
  buf1  g66(.din(new_new_n25__), .dout(new_new_n86__));
  buf1  g67(.din(new_new_n27__), .dout(new_new_n87__));
  buf1  g68(.din(new_new_n46__), .dout(new_new_n88__));
  buf1  g69(.din(new_new_n51__), .dout(new_new_n89__));
  buf1  g70(.din(new_new_n28__), .dout(new_new_n90__));
  buf1  g71(.din(new_new_n30__), .dout(new_new_n91__));
  buf1  g72(.din(new_new_n29__), .dout(new_new_n92__));
  buf1  g73(.din(new_new_n31__), .dout(new_new_n93__));
  buf1  g74(.din(new_new_n55__), .dout(new_new_n94__));
  buf1  g75(.din(new_new_n60__), .dout(new_new_n95__));
  buf1  g76(.din(new_new_n32__), .dout(new_new_n96__));
  buf1  g77(.din(new_new_n34__), .dout(new_new_n97__));
  buf1  g78(.din(new_new_n33__), .dout(new_new_n98__));
  buf1  g79(.din(new_new_n35__), .dout(new_new_n99__));
  buf1  g80(.din(new_new_n64__), .dout(new_new_n100__));
  buf1  g81(.din(new_new_n69__), .dout(new_new_n101__));
  always @ (posedge clock) begin
    \rippe_adder|xw1  <= n189;
    \rippe_adder|xw2  <= n192;
    \rippe_adder|xw3  <= n195;
  end
  initial begin
    \rippe_adder|xw1  <= 1'b0;
    \rippe_adder|xw2  <= 1'b0;
    \rippe_adder|xw3  <= 1'b0;
  end
endmodule


