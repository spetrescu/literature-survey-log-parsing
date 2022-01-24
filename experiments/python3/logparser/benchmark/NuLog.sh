for d in OpenStack
do
  for s in 2
  do
    for r in 1
    do
        python NuLog_benchmark.py $d $s $r
        echo "Dataset $d size $s run no $r"
        mv "NuLog_result/${d}_2k.log_structured.csv" "NuLog_result/${d}_2k.log_structured_run_${r}.csv"
    done
  done
done


#for s in 1
#do
#  for r in 1
#  do
#      python NuLog_benchmark.py OpenSSH $s
#  done
#done
#
#for s in 1
#do
#  for r in 1
#  do
#      python NuLog_benchmark.py BGL $s
#  done
#done

#for d in Andriod HDFS Thunderbird Windows
#do
#  for s in 1 2 4 10 20 50 100 200 300 500 1000
#  do
#    for r in 1 2 3 4 5 6 7 8 9 10
#    do
#        python MoLFI_benchmark.py $d $s
#    done
#  done
#done
#
#
#for s in 1 2 4 20 50 100 200 300 500
#do
#  for r in 1 2 3 4 5 6 7 8 9 10
#  do
#      python MoLFI_benchmark.py OpenSSH $s
#  done
#done
#
#for s in 1 2 4 20 50 100 200 300
#do
#  for r in 1 2 3 4 5 6 7 8 9 10
#  do
#      python MoLFI_benchmark.py BGL $s
#  done
#done