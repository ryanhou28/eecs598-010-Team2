module c880(G1,G10,G11,G12,G13,G14,G15,G16,G17,G18,G19,G2,G20,G21,G22,G23,
  G24,G25,G26,G27,G28,G29,G3,G30,G31,G32,G33,G34,G35,G36,G37,G38,G39,G4,G40,
  G41,G42,G43,G44,G45,G46,G47,G48,G49,G5,G50,G51,G52,G53,G54,G55,G56,G57,G58,
  G59,G6,G60,G7,G8,G855,G856,G857,G858,G859,G860,G861,G862,G863,G864,G865,G866,
  G867,G868,G869,G870,G871,G872,G873,G874,G875,G876,G877,G878,G879,G880,G9);
input G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15,G16,G17,G18,G19,G20,
  G21,G22,G23,G24,G25,G26,G27,G28,G29,G30,G31,G32,G33,G34,G35,G36,G37,G38,G39,
  G40,G41,G42,G43,G44,G45,G46,G47,G48,G49,G50,G51,G52,G53,G54,G55,G56,G57,G58,
  G59,G60;
output G855,G856,G857,G858,G859,G860,G861,G862,G863,G864,G865,G866,G867,G868,
  G869,G870,G871,G872,G873,G874,G875,G876,G877,G878,G879,G880;

  wire G269,G270,G273,G276,G279,G280,G284,G285,G286,G287,G290,G291,G292,G293,
    G294,G295,G296,G297,G298,G301,G302,G303,G304,G305,G306,G307,G308,G309,G310,
    G316,G317,G318,G319,G322,G323,G324,G325,G326,G327,G328,G329,G330,G331,G332,
    G333,G334,G335,G336,G337,G338,G339,G340,G341,G342,G343,G344,G345,G346,G347,
    G348,G349,G350,G351,G352,G353,G354,G355,G356,G357,G360,G363,G366,G369,G375,
    G376,G379,G382,G385,G388,G389,G395,G396,G397,G398,G399,G400,G401,G402,G403,
    G404,G405,G406,G407,G408,G409,G410,G411,G412,G413,G414,G415,G416,G417,G422,
    G427,G432,G433,G434,G435,G436,G445,G448,G451,G460,G461,G462,G463,G464,G465,
    G466,G467,G468,G473,G474,G475,G476,G477,G480,G483,G484,G485,G486,G487,G488,
    G489,G490,G491,G492,G493,G494,G495,G496,G497,G498,G499,G500,G501,G502,G503,
    G504,G505,G506,G507,G508,G509,G510,G511,G512,G513,G514,G515,G518,G521,G522,
    G523,G524,G525,G526,G527,G528,G529,G532,G535,G536,G537,G538,G542,G546,G550,
    G554,G558,G562,G566,G570,G571,G572,G573,G574,G575,G578,G581,G582,G585,G590,
    G591,G594,G600,G601,G604,G609,G610,G613,G616,G617,G620,G625,G626,G629,G635,
    G636,G639,G644,G645,G646,G647,G650,G654,G655,G658,G662,G663,G667,G671,G672,
    G677,G681,G682,G685,G689,G690,G693,G697,G698,G702,G706,G707,G712,G716,G717,
    G718,G719,G720,G721,G722,G723,G724,G725,G726,G727,G728,G729,G730,G731,G732,
    G733,G734,G735,G736,G737,G738,G739,G740,G741,G742,G743,G744,G745,G746,G747,
    G748,G749,G750,G751,G752,G753,G754,G755,G756,G760,G761,G764,G765,G768,G769,
    G770,G771,G772,G773,G774,G775,G776,G777,G778,G779,G785,G786,G787,G788,G789,
    G790,G791,G792,G793,G794,G795,G796,G797,G798,G802,G805,G808,G809,G810,G811,
    G812,G813,G814,G815,G816,G817,G818,G819,G820,G821,G822,G823,G824,G825,G826,
    G827,G828,G829,G830,G831,G832,G833,G834,G835,G836,G837,G838,G839,G840,G841,
    G842,G843,G844,G845,G846,G847,G848,G849,G850,G851,G852,G853,G854;

  nand (G269,G1,G2,G3,G4);
  nand (G270,G1,G5,G3,G4);
  and (G273,G6,G7,G8);
  and (G276,G1,G5,G9);
  nand (G279,G1,G2,G9,G4);
  nand (G280,G1,G2,G3,G10);
  nand (G284,G11,G8,G12,G13);
  nand (G285,G6,G12);
  nand (G286,G11,G12,G15);
  and (G287,G6,G16,G17);
  and (G290,G6,G16,G8);
  and (G291,G6,G7,G17);
  and (G292,G6,G7,G8);
  and (G293,G11,G16,G17);
  and (G294,G11,G16,G8);
  and (G295,G11,G7,G17);
  and (G296,G11,G7,G8);
  and (G297,G18,G19);
  or (G298,G20,G21);
  nand (G301,G24,G25);
  or (G302,G24,G25);
  nand (G303,G26,G27);
  or (G304,G26,G27);
  nand (G305,G28,G29);
  or (G306,G28,G29);
  nand (G307,G30,G31);
  or (G308,G30,G31);
  and (G309,G2,G34);
  not (G310,G60);
  and (G316,G9,G34);
  and (G317,G4,G34);
  and (G318,G38,G34);
  nand (G319,G11,G40);
  nor (G322,G4,G8);
  and (G323,G4,G8);
  nand (G324,G41,G42);
  or (G325,G41,G42);
  nand (G326,G43,G44);
  or (G327,G43,G44);
  nand (G328,G45,G46);
  or (G329,G45,G46);
  nand (G330,G47,G48);
  or (G331,G47,G48);
  and (G332,G50,G24);
  and (G333,G50,G25);
  and (G334,G50,G26);
  and (G335,G50,G27);
  and (G336,G50,G28);
  and (G337,G55,G56);
  and (G338,G50,G29);
  and (G339,G55,G57);
  and (G340,G50,G30);
  and (G341,G55,G59);
  not (G342,G269);
  not (G343,G273);
  or (G344,G270,G273);
  not (G345,G276);
  not (G346,G276);
  not (G347,G279);
  nor (G348,G280,G284);
  or (G349,G280,G285);
  or (G350,G280,G286);
  not (G351,G293);
  not (G352,G294);
  not (G353,G295);
  not (G354,G296);
  nand (G355,G22,G298);
  and (G356,G23,G298);
  nand (G357,G301,G302);
  nand (G360,G303,G304);
  nand (G363,G305,G306);
  nand (G366,G307,G308);
  not (G369,G310);
  nor (G375,G322,G323);
  nand (G376,G324,G325);
  nand (G379,G326,G327);
  nand (G382,G328,G329);
  nand (G385,G330,G331);
  or (G388,G270,G343);
  not (G389,G345);
  not (G395,G346);
  and (G396,G348,G14);
  not (G397,G349);
  not (G398,G350);
  not (G399,G355);
  not (G400,G357);
  not (G401,G360);
  and (G402,G357,G360);
  not (G403,G363);
  not (G404,G366);
  and (G405,G363,G366);
  nand (G406,G347,G352);
  not (G407,G376);
  not (G408,G379);
  and (G409,G376,G379);
  not (G410,G382);
  not (G411,G385);
  and (G412,G382,G385);
  and (G413,G50,G369);
  not (G414,G396);
  and (G415,G400,G401);
  and (G416,G403,G404);
  and (G417,G319,G389,G10);
  and (G422,G389,G4,G287);
  nand (G427,G389,G287,G10);
  nand (G432,G375,G11,G40,G389);
  nand (G433,G389,G319,G4);
  and (G434,G407,G408);
  and (G435,G410,G411);
  not (G436,G414);
  nor (G445,G402,G415);
  nor (G448,G405,G416);
  nand (G451,G432,G406);
  and (G460,G35,G417);
  and (G461,G310,G422);
  and (G462,G36,G417);
  and (G463,G310,G422);
  and (G464,G37,G417);
  and (G465,G310,G422);
  and (G466,G39,G417);
  and (G467,G310,G422);
  nand (G468,G433,G1);
  or (G473,G369,G427);
  or (G474,G369,G427);
  or (G475,G369,G427);
  or (G476,G369,G427);
  nor (G477,G409,G434);
  nor (G480,G412,G435);
  nand (G483,G32,G445);
  or (G484,G32,G445);
  nand (G485,G448,G33);
  or (G486,G448,G33);
  and (G487,G24,G451);
  nor (G488,G460,G461);
  and (G489,G25,G451);
  nor (G490,G462,G463);
  and (G491,G26,G451);
  nor (G492,G464,G465);
  and (G493,G27,G451);
  nor (G494,G466,G467);
  and (G495,G35,G468);
  and (G496,G28,G451);
  and (G497,G36,G468);
  and (G498,G29,G451);
  and (G499,G37,G468);
  and (G500,G30,G451);
  and (G501,G39,G468);
  and (G502,G31,G451);
  nand (G503,G32,G477);
  or (G504,G32,G477);
  nand (G505,G480,G49);
  or (G506,G480,G49);
  and (G507,G436,G41);
  and (G508,G436,G42);
  and (G509,G436,G43);
  and (G510,G436,G44);
  and (G511,G436,G45);
  nand (G512,G436,G46);
  nand (G513,G436,G47);
  nand (G514,G436,G48);
  nand (G515,G483,G484);
  nand (G518,G485,G486);
  nor (G521,G309,G487);
  nor (G522,G316,G489);
  nor (G523,G317,G491);
  nor (G524,G318,G493);
  nor (G525,G495,G496);
  nor (G526,G497,G498);
  nor (G527,G499,G500);
  nor (G528,G501,G502);
  nand (G529,G503,G504);
  nand (G532,G505,G506);
  not (G535,G515);
  not (G536,G518);
  and (G537,G515,G518);
  nand (G538,G521,G488);
  nand (G542,G522,G490);
  nand (G546,G523,G492);
  nand (G550,G524,G494);
  nand (G554,G473,G525);
  nand (G558,G474,G526);
  nand (G562,G475,G527);
  nand (G566,G476,G528);
  not (G570,G529);
  not (G571,G532);
  and (G572,G529,G532);
  and (G573,G535,G536);
  and (G574,G570,G571);
  nand (G575,G538,G41);
  or (G578,G538,G41);
  and (G581,G54,G538);
  nand (G582,G542,G42);
  or (G585,G542,G42);
  and (G590,G54,G542);
  nand (G591,G546,G43);
  or (G594,G546,G43);
  and (G600,G54,G546);
  nand (G601,G550,G44);
  or (G604,G550,G44);
  and (G609,G54,G550);
  nand (G610,G554,G45);
  or (G613,G554,G45);
  and (G616,G54,G554);
  nand (G617,G558,G46);
  or (G620,G558,G46);
  and (G625,G54,G558);
  nand (G626,G562,G47);
  or (G629,G562,G47);
  and (G635,G54,G562);
  nand (G636,G566,G48);
  or (G639,G566,G48);
  and (G644,G54,G566);
  nor (G645,G537,G573);
  nor (G646,G572,G574);
  not (G647,G575);
  and (G650,G578,G575);
  nor (G654,G581,G507);
  not (G655,G582);
  and (G658,G585,G582);
  nor (G662,G590,G508);
  not (G663,G591);
  and (G667,G594,G591);
  nor (G671,G600,G509);
  not (G672,G601);
  and (G677,G604,G601);
  nor (G681,G609,G510);
  not (G682,G610);
  and (G685,G613,G610);
  nor (G689,G616,G511);
  not (G690,G617);
  and (G693,G620,G617);
  nor (G697,G337,G625);
  not (G698,G626);
  and (G702,G629,G626);
  nor (G706,G339,G635);
  not (G707,G636);
  and (G712,G639,G636);
  nor (G716,G341,G644);
  nand (G717,G639,G58);
  nand (G718,G629,G639,G58);
  nand (G719,G620,G629,G639,G58);
  not (G720,G647);
  and (G721,G52,G650);
  and (G722,G53,G647);
  not (G723,G655);
  and (G724,G52,G658);
  and (G725,G53,G655);
  not (G726,G663);
  and (G727,G52,G667);
  and (G728,G53,G663);
  not (G729,G672);
  and (G730,G52,G677);
  and (G731,G53,G672);
  not (G732,G682);
  and (G733,G52,G685);
  and (G734,G53,G682);
  not (G735,G690);
  and (G736,G52,G693);
  and (G737,G53,G690);
  not (G738,G698);
  and (G739,G52,G702);
  and (G740,G53,G698);
  not (G741,G707);
  nor (G742,G712,G58);
  and (G743,G712,G58);
  and (G744,G52,G712);
  and (G745,G53,G707);
  nand (G746,G629,G707);
  nand (G747,G620,G698);
  nand (G748,G620,G629,G707);
  nand (G749,G594,G672);
  nand (G750,G585,G663);
  nand (G751,G585,G594,G672);
  nor (G752,G721,G722);
  nor (G753,G724,G725);
  nor (G754,G727,G728);
  nor (G755,G730,G731);
  nand (G756,G735,G747,G748,G719);
  nor (G760,G733,G734);
  nand (G761,G738,G746,G718);
  nor (G764,G736,G737);
  nand (G765,G741,G717);
  nor (G768,G739,G740);
  nor (G769,G742,G743);
  nor (G770,G744,G745);
  nor (G771,G685,G756);
  and (G772,G685,G756);
  nor (G773,G693,G761);
  and (G774,G693,G761);
  nor (G775,G702,G765);
  and (G776,G702,G765);
  and (G777,G51,G769);
  nand (G778,G613,G756);
  nand (G779,G778,G732);
  nor (G785,G771,G772);
  nor (G786,G773,G774);
  nor (G787,G775,G776);
  nor (G788,G340,G777);
  nor (G789,G677,G779);
  and (G790,G677,G779);
  and (G791,G51,G785);
  and (G792,G51,G786);
  and (G793,G51,G787);
  nand (G794,G788,G770,G716,G514);
  nand (G795,G604,G779);
  nand (G796,G594,G604,G779);
  nand (G797,G585,G594,G604,G779);
  nand (G798,G723,G750,G751,G797);
  nand (G802,G726,G749,G796);
  nand (G805,G729,G795);
  nor (G808,G789,G790);
  nor (G809,G335,G791);
  nor (G810,G336,G792);
  nor (G811,G338,G793);
  not (G812,G794);
  nor (G813,G650,G798);
  and (G814,G650,G798);
  nor (G815,G658,G802);
  and (G816,G658,G802);
  nor (G817,G667,G805);
  and (G818,G667,G805);
  and (G819,G51,G808);
  nand (G820,G809,G760,G689);
  nand (G821,G810,G764,G697,G512);
  nand (G822,G811,G768,G706,G513);
  not (G823,G812);
  nand (G824,G798,G578);
  nor (G825,G813,G814);
  nor (G826,G815,G816);
  nor (G827,G817,G818);
  nor (G828,G334,G819);
  not (G829,G820);
  not (G830,G821);
  not (G831,G822);
  and (G832,G720,G824);
  and (G833,G51,G825);
  and (G834,G51,G826);
  and (G835,G51,G827);
  nand (G836,G828,G755,G681);
  not (G837,G829);
  not (G838,G830);
  not (G839,G831);
  not (G840,G832);
  nor (G841,G413,G833);
  nor (G842,G332,G834);
  nor (G843,G333,G835);
  not (G844,G836);
  nand (G845,G841,G752,G654);
  nand (G846,G842,G753,G662);
  nand (G847,G843,G754,G671);
  not (G848,G844);
  not (G849,G845);
  not (G850,G846);
  not (G851,G847);
  not (G852,G849);
  not (G853,G850);
  not (G854,G851);
  not (G855,G290);
  not (G856,G291);
  not (G857,G292);
  not (G858,G297);
  not (G859,G342);
  not (G860,G344);
  not (G861,G351);
  not (G862,G353);
  not (G863,G354);
  not (G864,G356);
  not (G865,G388);
  not (G866,G395);
  not (G867,G397);
  not (G868,G398);
  not (G869,G399);
  not (G870,G645);
  not (G871,G646);
  not (G872,G823);
  not (G873,G837);
  not (G874,G838);
  not (G875,G839);
  not (G876,G840);
  not (G877,G848);
  not (G878,G852);
  not (G879,G853);
  not (G880,G854);

endmodule