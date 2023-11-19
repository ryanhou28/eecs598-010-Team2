file=$1
sed -i -E -e 's/clock,//g' -e 's/input +clock;//g' -e 's/@ +(posedge +clock)//g' $file
faig="${file%.v}_comb.aig"
faag="${file%.v}_comb.aag"
yosys-abc -f pline.script -o $faig $file > yoout.txt
lcnt=$(cat yoout.txt |  grep -Po "lat =\s+\d+" | grep -Po "\d+")
sed -n 's/.*\(([0-9]*)\).*/\1/p' yoout.txt > iol.txt
sed -n '/^[01]\+$/p' yoout.txt > bin.txt
hj=$(python parselvl.py)
rm yoout.txt
rm iol.txt
rm bin.txt
echo "$hj"
echo "$lcnt latches"
aigtoaig $faig $faag
fdup="${file%.v}_N.v"
fdro="${file%.v}_DRO.v"
fout="${file%.v}_SEQ.v"
fmap="${file%.v}_MAP.v"

command1=`cat <<EOF
from aig2cell import *
dumpscr("$faag", "$fdup")
EOF`
python -c "$command1"
echo "Split: $file"

# ipython -c "from aig2cell import *;dumpscr(\"$faag\", \"$fdup\")" && echo "Split: $file"

command2=`cat <<EOF
from aig2cell import *
dumpscr("$faag", "$fdro", L_cnt=$lcnt, Non_dbg=True, levels=$hj)
EOF`
python -c "$command2"
# ipython -c "from aig2cell import *;dumpscr(\"$faag\", \"$fdro\", L_cnt=$lcnt, Non_dbg=True, levels=$hj)" && echo "DRO: $file"
echo "DRO: $file"
yosys-abc -c "read $fdup; comb -L $lcnt; write $fout"
sed -i -E -e 's/clock,//g' -e 's/input +clock;//g' -e 's/@ +(posedge +clock)//g' $fout
yosys-abc -c "read $fout; read_library builtin.genlib; sop; attach; write $fmap"
sed -i -E -e 's/clock,//g' -e 's/input +clock;//g' -e 's/@ +(posedge +clock)//g' $fmap
yosys-abc -c "dsec $file $fout"
