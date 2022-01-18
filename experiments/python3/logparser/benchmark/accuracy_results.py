import csv
import sys

n = len(sys.argv)
METHOD = str(sys.argv[1])
RESULTS_FILE = f"res/{METHOD}_raw_terminal_logs_results.txt"

DIR_PATH = "final/"
SAVE_PATH = f"final/accuracy_res_{METHOD}.csv"
method = METHOD

row_list = [["method", "dataset", "log_size", "precision", "recall", "F1_measure", "parsing_accuracy", "iteration_no"]]
with open(f'{SAVE_PATH}', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

with open(RESULTS_FILE) as file:
    for line in file:
        if "run no" in line and "Dataset" in line and "size" in line:
            log_size = line.split(" ")[3]
            dataset = line.split(" ")[1]
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
            with open(SAVE_PATH, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(row_list)
            print(parsing_accuracy)
        else:
            continue
