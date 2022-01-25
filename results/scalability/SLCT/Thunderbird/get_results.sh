mkdir res/
sed '/^Sun\ Dec/d' raw/raw_results.txt > 1.txt
sed '/^Compile\ SLCT/d' 1.txt > 2.txt
sed '/^Dumping\ event/d' 2.txt > 3.txt
sed '/^Loading\ log\ messages\ to/d' 3.txt > 4.txt
sed '/^Matching/d' 4.txt > 5.txt
sed '/^Worker/d' 5.txt > 6.txt
sed '/^===\ E/d' 6.txt > 7.txt
sed '/^>>\ gcc\ -o/d' 7.txt > 8.txt
sed '/^Run\ SLCT/d' 8.txt > 9.txt
sed '/^Parsing\ file:/d' 9.txt > 10.txt
sed '/^Processing\ log\ file:/d' 10.txt > 11.txt
sed '/^Loading/d' 11.txt > 12.txt
sed '/^\>/d' 12.txt > res/res_results.txt

rm 1.txt
rm 2.txt
rm 3.txt
rm 4.txt
rm 5.txt
rm 6.txt
rm 7.txt
rm 8.txt
rm 9.txt
rm 10.txt
rm 11.txt
rm 12.txt

python generate_final_results.py