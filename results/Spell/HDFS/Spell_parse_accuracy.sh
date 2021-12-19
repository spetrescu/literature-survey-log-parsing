sed '/^Processed/d' raw/raw_Spell_HDFS_accuracy_results.txt > res/1_res_Spell_HDFS_accuracy_results.txt
sed '/^Used/d' res/1_res_Spell_HDFS_accuracy_results.txt > res/2_res_Spell_HDFS_accuracy_results.txt
sed '/^Parsing\ file/d' res/2_res_Spell_HDFS_accuracy_results.txt > res/3_res_Spell_HDFS_accuracy_results.txt
sed '/^===\ E/d' res/3_res_Spell_HDFS_accuracy_results.txt > res/4_res_Spell_HDFS_accuracy_results.txt
sed '/^===\ O/d' res/4_res_Spell_HDFS_accuracy_results.txt > res/5_res_Spell_HDFS_accuracy_results.txt
sed '/^\ \ \ \ \ \ \ \ \ F/d' res/5_res_Spell_HDFS_accuracy_results.txt > res/6_res_Spell_HDFS_accuracy_results.txt
sed '/^Parsing\ done/d' res/6_res_Spell_HDFS_accuracy_results.txt > res/7_res_Spell_HDFS_accuracy_results.txt
rm res/1_res_Spell_HDFS_accuracy_results.txt
rm res/2_res_Spell_HDFS_accuracy_results.txt
rm res/3_res_Spell_HDFS_accuracy_results.txt
rm res/4_res_Spell_HDFS_accuracy_results.txt
rm res/5_res_Spell_HDFS_accuracy_results.txt
rm res/6_res_Spell_HDFS_accuracy_results.txt
mv res/7_res_Spell_HDFS_accuracy_results.txt res/res_Spell_HDFS_accuracy_results.txt