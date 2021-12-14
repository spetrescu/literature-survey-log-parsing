# #!/usr/bin/env python
# import sys
# sys.path.append('../')
# from logparser import Drain
# import tracemalloc
#
# input_dir  = ['../experiment_data/Android/', '../experiment_data/Apache/']  # The input directory of log file
# output_dir = ['Android_result/', 'Apache_result/']  # The output directory of parsing results
# log_file   = ['Andriod_2k.log', 'Andriod_2k.log', 'Andriod_2k.log', 'Andriod_2k.log', 'Andriod_2k.log']  # The input log file name
# log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
# # Regular expression list for optional preprocessing (default: [])
# regex      = [
#     r'blk_(|-)[0-9]+' , # block id
#     r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
#     r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
# ]
# st         = 0.5  # Similarity threshold
# depth      = 4  # Depth of all leaf nodes
#
# for inp_dir, out_dir in zip(input_dir, output_dir):
#     print("inp_dir", inp_dir)
#     print("out_dir", out_dir)
#     for file in log_file:
#         print("file", file)
#         tracemalloc.start()
#         parser = Drain.LogParser(log_format, indir=dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
#         parser.parse(str(file))
#         current, peak = tracemalloc.get_traced_memory()
#         print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
#         tracemalloc.stop()
#         print("")
#
#
#!/usr/bin/env python


# import sys
# sys.path.append('../')
# from logparser import Drain
# import tracemalloc
#
# log_dataset = ['Android', 'Apache', 'HDFS']
#
# input_dir  = ['../data/initial_data/Android/', '../data/initial_data/Apache/', '../data/initial_data/HDFS/']  # The input directory of log file
# output_dir = 'Drain_result/'  # The output directory of parsing results
# log_file   = ['_2k.log', '_2k.log', '_2k.log', '_2k.log', '_2k.log', '_2k.log', '_2k.log', '_2k.log', '_2k.log', '_2k.log']  # The input log file name
# log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
# # Regular expression list for optional preprocessing (default: [])
# regex      = [
#     r'blk_(|-)[0-9]+' , # block id
#     r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
#     r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
# ]
# st         = 0.5  # Similarity threshold
# depth      = 4  # Depth of all leaf nodes

# for inp_dir, dtset in zip(input_dir, log_dataset):
#     for fi in log_file:
#         tracemalloc.start()
#         parser = Drain.LogParser(log_format, indir=inp_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
#         parser.parse(f"{dtset}{fi}")
#         current, peak = tracemalloc.get_traced_memory()
#         print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
#         tracemalloc.stop()
#         print("")

# # !/usr/bin/env python
#
#


# #python3.7 {method}_demo.py [dataset] [size]
#
#
#
#
#
#
import sys
sys.path.append('../')
from logparser import Drain, evaluator
import os
import tracemalloc
import csv

n = len(sys.argv)
print("Running ", sys.argv[0])
print("Arguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")
print()
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])
RUN_NO = str(sys.argv[3])
METHOD = str(sys.argv[4])
#AUGMENT_TIMES = int(sys.argv[1])


benchmark_settings = {
    'HDFS': {
        'log_file': 'HDFS/HDFS_augmented_2k.log',
        'log_format': '<Date> <Time> <Pid> <Level> <Component>: <Content>',
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'],
        'st': 0.5,
        'depth': 4
    },

    'Hadoop': {
        'log_file': 'Hadoop/Hadoop_2k.log',
        'log_format': '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'st': 0.5,
        'depth': 4
    },

    'Spark': {
        'log_file': 'Spark/Spark_2k.log',
        'log_format': '<Date> <Time> <Level> <Component>: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+'],
        'st': 0.5,
        'depth': 4
    },

    'Zookeeper': {
        'log_file': 'Zookeeper/Zookeeper_2k.log',
        'log_format': '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>',
        'regex': [r'(/|)(\d+\.){3}\d+(:\d+)?'],
        'st': 0.5,
        'depth': 4
    },

    'BGL': {
        'log_file': 'BGL/BGL_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
        'regex': [r'core\.\d+'],
        'st': 0.5,
        'depth': 4
    },

    'HPC': {
        'log_file': 'HPC/HPC_2k.log',
        'log_format': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>',
        'regex': [r'=\d+'],
        'st': 0.5,
        'depth': 4
    },

    'Thunderbird': {
        'log_file': 'Thunderbird/Thunderbird_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'st': 0.5,
        'depth': 4
    },

    'Windows': {
        'log_file': 'Windows/Windows_2k.log',
        'log_format': '<Date> <Time>, <Level>                  <Component>    <Content>',
        'regex': [r'0x.*?\s'],
        'st': 0.7,
        'depth': 5
    },

    'Linux': {
        'log_file': 'Linux/Linux_2k.log',
        'log_format': '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}'],
        'st': 0.39,
        'depth': 6
    },

    'Andriod': {
        'log_file': 'Andriod/Andriod_2k.log',
        'log_format': '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>',
        'regex': [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b'],
        'st': 0.2,
        'depth': 6
    },

    'HealthApp': {
        'log_file': 'HealthApp/HealthApp_2k.log',
        'log_format': '<Time>\|<Component>\|<Pid>\|<Content>',
        'regex': [],
        'st': 0.2,
        'depth': 4
    },

    'Apache': {
        'log_file': 'Apache/Apache_2k.log',
        'log_format': '\[<Time>\] \[<Level>\] <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'st': 0.5,
        'depth': 4
    },

    'Proxifier': {
        'log_file': 'Proxifier/Proxifier_2k.log',
        'log_format': '\[<Time>\] <Program> - <Content>',
        'regex': [r'<\d+\ssec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B'],
        'st': 0.6,
        'depth': 3
    },

    'OpenSSH': {
        'log_file': 'OpenSSH/OpenSSH_2k.log',
        'log_format': '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+'],
        'st': 0.6,
        'depth': 5
    },

    'OpenStack': {
        'log_file': 'OpenStack/OpenStack_2k.log',
        'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
        'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+'],
        'st': 0.5,
        'depth': 5
    },

    'Mac': {
        'log_file': 'Mac/Mac_2k.log',
        'log_format': '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>',
        'regex': [r'([\w-]+\.){2,}[\w-]+'],
        'st': 0.7,
        'depth': 6
    },
}
#
input_dir  = '../data/augmented_data/'
LOG_FILE = f"{DATASET}_augmented_{SIZE}k.log"
output_dir = f'{METHOD}_result/'  # The output directory of parsing results

for dataset, setting in benchmark_settings.items():
    if DATASET == dataset:
        print('\n=== Evaluation on %s ===' % dataset)
        #indir = os.path.join(input_dir, log_file)
        indir = os.path.join(input_dir, DATASET)
        #indir = os.path.join(input_dir, os.path.dirname(setting['log_file']))
        #print("os.path.dirname(setting['log_file'])", os.path.dirname(setting['log_file']))
        #print("indir", indir)
        #log_file = os.path.basename(setting['log_file'])
        log_file = LOG_FILE
        print("log_file", log_file)

        tracemalloc.start()
        parser = Drain.LogParser(log_format=setting['log_format'], indir=indir, outdir=output_dir, rex=setting['regex'],
                                 depth=setting['depth'], st=setting['st'])
        time_taken = parser.parse(log_file)
        current, peak = tracemalloc.get_traced_memory()
        peak_mb = peak / 10 ** 6
        print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak_mb}MB")
        tracemalloc.stop()

        row_list = [[f"{METHOD}", f"{DATASET}", f"{SIZE}", f"{time_taken}", f"{peak / 10 ** 6}",  f"{RUN_NO}"]]
        with open(f'{METHOD}_results/{DATASET}/{METHOD}_{DATASET}_results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)

# have access to vim
# ModuleNotFoundError: No module named 'regex'