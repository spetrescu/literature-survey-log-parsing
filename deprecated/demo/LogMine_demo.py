#!/usr/bin/env python

import sys

sys.path.append('../')
from logparser import LogMine
import os
import csv
from memory_profiler import memory_usage
import pandas as pd

n = len(sys.argv)
print("Running ", sys.argv[0])
print("Arguments passed:")
for i in range(1, n):
    print(sys.argv[i])

DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])
RUN_NO = str(sys.argv[3])
METHOD = str(sys.argv[4])
SCALABILITY_EXPERIMENTS_OUTPUT_PATH = str(sys.argv[5])
input_scalability_experiments = '../data/scalability/'
input_accuracy_experiments = ''
output_scalability_results_file = SCALABILITY_EXPERIMENTS_OUTPUT_PATH
input_dir = input_scalability_experiments
LOG_FILE = str(DATASET) + "_" + str(SIZE) + "k.log"
output_dir = str(METHOD) + "_result/"  # The output directory of parsing results
indir = os.path.join(input_dir, DATASET)
log_file = LOG_FILE

benchmark_settings = {
    'HDFS': {
        'log_file': 'HDFS/HDFS_2k.log',
        'log_format': '<Date> <Time> <Pid> <Level> <Component>: <Content>',
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'],
        'max_dist': 0.005,
        'k': 1,
        'levels': 2
        },

    'Hadoop': {
        'log_file': 'Hadoop/Hadoop_2k.log',
        'log_format': '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'max_dist': 0.005,
        'k': 1,
        'levels': 2
        },

    'Spark': {
        'log_file': 'Spark/Spark_2k.log',
        'log_format': '<Date> <Time> <Level> <Component>: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+'],
        'max_dist': 0.01,
        'k': 1,
        'levels': 2
        },

    'Zookeeper': {
        'log_file': 'Zookeeper/Zookeeper_2k.log',
        'log_format': '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>',
        'regex': [r'(/|)(\d+\.){3}\d+(:\d+)?'],
        'max_dist': 0.001,
        'k': 1,
        'levels': 2
        },

    'BGL': {
        'log_file': 'BGL/BGL_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
        'regex': [r'core\.\d+'],
        'max_dist': 0.01,
        'k': 2,
        'levels': 2
        },

    'HPC': {
        'log_file': 'HPC/HPC_2k.log',
        'log_format': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>',
        'regex': [r'=\d+'],
        'max_dist': 0.0001,
        'k': 0.8,
        'levels': 2
        },

    'Thunderbird': {
        'log_file': 'Thunderbird/Thunderbird_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'max_dist': 0.005,
        'k': 1,
        'levels': 2
        },

    'Windows': {
        'log_file': 'Windows/Windows_2k.log',
        'log_format': '<Date> <Time>, <Level>                  <Component>    <Content>',
        'regex': [r'0x.*?\s'],
        'max_dist': 0.003,
        'k': 1,
        'levels': 2
        },

    'Linux': {
        'log_file': 'Linux/Linux_2k.log',
        'log_format': '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}'],
        'max_dist': 0.006,
        'k': 1,
        'levels': 2
        },

    'Android': {
        'log_file': 'Andriod/Andriod_2k.log',
        'log_format': '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>',
        'regex': [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b'],
        'max_dist': 0.01,
        'k': 1     ,
        'levels': 2
        },

    'HealthApp': {
        'log_file': 'HealthApp/HealthApp_2k.log',
        'log_format': '<Time>\|<Component>\|<Pid>\|<Content>',
        'regex': [],
        'max_dist': 0.008,
        'k': 1,
        'levels': 2
        },

    'Apache': {
        'log_file': 'Apache/Apache_2k.log',
        'log_format': '\[<Time>\] \[<Level>\] <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'max_dist': 0.005,
        'k': 1,
        'levels': 2
        },

    'Proxifier': {
        'log_file': 'Proxifier/Proxifier_2k.log',
        'log_format': '\[<Time>\] <Program> - <Content>',
        'regex': [r'<\d+\ssec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B'],
        'max_dist': 0.002,
        'k': 1,
        'levels': 2
        },

    'OpenSSH': {
        'log_file': 'OpenSSH/OpenSSH_2k.log',
        'log_format': '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+'],
        'max_dist': 0.001,
        'k': 1,
        'levels': 2
        },

    'OpenStack': {
        'log_file': 'OpenStack/OpenStack_2k.log',
        'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
        'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+'],
        'max_dist': 0.001,
        'k': 0.1,
        'levels': 2
        },

    'Mac': {
        'log_file': 'Mac/Mac_2k.log',
        'log_format': '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>',
        'regex': [r'([\w-]+\.){2,}[\w-]+'],
        'max_dist': 0.004,
        'k': 1,
        'levels': 2
        },
}

def parsing_logs(setting, indir, output_dir, log_file):
    setting = setting
    parser = LogMine.LogParser(log_format=setting['log_format'], indir=indir, outdir=output_dir,
                               rex=setting['regex'], max_dist=setting['max_dist'], k=setting['k'],
                               levels=setting['levels'])
    time_taken = parser.parse(log_file)

    row_list = [[str(METHOD), str(DATASET), str(SIZE), str(time_taken), str(0), str(RUN_NO)]]
    with open(output_scalability_results_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
    return


for dataset, setting in benchmark_settings.iteritems():
    if DATASET == dataset:
        print('\n=== Evaluation on %s ===' % dataset)
        setting_dataset = setting
        mem = max(memory_usage((parsing_logs, (setting, indir, output_dir, log_file))))
        print('Peak memory: {!s}'.format(mem))
        df = pd.read_csv(output_scalability_results_file)

        ##method,dataset,log_size,elapsed_time,peak_memory,iteration_no
        print(df.iloc[-1]['elapsed_time'])
        met = df.iloc[-1]['method']
        ds = df.iloc[-1]['dataset']
        ls = df.iloc[-1]['log_size']
        et = df.iloc[-1]['elapsed_time']
        pm = df.iloc[-1]['peak_memory']
        itno = df.iloc[-1]['iteration_no']
        df.loc[df.shape[0] - 1, ['method', 'dataset', 'log_size', 'elapsed_time', 'peak_memory', 'iteration_no']] = [
            met, ds, ls, et, mem, itno]
        df.to_csv(output_scalability_results_file, index=False)
