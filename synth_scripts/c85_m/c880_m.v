// Benchmark "c880" written by ABC on Sun Oct 29 22:18:03 2023

module c880 ( 
    G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16,
    G17, G18, G19, G20, G21, G22, G23, G24, G25, G26, G27, G28, G29, G30,
    G31, G32, G33, G34, G35, G36, G37, G38, G39, G40, G41, G42, G43, G44,
    G45, G46, G47, G48, G49, G50, G51, G52, G53, G54, G55, G56, G57, G58,
    G59, G60,
    G855, G856, G857, G858, G859, G860, G861, G862, G863, G864, G865, G866,
    G867, G868, G869, G870, G871, G872, G873, G874, G875, G876, G877, G878,
    G879, G880  );
  input  G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14,
    G15, G16, G17, G18, G19, G20, G21, G22, G23, G24, G25, G26, G27, G28,
    G29, G30, G31, G32, G33, G34, G35, G36, G37, G38, G39, G40, G41, G42,
    G43, G44, G45, G46, G47, G48, G49, G50, G51, G52, G53, G54, G55, G56,
    G57, G58, G59, G60;
  output G855, G856, G857, G858, G859, G860, G861, G862, G863, G864, G865,
    G866, G867, G868, G869, G870, G871, G872, G873, G874, G875, G876, G877,
    G878, G879, G880;
  wire new_n87_, new_n89_, new_n93_, new_n94_, new_n96_, new_n97_, new_n98_,
    new_n100_, new_n102_, new_n105_, new_n109_, new_n110_, new_n112_,
    new_n113_, new_n116_, new_n117_, new_n118_, new_n119_, new_n120_,
    new_n121_, new_n122_, new_n123_, new_n124_, new_n125_, new_n126_,
    new_n127_, new_n128_, new_n129_, new_n130_, new_n131_, new_n132_,
    new_n133_, new_n134_, new_n135_, new_n136_, new_n137_, new_n138_,
    new_n139_, new_n140_, new_n141_, new_n143_, new_n144_, new_n145_,
    new_n146_, new_n147_, new_n148_, new_n149_, new_n150_, new_n151_,
    new_n152_, new_n153_, new_n154_, new_n155_, new_n156_, new_n157_,
    new_n158_, new_n159_, new_n160_, new_n161_, new_n162_, new_n163_,
    new_n164_, new_n165_, new_n166_, new_n167_, new_n168_, new_n170_,
    new_n171_, new_n172_, new_n173_, new_n174_, new_n175_, new_n176_,
    new_n177_, new_n178_, new_n179_, new_n180_, new_n181_, new_n182_,
    new_n183_, new_n184_, new_n185_, new_n186_, new_n187_, new_n188_,
    new_n189_, new_n190_, new_n191_, new_n192_, new_n193_, new_n194_,
    new_n195_, new_n196_, new_n197_, new_n198_, new_n199_, new_n200_,
    new_n201_, new_n202_, new_n203_, new_n204_, new_n205_, new_n206_,
    new_n207_, new_n208_, new_n209_, new_n210_, new_n211_, new_n212_,
    new_n213_, new_n215_, new_n216_, new_n217_, new_n218_, new_n219_,
    new_n220_, new_n221_, new_n222_, new_n223_, new_n224_, new_n225_,
    new_n226_, new_n227_, new_n228_, new_n229_, new_n230_, new_n231_,
    new_n232_, new_n233_, new_n234_, new_n235_, new_n236_, new_n237_,
    new_n238_, new_n239_, new_n240_, new_n241_, new_n242_, new_n243_,
    new_n244_, new_n245_, new_n246_, new_n247_, new_n248_, new_n249_,
    new_n250_, new_n251_, new_n253_, new_n254_, new_n255_, new_n256_,
    new_n257_, new_n258_, new_n259_, new_n260_, new_n261_, new_n262_,
    new_n263_, new_n264_, new_n265_, new_n266_, new_n267_, new_n269_,
    new_n270_, new_n271_, new_n272_, new_n273_, new_n274_, new_n275_,
    new_n276_, new_n277_, new_n278_, new_n279_, new_n280_, new_n281_,
    new_n282_, new_n283_, new_n285_, new_n286_, new_n287_, new_n288_,
    new_n289_, new_n290_, new_n291_, new_n292_, new_n293_, new_n294_,
    new_n295_, new_n296_, new_n297_, new_n298_, new_n299_, new_n300_,
    new_n301_, new_n302_, new_n303_, new_n304_, new_n305_, new_n306_,
    new_n307_, new_n308_, new_n309_, new_n310_, new_n311_, new_n312_,
    new_n313_, new_n314_, new_n315_, new_n316_, new_n317_, new_n318_,
    new_n319_, new_n320_, new_n321_, new_n322_, new_n323_, new_n324_,
    new_n325_, new_n326_, new_n327_, new_n329_, new_n330_, new_n331_,
    new_n332_, new_n333_, new_n334_, new_n335_, new_n336_, new_n337_,
    new_n338_, new_n339_, new_n340_, new_n341_, new_n342_, new_n344_,
    new_n345_, new_n346_, new_n347_, new_n348_, new_n349_, new_n350_,
    new_n351_, new_n352_, new_n353_, new_n354_, new_n355_, new_n356_,
    new_n357_, new_n359_, new_n360_, new_n361_, new_n362_, new_n363_,
    new_n364_, new_n365_, new_n366_, new_n367_, new_n368_, new_n369_,
    new_n370_, new_n371_, new_n372_, new_n374_, new_n375_, new_n376_,
    new_n377_, new_n378_, new_n379_, new_n380_, new_n381_, new_n382_,
    new_n383_, new_n384_, new_n385_, new_n386_, new_n387_;
  nor2 g000(.dina(G6), .dinb(G16), .dout(new_n87_));
  nab2 g001(.dina(G8), .dinb(new_n87_), .dout(G855));
  nor2 g002(.dina(G6), .dinb(G7), .dout(new_n89_));
  nab2 g003(.dina(G17), .dinb(new_n89_), .dout(G856));
  nab2 g004(.dina(G8), .dinb(new_n89_), .dout(G857));
  nor2 g005(.dina(G18), .dinb(G19), .dout(G858));
  nor2 g006(.dina(G1), .dinb(G2), .dout(new_n93_));
  nab2 g007(.dina(G3), .dinb(new_n93_), .dout(new_n94_));
  nab2 g008(.dina(G4), .dinb(new_n94_), .dout(G859));
  nor2 g009(.dina(G1), .dinb(G5), .dout(new_n96_));
  and1 g010(.dina(G3), .dinb(G4), .dout(new_n97_));
  anb2 g011(.dina(new_n96_), .dinb(new_n97_), .dout(new_n98_));
  anb1 g012(.dina(G857), .dinb(new_n98_), .dout(G860));
  nor2 g013(.dina(G11), .dinb(G16), .dout(new_n100_));
  anb1 g014(.dina(G17), .dinb(new_n100_), .dout(G861));
  nor2 g015(.dina(G7), .dinb(G11), .dout(new_n102_));
  anb1 g016(.dina(G17), .dinb(new_n102_), .dout(G862));
  anb1 g017(.dina(G8), .dinb(new_n102_), .dout(G863));
  nor1 g018(.dina(G20), .dinb(G21), .dout(new_n105_));
  anb2 g019(.dina(new_n105_), .dinb(G23), .dout(G864));
  nor1 g020(.dina(G857), .dinb(new_n98_), .dout(G865));
  nab2 g021(.dina(G9), .dinb(new_n96_), .dout(G866));
  nab2 g022(.dina(G10), .dinb(new_n94_), .dout(new_n109_));
  and1 g023(.dina(G6), .dinb(G12), .dout(new_n110_));
  anb2 g024(.dina(new_n109_), .dinb(new_n110_), .dout(G867));
  nor2 g025(.dina(G11), .dinb(G12), .dout(new_n112_));
  anb1 g026(.dina(G15), .dinb(new_n112_), .dout(new_n113_));
  anb2 g027(.dina(new_n109_), .dinb(new_n113_), .dout(G868));
  anb2 g028(.dina(new_n105_), .dinb(G22), .dout(G869));
  nor1 g029(.dina(G24), .dinb(G25), .dout(new_n116_));
  nor2 g030(.dina(G24), .dinb(G25), .dout(new_n117_));
  anb2 g031(.dina(new_n116_), .dinb(new_n117_), .dout(new_n118_));
  and2 g032(.dina(G26), .dinb(G27), .dout(new_n119_));
  and1 g033(.dina(G26), .dinb(G27), .dout(new_n120_));
  anb1 g034(.dina(new_n119_), .dinb(new_n120_), .dout(new_n121_));
  anb1 g035(.dina(new_n118_), .dinb(new_n121_), .dout(new_n122_));
  anb2 g036(.dina(new_n118_), .dinb(new_n121_), .dout(new_n123_));
  anb2 g037(.dina(new_n122_), .dinb(new_n123_), .dout(new_n124_));
  anb1 g038(.dina(G32), .dinb(new_n124_), .dout(new_n125_));
  anb2 g039(.dina(G32), .dinb(new_n124_), .dout(new_n126_));
  anb2 g040(.dina(new_n125_), .dinb(new_n126_), .dout(new_n127_));
  nor1 g041(.dina(G28), .dinb(G29), .dout(new_n128_));
  nor2 g042(.dina(G28), .dinb(G29), .dout(new_n129_));
  anb2 g043(.dina(new_n128_), .dinb(new_n129_), .dout(new_n130_));
  and2 g044(.dina(G30), .dinb(G31), .dout(new_n131_));
  and1 g045(.dina(G30), .dinb(G31), .dout(new_n132_));
  anb1 g046(.dina(new_n131_), .dinb(new_n132_), .dout(new_n133_));
  anb1 g047(.dina(new_n130_), .dinb(new_n133_), .dout(new_n134_));
  anb2 g048(.dina(new_n130_), .dinb(new_n133_), .dout(new_n135_));
  anb2 g049(.dina(new_n134_), .dinb(new_n135_), .dout(new_n136_));
  nab2 g050(.dina(G33), .dinb(new_n136_), .dout(new_n137_));
  nab1 g051(.dina(G33), .dinb(new_n136_), .dout(new_n138_));
  anb1 g052(.dina(new_n137_), .dinb(new_n138_), .dout(new_n139_));
  anb1 g053(.dina(new_n127_), .dinb(new_n139_), .dout(new_n140_));
  anb2 g054(.dina(new_n127_), .dinb(new_n139_), .dout(new_n141_));
  anb2 g055(.dina(new_n140_), .dinb(new_n141_), .dout(G870));
  nor1 g056(.dina(G41), .dinb(G42), .dout(new_n143_));
  nor2 g057(.dina(G41), .dinb(G42), .dout(new_n144_));
  anb2 g058(.dina(new_n143_), .dinb(new_n144_), .dout(new_n145_));
  and2 g059(.dina(G43), .dinb(G44), .dout(new_n146_));
  and1 g060(.dina(G43), .dinb(G44), .dout(new_n147_));
  anb1 g061(.dina(new_n146_), .dinb(new_n147_), .dout(new_n148_));
  anb1 g062(.dina(new_n145_), .dinb(new_n148_), .dout(new_n149_));
  anb2 g063(.dina(new_n145_), .dinb(new_n148_), .dout(new_n150_));
  anb2 g064(.dina(new_n149_), .dinb(new_n150_), .dout(new_n151_));
  anb1 g065(.dina(G32), .dinb(new_n151_), .dout(new_n152_));
  anb2 g066(.dina(G32), .dinb(new_n151_), .dout(new_n153_));
  anb2 g067(.dina(new_n152_), .dinb(new_n153_), .dout(new_n154_));
  nor1 g068(.dina(G45), .dinb(G46), .dout(new_n155_));
  nor2 g069(.dina(G45), .dinb(G46), .dout(new_n156_));
  anb2 g070(.dina(new_n155_), .dinb(new_n156_), .dout(new_n157_));
  and2 g071(.dina(G47), .dinb(G48), .dout(new_n158_));
  and1 g072(.dina(G47), .dinb(G48), .dout(new_n159_));
  anb1 g073(.dina(new_n158_), .dinb(new_n159_), .dout(new_n160_));
  anb1 g074(.dina(new_n157_), .dinb(new_n160_), .dout(new_n161_));
  anb2 g075(.dina(new_n157_), .dinb(new_n160_), .dout(new_n162_));
  anb2 g076(.dina(new_n161_), .dinb(new_n162_), .dout(new_n163_));
  nab2 g077(.dina(G49), .dinb(new_n163_), .dout(new_n164_));
  nab1 g078(.dina(G49), .dinb(new_n163_), .dout(new_n165_));
  anb1 g079(.dina(new_n164_), .dinb(new_n165_), .dout(new_n166_));
  anb1 g080(.dina(new_n154_), .dinb(new_n166_), .dout(new_n167_));
  anb2 g081(.dina(new_n154_), .dinb(new_n166_), .dout(new_n168_));
  anb2 g082(.dina(new_n167_), .dinb(new_n168_), .dout(G871));
  nor2 g083(.dina(G11), .dinb(G40), .dout(new_n170_));
  anb2 g084(.dina(G866), .dinb(new_n170_), .dout(new_n171_));
  anb1 g085(.dina(G4), .dinb(new_n171_), .dout(new_n172_));
  anb1 g086(.dina(G1), .dinb(new_n172_), .dout(new_n173_));
  anb1 g087(.dina(G39), .dinb(new_n173_), .dout(new_n174_));
  anb1 g088(.dina(G17), .dinb(new_n87_), .dout(new_n175_));
  anb2 g089(.dina(G866), .dinb(new_n175_), .dout(new_n176_));
  anb1 g090(.dina(G10), .dinb(G60), .dout(new_n177_));
  anb2 g091(.dina(new_n176_), .dinb(new_n177_), .dout(new_n178_));
  and2 g092(.dina(G4), .dinb(G8), .dout(new_n179_));
  and1 g093(.dina(G4), .dinb(G8), .dout(new_n180_));
  anb1 g094(.dina(new_n179_), .dinb(new_n180_), .dout(new_n181_));
  anb2 g095(.dina(new_n170_), .dinb(new_n181_), .dout(new_n182_));
  and2 g096(.dina(G866), .dinb(new_n182_), .dout(new_n183_));
  nab2 g097(.dina(G8), .dinb(new_n100_), .dout(new_n184_));
  and1 g098(.dina(G4), .dinb(G9), .dout(new_n185_));
  anb2 g099(.dina(new_n93_), .dinb(new_n185_), .dout(new_n186_));
  anb1 g100(.dina(new_n184_), .dinb(new_n186_), .dout(new_n187_));
  anb1 g101(.dina(new_n183_), .dinb(new_n187_), .dout(new_n188_));
  anb2 g102(.dina(new_n188_), .dinb(G31), .dout(new_n189_));
  anb2 g103(.dina(new_n174_), .dinb(new_n189_), .dout(new_n190_));
  anb1 g104(.dina(new_n178_), .dinb(new_n190_), .dout(new_n191_));
  anb2 g105(.dina(new_n191_), .dinb(G48), .dout(new_n192_));
  nor1 g106(.dina(G53), .dinb(new_n192_), .dout(new_n193_));
  anb1 g107(.dina(new_n191_), .dinb(G48), .dout(new_n194_));
  and2 g108(.dina(new_n193_), .dinb(new_n194_), .dout(new_n195_));
  and1 g109(.dina(G51), .dinb(G58), .dout(new_n196_));
  anb1 g110(.dina(new_n195_), .dinb(new_n196_), .dout(new_n197_));
  anb1 g111(.dina(G58), .dinb(new_n194_), .dout(new_n198_));
  anb1 g112(.dina(G51), .dinb(new_n198_), .dout(new_n199_));
  nab1 g113(.dina(G52), .dinb(new_n192_), .dout(new_n200_));
  anb2 g114(.dina(new_n199_), .dinb(new_n200_), .dout(new_n201_));
  anb2 g115(.dina(new_n197_), .dinb(new_n201_), .dout(new_n202_));
  anb1 g116(.dina(G54), .dinb(new_n191_), .dout(new_n203_));
  nor2 g117(.dina(G8), .dinb(G13), .dout(new_n204_));
  anb1 g118(.dina(G14), .dinb(new_n204_), .dout(new_n205_));
  nab1 g119(.dina(new_n112_), .dinb(new_n205_), .dout(new_n206_));
  anb2 g120(.dina(new_n109_), .dinb(new_n206_), .dout(new_n207_));
  nab2 g121(.dina(G48), .dinb(new_n207_), .dout(new_n208_));
  and1 g122(.dina(G55), .dinb(G59), .dout(new_n209_));
  nor2 g123(.dina(G30), .dinb(G50), .dout(new_n210_));
  anb2 g124(.dina(new_n209_), .dinb(new_n210_), .dout(new_n211_));
  anb1 g125(.dina(new_n208_), .dinb(new_n211_), .dout(new_n212_));
  anb2 g126(.dina(new_n203_), .dinb(new_n212_), .dout(new_n213_));
  anb1 g127(.dina(new_n202_), .dinb(new_n213_), .dout(G872));
  anb1 g128(.dina(G36), .dinb(new_n173_), .dout(new_n215_));
  anb2 g129(.dina(new_n188_), .dinb(G29), .dout(new_n216_));
  anb2 g130(.dina(new_n215_), .dinb(new_n216_), .dout(new_n217_));
  anb1 g131(.dina(new_n178_), .dinb(new_n217_), .dout(new_n218_));
  anb2 g132(.dina(new_n218_), .dinb(G46), .dout(new_n219_));
  anb2 g133(.dina(G46), .dinb(new_n218_), .dout(new_n220_));
  anb1 g134(.dina(G37), .dinb(new_n173_), .dout(new_n221_));
  anb2 g135(.dina(new_n188_), .dinb(G30), .dout(new_n222_));
  anb2 g136(.dina(new_n221_), .dinb(new_n222_), .dout(new_n223_));
  anb1 g137(.dina(new_n178_), .dinb(new_n223_), .dout(new_n224_));
  anb2 g138(.dina(new_n224_), .dinb(G47), .dout(new_n225_));
  anb2 g139(.dina(G47), .dinb(new_n224_), .dout(new_n226_));
  anb1 g140(.dina(new_n192_), .dinb(new_n198_), .dout(new_n227_));
  anb1 g141(.dina(new_n226_), .dinb(new_n227_), .dout(new_n228_));
  anb1 g142(.dina(new_n225_), .dinb(new_n228_), .dout(new_n229_));
  anb1 g143(.dina(new_n220_), .dinb(new_n229_), .dout(new_n230_));
  anb1 g144(.dina(new_n219_), .dinb(new_n230_), .dout(new_n231_));
  anb2 g145(.dina(new_n231_), .dinb(G51), .dout(new_n232_));
  anb1 g146(.dina(G35), .dinb(new_n173_), .dout(new_n233_));
  anb2 g147(.dina(new_n188_), .dinb(G28), .dout(new_n234_));
  anb2 g148(.dina(new_n233_), .dinb(new_n234_), .dout(new_n235_));
  anb1 g149(.dina(new_n178_), .dinb(new_n235_), .dout(new_n236_));
  anb1 g150(.dina(G45), .dinb(new_n236_), .dout(new_n237_));
  anb2 g151(.dina(G53), .dinb(new_n237_), .dout(new_n238_));
  anb1 g152(.dina(new_n236_), .dinb(G45), .dout(new_n239_));
  anb1 g153(.dina(new_n238_), .dinb(new_n239_), .dout(new_n240_));
  anb1 g154(.dina(new_n232_), .dinb(new_n240_), .dout(new_n241_));
  nor1 g155(.dina(new_n231_), .dinb(new_n239_), .dout(new_n242_));
  anb1 g156(.dina(G51), .dinb(new_n242_), .dout(new_n243_));
  nor1 g157(.dina(G52), .dinb(new_n237_), .dout(new_n244_));
  anb2 g158(.dina(new_n243_), .dinb(new_n244_), .dout(new_n245_));
  anb2 g159(.dina(new_n241_), .dinb(new_n245_), .dout(new_n246_));
  anb1 g160(.dina(G54), .dinb(new_n236_), .dout(new_n247_));
  nor2 g161(.dina(G27), .dinb(G50), .dout(new_n248_));
  anb1 g162(.dina(G45), .dinb(new_n207_), .dout(new_n249_));
  anb1 g163(.dina(new_n248_), .dinb(new_n249_), .dout(new_n250_));
  anb2 g164(.dina(new_n247_), .dinb(new_n250_), .dout(new_n251_));
  anb1 g165(.dina(new_n246_), .dinb(new_n251_), .dout(G873));
  nor1 g166(.dina(G53), .dinb(new_n219_), .dout(new_n253_));
  nab2 g167(.dina(new_n220_), .dinb(new_n253_), .dout(new_n254_));
  anb1 g168(.dina(G51), .dinb(new_n229_), .dout(new_n255_));
  anb1 g169(.dina(new_n254_), .dinb(new_n255_), .dout(new_n256_));
  anb1 g170(.dina(G51), .dinb(new_n230_), .dout(new_n257_));
  nab1 g171(.dina(G52), .dinb(new_n219_), .dout(new_n258_));
  anb2 g172(.dina(new_n257_), .dinb(new_n258_), .dout(new_n259_));
  anb2 g173(.dina(new_n256_), .dinb(new_n259_), .dout(new_n260_));
  anb1 g174(.dina(G54), .dinb(new_n218_), .dout(new_n261_));
  nab2 g175(.dina(G46), .dinb(new_n207_), .dout(new_n262_));
  and1 g176(.dina(G55), .dinb(G56), .dout(new_n263_));
  nor2 g177(.dina(G28), .dinb(G50), .dout(new_n264_));
  anb2 g178(.dina(new_n263_), .dinb(new_n264_), .dout(new_n265_));
  anb1 g179(.dina(new_n262_), .dinb(new_n265_), .dout(new_n266_));
  anb2 g180(.dina(new_n261_), .dinb(new_n266_), .dout(new_n267_));
  anb1 g181(.dina(new_n260_), .dinb(new_n267_), .dout(G874));
  nor1 g182(.dina(G53), .dinb(new_n225_), .dout(new_n269_));
  nab2 g183(.dina(new_n226_), .dinb(new_n269_), .dout(new_n270_));
  anb1 g184(.dina(G51), .dinb(new_n227_), .dout(new_n271_));
  anb1 g185(.dina(new_n270_), .dinb(new_n271_), .dout(new_n272_));
  anb1 g186(.dina(G51), .dinb(new_n228_), .dout(new_n273_));
  nab1 g187(.dina(G52), .dinb(new_n225_), .dout(new_n274_));
  anb2 g188(.dina(new_n273_), .dinb(new_n274_), .dout(new_n275_));
  anb2 g189(.dina(new_n272_), .dinb(new_n275_), .dout(new_n276_));
  anb1 g190(.dina(G54), .dinb(new_n224_), .dout(new_n277_));
  nab2 g191(.dina(G47), .dinb(new_n207_), .dout(new_n278_));
  and1 g192(.dina(G55), .dinb(G57), .dout(new_n279_));
  nor2 g193(.dina(G29), .dinb(G50), .dout(new_n280_));
  anb2 g194(.dina(new_n279_), .dinb(new_n280_), .dout(new_n281_));
  anb1 g195(.dina(new_n278_), .dinb(new_n281_), .dout(new_n282_));
  anb2 g196(.dina(new_n277_), .dinb(new_n282_), .dout(new_n283_));
  anb1 g197(.dina(new_n276_), .dinb(new_n283_), .dout(G875));
  anb2 g198(.dina(new_n188_), .dinb(G24), .dout(new_n285_));
  nab2 g199(.dina(G10), .dinb(new_n171_), .dout(new_n286_));
  anb1 g200(.dina(G35), .dinb(new_n286_), .dout(new_n287_));
  nor2 g201(.dina(G2), .dinb(G34), .dout(new_n288_));
  anb1 g202(.dina(G4), .dinb(G60), .dout(new_n289_));
  anb2 g203(.dina(new_n176_), .dinb(new_n289_), .dout(new_n290_));
  and1 g204(.dina(new_n288_), .dinb(new_n290_), .dout(new_n291_));
  anb2 g205(.dina(new_n287_), .dinb(new_n291_), .dout(new_n292_));
  anb1 g206(.dina(new_n285_), .dinb(new_n292_), .dout(new_n293_));
  anb2 g207(.dina(new_n293_), .dinb(G41), .dout(new_n294_));
  anb2 g208(.dina(new_n188_), .dinb(G25), .dout(new_n295_));
  anb1 g209(.dina(G36), .dinb(new_n286_), .dout(new_n296_));
  and1 g210(.dina(G9), .dinb(G34), .dout(new_n297_));
  anb1 g211(.dina(new_n290_), .dinb(new_n297_), .dout(new_n298_));
  anb2 g212(.dina(new_n296_), .dinb(new_n298_), .dout(new_n299_));
  anb1 g213(.dina(new_n295_), .dinb(new_n299_), .dout(new_n300_));
  anb2 g214(.dina(new_n300_), .dinb(G42), .dout(new_n301_));
  anb2 g215(.dina(G42), .dinb(new_n300_), .dout(new_n302_));
  anb2 g216(.dina(new_n188_), .dinb(G26), .dout(new_n303_));
  anb1 g217(.dina(G37), .dinb(new_n286_), .dout(new_n304_));
  and1 g218(.dina(G4), .dinb(G34), .dout(new_n305_));
  anb1 g219(.dina(new_n290_), .dinb(new_n305_), .dout(new_n306_));
  anb2 g220(.dina(new_n304_), .dinb(new_n306_), .dout(new_n307_));
  anb1 g221(.dina(new_n303_), .dinb(new_n307_), .dout(new_n308_));
  anb2 g222(.dina(new_n308_), .dinb(G43), .dout(new_n309_));
  anb2 g223(.dina(G43), .dinb(new_n308_), .dout(new_n310_));
  nor1 g224(.dina(new_n237_), .dinb(new_n242_), .dout(new_n311_));
  anb2 g225(.dina(new_n188_), .dinb(G27), .dout(new_n312_));
  anb1 g226(.dina(G39), .dinb(new_n286_), .dout(new_n313_));
  and1 g227(.dina(G34), .dinb(G38), .dout(new_n314_));
  anb1 g228(.dina(new_n290_), .dinb(new_n314_), .dout(new_n315_));
  anb2 g229(.dina(new_n313_), .dinb(new_n315_), .dout(new_n316_));
  anb1 g230(.dina(new_n312_), .dinb(new_n316_), .dout(new_n317_));
  anb1 g231(.dina(new_n317_), .dinb(G44), .dout(new_n318_));
  nor1 g232(.dina(new_n311_), .dinb(new_n318_), .dout(new_n319_));
  anb2 g233(.dina(new_n317_), .dinb(G44), .dout(new_n320_));
  anb2 g234(.dina(new_n319_), .dinb(new_n320_), .dout(new_n321_));
  and1 g235(.dina(new_n310_), .dinb(new_n321_), .dout(new_n322_));
  nab2 g236(.dina(new_n309_), .dinb(new_n322_), .dout(new_n323_));
  and1 g237(.dina(new_n302_), .dinb(new_n323_), .dout(new_n324_));
  nab2 g238(.dina(new_n301_), .dinb(new_n324_), .dout(new_n325_));
  anb1 g239(.dina(new_n293_), .dinb(G41), .dout(new_n326_));
  anb1 g240(.dina(new_n325_), .dinb(new_n326_), .dout(new_n327_));
  anb1 g241(.dina(new_n294_), .dinb(new_n327_), .dout(G876));
  anb2 g242(.dina(new_n318_), .dinb(new_n320_), .dout(new_n329_));
  anb2 g243(.dina(new_n311_), .dinb(new_n329_), .dout(new_n330_));
  anb1 g244(.dina(new_n311_), .dinb(new_n329_), .dout(new_n331_));
  anb1 g245(.dina(new_n330_), .dinb(new_n331_), .dout(new_n332_));
  anb2 g246(.dina(new_n332_), .dinb(G51), .dout(new_n333_));
  anb1 g247(.dina(G52), .dinb(new_n329_), .dout(new_n334_));
  nab2 g248(.dina(G53), .dinb(new_n320_), .dout(new_n335_));
  anb1 g249(.dina(G54), .dinb(new_n317_), .dout(new_n336_));
  nor2 g250(.dina(G26), .dinb(G50), .dout(new_n337_));
  anb1 g251(.dina(G44), .dinb(new_n207_), .dout(new_n338_));
  anb1 g252(.dina(new_n337_), .dinb(new_n338_), .dout(new_n339_));
  anb2 g253(.dina(new_n336_), .dinb(new_n339_), .dout(new_n340_));
  anb1 g254(.dina(new_n335_), .dinb(new_n340_), .dout(new_n341_));
  anb2 g255(.dina(new_n334_), .dinb(new_n341_), .dout(new_n342_));
  anb1 g256(.dina(new_n333_), .dinb(new_n342_), .dout(G877));
  nab2 g257(.dina(new_n294_), .dinb(new_n326_), .dout(new_n344_));
  anb1 g258(.dina(new_n325_), .dinb(new_n344_), .dout(new_n345_));
  anb1 g259(.dina(new_n344_), .dinb(new_n325_), .dout(new_n346_));
  anb1 g260(.dina(G51), .dinb(new_n346_), .dout(new_n347_));
  anb2 g261(.dina(new_n345_), .dinb(new_n347_), .dout(new_n348_));
  anb1 g262(.dina(G52), .dinb(new_n344_), .dout(new_n349_));
  nab2 g263(.dina(G53), .dinb(new_n294_), .dout(new_n350_));
  anb1 g264(.dina(G54), .dinb(new_n293_), .dout(new_n351_));
  nor2 g265(.dina(G50), .dinb(G60), .dout(new_n352_));
  anb1 g266(.dina(G41), .dinb(new_n207_), .dout(new_n353_));
  anb1 g267(.dina(new_n352_), .dinb(new_n353_), .dout(new_n354_));
  anb2 g268(.dina(new_n351_), .dinb(new_n354_), .dout(new_n355_));
  anb1 g269(.dina(new_n350_), .dinb(new_n355_), .dout(new_n356_));
  anb2 g270(.dina(new_n349_), .dinb(new_n356_), .dout(new_n357_));
  anb1 g271(.dina(new_n348_), .dinb(new_n357_), .dout(G878));
  nor2 g272(.dina(new_n301_), .dinb(new_n302_), .dout(new_n359_));
  anb1 g273(.dina(new_n323_), .dinb(new_n359_), .dout(new_n360_));
  anb1 g274(.dina(new_n359_), .dinb(new_n323_), .dout(new_n361_));
  anb1 g275(.dina(G51), .dinb(new_n361_), .dout(new_n362_));
  anb2 g276(.dina(new_n360_), .dinb(new_n362_), .dout(new_n363_));
  anb1 g277(.dina(G52), .dinb(new_n359_), .dout(new_n364_));
  nab2 g278(.dina(G53), .dinb(new_n301_), .dout(new_n365_));
  anb1 g279(.dina(G54), .dinb(new_n300_), .dout(new_n366_));
  nor2 g280(.dina(G24), .dinb(G50), .dout(new_n367_));
  anb1 g281(.dina(G42), .dinb(new_n207_), .dout(new_n368_));
  anb1 g282(.dina(new_n367_), .dinb(new_n368_), .dout(new_n369_));
  anb2 g283(.dina(new_n366_), .dinb(new_n369_), .dout(new_n370_));
  anb1 g284(.dina(new_n365_), .dinb(new_n370_), .dout(new_n371_));
  anb2 g285(.dina(new_n364_), .dinb(new_n371_), .dout(new_n372_));
  anb1 g286(.dina(new_n363_), .dinb(new_n372_), .dout(G879));
  nor2 g287(.dina(new_n309_), .dinb(new_n310_), .dout(new_n374_));
  anb1 g288(.dina(new_n321_), .dinb(new_n374_), .dout(new_n375_));
  anb1 g289(.dina(new_n374_), .dinb(new_n321_), .dout(new_n376_));
  anb1 g290(.dina(G51), .dinb(new_n376_), .dout(new_n377_));
  anb2 g291(.dina(new_n375_), .dinb(new_n377_), .dout(new_n378_));
  anb1 g292(.dina(G52), .dinb(new_n374_), .dout(new_n379_));
  nab2 g293(.dina(G53), .dinb(new_n309_), .dout(new_n380_));
  anb1 g294(.dina(G54), .dinb(new_n308_), .dout(new_n381_));
  nor2 g295(.dina(G25), .dinb(G50), .dout(new_n382_));
  anb1 g296(.dina(G43), .dinb(new_n207_), .dout(new_n383_));
  anb1 g297(.dina(new_n382_), .dinb(new_n383_), .dout(new_n384_));
  anb2 g298(.dina(new_n381_), .dinb(new_n384_), .dout(new_n385_));
  anb1 g299(.dina(new_n380_), .dinb(new_n385_), .dout(new_n386_));
  anb2 g300(.dina(new_n379_), .dinb(new_n386_), .dout(new_n387_));
  anb1 g301(.dina(new_n378_), .dinb(new_n387_), .dout(G880));
endmodule


