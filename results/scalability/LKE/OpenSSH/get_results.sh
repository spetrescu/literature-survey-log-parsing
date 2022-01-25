mkdir res/
sed '/^the/d' raw/raw_results.txt > 1.txt
sed '/^===\ S/d' 1.txt > 2.txt
sed '/^splitting/d' 2.txt > 3.txt
sed '/^Loading\ log\ messages\ to/d' 3.txt > 4.txt
sed '/^Run/d' 4.txt > 5.txt
sed '/^Worker/d' 5.txt > 6.txt
sed '/^===\ E/d' 6.txt > 7.txt
sed '/^kMeans/d' 7.txt > 8.txt
sed '/^Used/d' 8.txt > 9.txt
sed '/^Parsing\ file:/d' 9.txt > 10.txt
sed '/^Merge/d' 10.txt > 11.txt
sed '/^Loading/d' 11.txt > 12.txt
sed '/^calcula/d' 12.txt > res/res_results.txt


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