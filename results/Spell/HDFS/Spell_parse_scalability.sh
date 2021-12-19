sed '/^Processed/d' HDFS/raw/raw_Spell_HDFS_scalability_results.txt > HDFS/res/1_res_Spell_HDFS_scalability_results.txt
sed '/^Used/d' HDFS/res/1_res_Spell_HDFS_scalability_results.txt > HDFS/res/2_res_Spell_HDFS_scalability_results.txt
sed '/^Parsing\ file/d' HDFS/res/2_res_Spell_HDFS_scalability_results.txt > HDFS/res/3_res_Spell_HDFS_scalability_results.txt
sed '/^\ \ \ \ \ \ \ \ \ F/d' HDFS/res/3_res_Spell_HDFS_scalability_results.txt > HDFS/res/4_res_Spell_HDFS_scalability_results.txt
sed '/^===\ O/d' HDFS/res/4_res_Spell_HDFS_scalability_results.txt > HDFS/res/5_res_Spell_HDFS_scalability_results.txt
sed '/^===\ E/d' HDFS/res/5_res_Spell_HDFS_scalability_results.txt > HDFS/res/6_res_Spell_HDFS_scalability_results.txt
rm HDFS/res/1_res_Spell_HDFS_scalability_results.txt
rm HDFS/res/2_res_Spell_HDFS_scalability_results.txt
rm HDFS/res/3_res_Spell_HDFS_scalability_results.txt
rm HDFS/res/4_res_Spell_HDFS_scalability_results.txt
rm HDFS/res/5_res_Spell_HDFS_scalability_results.txt
mv HDFS/res/6_res_Spell_HDFS_scalability_results.txt HDFS/res/res_Spell_HDFS_scalability_results.txt
