import os
import csv
import sys

n = len(sys.argv)

print("Running ", sys.argv[0])

print("Arguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")
print()

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
with open(f'{save_path}{METHOD}_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

os.chdir(cwd)
