mkdir res/

for met in AEL
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
          echo "$met run no. $run dataset $dataset"
          echo "Dataset $dataset size $size run no $run" >> "res/${met}_raw_terminal_logs_results.txt"
          python "${met}_benchmark.py" $dataset $size >> "res/${met}_raw_terminal_logs_results.txt"
      done
    done
  done
  python accuracy_results.py $met
done
