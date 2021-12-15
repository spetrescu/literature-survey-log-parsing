import sys
sys.path.append('../')
from logparser import AEL, evaluator
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

benchmark_settings = {
    'HDFS': {
        'log_file': 'HDFS/HDFS_2k.log',
        'log_format': '<Date> <Time> <Pid> <Level> <Component>: <Content>',
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'],
        'minEventCount': 2,
        'merge_percent' : 0.5
        },

    'Hadoop': {
        'log_file': 'Hadoop/Hadoop_2k.log',
        'log_format': '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>', 
        'regex': [r'(\d+\.){3}\d+'],
        'minEventCount': 2,
        'merge_percent' : 0.4
        },

    'Spark': {
        'log_file': 'Spark/Spark_2k.log',
        'log_format': '<Date> <Time> <Level> <Component>: <Content>', 
        'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+'],
        'minEventCount': 2,
        'merge_percent' : 0.4
        },

    'Zookeeper': {
        'log_file': 'Zookeeper/Zookeeper_2k.log',
        'log_format': '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>',
        'regex': [r'(/|)(\d+\.){3}\d+(:\d+)?'],
        'minEventCount': 2,
        'merge_percent' : 0.4
        },

    'BGL': {
        'log_file': 'BGL/BGL_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
        'regex': [r'core\.\d+'],
        'minEventCount': 2,
        'merge_percent' : 0.5
        },

    'HPC': {
        'log_file': 'HPC/HPC_2k.log',
        'log_format': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>',
        'regex': [r'=\d+'],
        'minEventCount': 5,
        'merge_percent' : 0.4
        },

    'Thunderbird': {
        'log_file': 'Thunderbird/Thunderbird_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'minEventCount': 2,
        'merge_percent' : 0.4
        },

    'Windows': {
        'log_file': 'Windows/Windows_2k.log',
        'log_format': '<Date> <Time>, <Level>                  <Component>    <Content>',
        'regex': [r'0x.*?\s'],
        'minEventCount': 2,
        'merge_percent' : 0.4
        },

    'Linux': {
        'log_file': 'Linux/Linux_2k.log',
        'log_format': '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}'],
        'minEventCount': 2,
        'merge_percent' : 0.6
        },

    'Andriod': {
        'log_file': 'Andriod/Andriod_2k.log',
        'log_format': '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>',
        'regex': [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b'],
        'minEventCount': 2,
        'merge_percent' : 0.6
        },

    'HealthApp': {
        'log_file': 'HealthApp/HealthApp_2k.log',
        'log_format': '<Time>\|<Component>\|<Pid>\|<Content>',
        'regex': [],
        'minEventCount': 2,
        'merge_percent' : 0.6
        },

    'Apache': {
        'log_file': 'Apache/Apache_2k.log',
        'log_format': '\[<Time>\] \[<Level>\] <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'minEventCount': 2,
        'merge_percent' : 0.4
        },

    'Proxifier': {
        'log_file': 'Proxifier/Proxifier_2k.log',
        'log_format': '\[<Time>\] <Program> - <Content>',
        'regex': [r'<\d+\s?sec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B'],
        'minEventCount': 2,
        'merge_percent' : 0.4
        },

    'OpenSSH': {
        'log_file': 'OpenSSH/OpenSSH_2k.log',
        'log_format': '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+'],
        'minEventCount': 10,
        'merge_percent' : 0.7
        },

    'OpenStack': {
        'log_file': 'OpenStack/OpenStack_2k.log',
        'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
        'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+'],
        'minEventCount': 6,
        'merge_percent' : 0.5
        },

    'Mac': {
        'log_file': 'Mac/Mac_2k.log',
        'log_format': '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>',
        'regex': [r'([\w-]+\.){2,}[\w-]+'],
        'minEventCount': 2,
        'merge_percent' : 0.6
        }
}

input_dir  = '../data/augmented_data/'
LOG_FILE = f"{DATASET}_augmented_{SIZE}k.log"
LOG_FILE = "AEL_augmented_2k.log"
output_dir = f'{METHOD}_result/'  # The output directory of parsing results
output_dir = 'AEL_result/'

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
        parser = AEL.LogParser(log_format=setting['log_format'], indir=indir, outdir=output_dir,
                               minEventCount=setting['minEventCount'], merge_percent=setting['merge_percent'],
                               rex=setting['regex'])
        time_taken = parser.parse(log_file)
        current, peak = tracemalloc.get_traced_memory()
        peak_mb = peak / 10 ** 6
        print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak_mb}MB")
        tracemalloc.stop()

        row_list = [[f"{METHOD}", f"{DATASET}", f"{SIZE}", f"{time_taken}", f"{peak / 10 ** 6}",  f"{RUN_NO}"]]
        with open(f'{METHOD}_results/{DATASET}/{METHOD}_{DATASET}_results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)