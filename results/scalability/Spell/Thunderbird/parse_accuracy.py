import csv

ACCURACY_RESULTS_FILE_PATH = "res/res_accuracy_results.txt"

RESULTS_PATH = "res/final_accuracy_results.csv"
METHOD = "Spell"

row_list = [["method", "dataset", "log_size", "precision", "recall", "F1_measure", "parsing_accuracy", "iteration_no"]]
with open(f'{RESULTS_PATH}', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

complete_information_about_row = True
method = METHOD

with open(ACCURACY_RESULTS_FILE_PATH) as file:
    for line in file:
        if "run no" in line and "Dataset" in line and "size" in line:
            dataset = line.split(" ")[1]
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
            with open(RESULTS_PATH, 'a') as file:
                writer = csv.writer(file)
                writer.writerows(row_list)
            print(parsing_accuracy)
        else:
            continue