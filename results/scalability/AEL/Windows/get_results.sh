mkdir res/

sed '/^===\ E/d' raw/raw_results.txt > 1.txt
sed '/^===\ O/d' 1.txt > 2.txt
sed '/^Parsing\ file:/d' 2.txt > 3.txt
sed '/^Processing\ log\ file:/d' 3.txt > 4.txt
sed '/^\ \ \ \ \ \ \ \ \ F/d' 4.txt > 5.txt
sed '/^\ \ \ \ \ \ \ \ \ \ \ \ \ F/d' 5.txt > res/res_results.txt
#sed '/^===\ E/d' 6.txt > res/res_results.txt

rm 1.txt
rm 2.txt
rm 3.txt
rm 4.txt
rm 5.txt

python generate_final_results.py