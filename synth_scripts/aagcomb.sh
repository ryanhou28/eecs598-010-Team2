file=$1
[ -e "$file" ] && yosys-abc -f abcaig.script -o "${file%.v}.aig" "$file" && echo "AIGed: $file"
aigtoaig "${file%.v}.aig" "${file%.v}.aag"
fin="${file%.v}.aag"
fout="${file%.v}_N.v"
ipython -c "from aig2cell import *;dumpscr(\"$fin\", \"$fout\")" && echo "Split: $file"
yosys-abc -c "cec $file $fout"
