mkdir res/
sed '/^Processed/d' raw/raw_results.txt > 1.txt
sed '/^Used/d' 1.txt > 2.txt
sed '/^Parsing\ file/d' 2.txt > 3.txt
sed '/^\ \ F/d' 3.txt > 4.txt
sed '/^===\ O/d' 4.txt > 5.txt
sed '/^\ \ \ \ mem/d' 5.txt > 6.txt
sed '/^Traceback/d' 6.txt > 7.txt
sed '/^UnicodeDecodeError/d' 7.txt > 8.txt
sed '/^\ \ \ \ self.d/d' 8.txt > 9.txt
sed '/^\ \ \ \ return/d' 9.txt > 10.txt
sed '/^\ \ \ \ parse/d' 10.txt > 11.txt
sed '/^\ \ \ \ EventId\ =/d' 11.txt > 12.txt
sed '/^===\ E/d' 12.txt > res/res_results.txt

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