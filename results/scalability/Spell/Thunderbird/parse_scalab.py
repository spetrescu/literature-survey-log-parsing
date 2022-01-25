import csv

SCALABILITY_RESULTS_FILE_PATH = "res/res_scalability_results.txt"

RESULTS_PATH = "res/final_scalability_results.csv"
METHOD = "Spell"

row_list = [["method", "dataset", "log_size", "elapsed_time", "peak_memory", "iteration_no"]]
with open(f'{RESULTS_PATH}', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

complete_information_about_row = True
method = METHOD

with open(SCALABILITY_RESULTS_FILE_PATH) as file:
    for line in file:
        if "run no" in line and "Dataset" in line and "size" in line:
            complete_information_about_row = False
            dataset = line.split(" ")[1]
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
            if "." in line and "Precision" not in line and "Thunderbird" not in line:
                line = line.rstrip("\n")
                peak_memory = line
                row_list = [[str(method), str(dataset), str(log_size), str(elapsed_time), str(peak_memory), str(iteration_no)]]
                with open(RESULTS_PATH, 'a') as file:
                    writer = csv.writer(file)
                    writer.writerows(row_list)
