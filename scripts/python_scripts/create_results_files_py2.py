import os
import csv
import sys

n = len(sys.argv)

METHOD = str(sys.argv[1])
SCALABILITY_EXPERIMENTS_OUTPUT_PATH = str(sys.argv[2])

save_path = SCALABILITY_EXPERIMENTS_OUTPUT_PATH
cwd = os.getcwd()
os.chdir('..')
print(os.getcwd())
os.chdir('demo/')

if not os.path.exists(save_path):
    os.makedirs(save_path)

# method, dataset, current_run, size, elapsed_time, peak_memory
row_list = [["method", "dataset", "log_size", "elapsed_time", "peak_memory", "iteration_no"]]
save_experiments = str(save_path)+str(METHOD)+"_results.csv"
with open(save_experiments, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
os.chdir(cwd)
