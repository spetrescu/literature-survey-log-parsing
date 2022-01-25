import csv
import os

RESULTS_FILE = "res/res_results.txt"

DIR_PATH = "final/"
SCALAB_SAVE_PATH = "final/scalability_res.csv"
METHOD = "AEL"
DATASET = "Thunderbird"

if not os.path.exists(DIR_PATH):
    os.makedirs(DIR_PATH)

row_list = [["method", "dataset", "log_size", "elapsed_time", "peak_memory", "iteration_no"]]
with open(f'{SCALAB_SAVE_PATH}', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

complete_information_about_row = True
method = METHOD

with open(RESULTS_FILE) as file:
    for line in file:
        if "run no" in line and "Dataset" in line and "size" in line:
            complete_information_about_row = False
            dataset = DATASET
            log_size = line.split(" ")[3]
            iteration_no = line.split(" ")[-1]
            iteration_no = iteration_no.rstrip("\n")
        elif "Parsing done." in line and "[Time taken:" in line and not complete_information_about_row:
            line = line.rstrip("\n")
            elapsed_time = line.split("taken: ")[1]
            print(elapsed_time[:-1])
            elapsed_time = elapsed_time[:-1]
            complete_information_about_row = True
        elif "Parsing done." in line and "[Time taken:" in line and complete_information_about_row:
            line = line.rstrip("\n")
            print()
        elif "Precision" in line:
            continue
        elif "Dataset" in line:
            continue
        elif "\n" == line:
            continue
        else:
            if "." in line and "Precision" not in line and f"{DATASET}" not in line:
                line = line.rstrip("\n")
                peak_memory = line
                row_list = [[str(method), str(dataset), str(log_size), str(elapsed_time), str(peak_memory), str(iteration_no)]]
                with open(SCALAB_SAVE_PATH, 'a') as file:
                    writer = csv.writer(file)
                    writer.writerows(row_list)


import csv

ACC_SAVE_PATH = "final/accuracy_res.csv"

row_list = [["method", "dataset", "log_size", "precision", "recall", "F1_measure", "parsing_accuracy", "iteration_no"]]
with open(f'{ACC_SAVE_PATH}', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

with open(RESULTS_FILE) as file:
    for line in file:
        if "run no" in line and "Dataset" in line and "size" in line:
            dataset = DATASET
            log_size = line.split(" ")[3]
            iteration_no = line.split(" ")[-1]
            iteration_no = iteration_no.rstrip("\n")
        elif "Precision:" in line:
            line = line.rstrip("\n")
            data = line.split(",")
            precision = data[0][11:]
            recall = data[1][9:]
            F1_measure = data[2][13:]
            parsing_accuracy = data[3][19:]
            row_list = [
                [str(method), str(dataset), str(log_size), str(precision), str(recall), str(F1_measure), str(parsing_accuracy), str(iteration_no)]]
            with open(ACC_SAVE_PATH, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(row_list)
            print(parsing_accuracy)
        else:
            continue