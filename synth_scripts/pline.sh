file=$1
sed -i -E -e 's/clock,//g' -e 's/input +clock;//g' -e 's/@ +(posedge +clock)//g' $file
faig="${file%.v}_comb.aig"
faag="${file%.v}_comb.aag"
lcnt=$(yosys-abc -f pline.script -o $faig $file |  grep -Po "lat =\s+\d+" | grep -Po "\d+")
echo "$lcnt latches"
aigtoaig $faig $faag
fdup="${file%.v}_N.v"
fout="${file%.v}_SEQ.v"
fmap="${file%.v}_MAP.v"
ipython -c "from aig2cell import *;dumpscr(\"$faag\", \"$fdup\")" && echo "Split: $file"
yosys-abc -c "read $fdup; comb -L $lcnt; write $fout"
sed -i -E -e 's/clock,//g' -e 's/input +clock;//g' -e 's/@ +(posedge +clock)//g' $fout
yosys-abc -c "read $fout; read_library builtin.genlib; sop; attach; write $fmap"
sed -i -E -e 's/clock,//g' -e 's/input +clock;//g' -e 's/@ +(posedge +clock)//g' $fmap
yosys-abc -c "dsec $file $fout"
