file=$1
[ -e "$file" ] && yosys-abc -f abcaig.script -o "${file%.v}.aig" "$file" && echo "AIGed: $file"
aigtoaig "${file%.v}.aig" "${file%.v}.aag"
fin="${file%.v}.aag"
fout="${file%.v}_N.v"
fxs="${file%.v}_XS.v"
command1=`cat <<EOF
from aig2cell import *
dumpscr("$fin", "$fout")
EOF`
python -c "$command1"
# ipython -c "from aig2cell import *;dumpscr(\"$fin\", \"$fout\")"
echo "Split: $file"
command2=`cat <<EOF
from aig2cell import *
dumpscr("$fin", "$fxs", Non_dbg=True)
EOF`
python -c "$command2"
# ipython -c "from aig2cell import *;dumpscr(\"$fin\", \"$fxs\", Non_dbg=True)"
echo "XS: $file"
yosys-abc -c "cec $file $fout"
