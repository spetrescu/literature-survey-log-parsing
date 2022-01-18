mkdir res/

for met in MoLFI
do
  # OpenStack HDFS Apache HPC Windows HealthApp Mac Spark
  for dataset in BGL
  do
    for size in 2
    do
      touch "res/${met}_raw_terminal_logs_results.txt"
      #  3 4 5 6 7 8 9 10
      for run in 1 2
      do
          echo echo "Dataset $dataset size $size run no $run\n" >> "res/${met}_raw_terminal_logs_results.txt"
          python "${met}_benchmark.py" $dataset $size >> "res/${met}_raw_terminal_logs_results.txt"
      done
    done
  done
  python accuracy_results.py $met
done
