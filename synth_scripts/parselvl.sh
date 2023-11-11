file=$1
yosys-abc -c "print_io;print_supp -w" $file > tmprs.txt
sed -n 's/.*\(([0-9]*)\).*/\1/p' tmprs.txt > iol.txt
sed -n '/^[01]\+$/p' tmprs.txt > bin.txt
hj=$(ipython parselvl.py)
rm tmprs.txt
rm iol.txt
rm bin.txt
echo "$hj"
