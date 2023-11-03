rm c85_m/*
for file in c85/*.v; do
    [ -e "$file" ] && yosys-abc -f ab2.script -o "${file%.v}_m.v" "$file" && echo "Processed: $file"
    mv c85/*_m.v c85_m/
done
for file in c85_m/*.v; do
  [ -e "$file" ] && ipython -c "from whatsplit import *;split_from_file(\"$file\")" && echo "Split: $file"
done
