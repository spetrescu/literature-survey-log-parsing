sed '/^Processed/d' raw/raw_Spell_Thunderbird_accuracy_results.txt > 1.txt
sed '/^Used/d' 1.txt > 2.txt
sed '/^Parsing\ file/d' 2.txt > 3.txt
sed '/^\ \ \ \ \ \ \ \ \ F/d' 3.txt > 4.txt
sed '/^===\ O/d' 4.txt > 5.txt
sed '/^\ \ \ \ \ \ \ \ \ \ \ \ \ F/d' 5.txt > 6.txt
sed '/^===\ E/d' 6.txt > res/res_accuracy_results.txt

rm 1.txt
rm 2.txt
rm 3.txt
rm 4.txt
rm 5.txt
rm 6.txt

