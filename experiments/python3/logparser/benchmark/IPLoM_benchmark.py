#!/usr/bin/env python

import sys
sys.path.append('../')
from logparser import IPLoM, evaluator
import os
import pandas as pd


input_dir = '../logs/'  # The input directory of log file
output_dir = 'IPLoM_result/'  # The output directory of parsing results

benchmark_settings = {
    'HDFS': {
        'log_file': 'HDFS/HDFS_2k.log',
        'log_format': '<Date> <Time> <Pid> <Level> <Component>: <Content>',
        'CT': 0.35,
        'lowerBound': 0.25,
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?']
        },

    'Hadoop': {
        'log_file': 'Hadoop/Hadoop_2k.log',
        'log_format': '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>', 
        'CT': 0.4,
        'lowerBound': 0.2,
        'regex': [r'(\d+\.){3}\d+']
        },

    'Spark': {
        'log_file': 'Spark/Spark_2k.log',
        'log_format': '<Date> <Time> <Level> <Component>: <Content>', 
        'CT': 0.35,
        'lowerBound': 0.3,
        'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+']
        },

    'Zookeeper': {
        'log_file': 'Zookeeper/Zookeeper_2k.log',
        'log_format': '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>',
        'CT': 0.4,
        'lowerBound': 0.7,
        'regex': [r'(/|)(\d+\.){3}\d+(:\d+)?']
        },

    'BGL': {
        'log_file': 'BGL/BGL_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
        'CT': 0.4,
        'lowerBound': 0.01,
        'regex': [r'core\.\d+']
        },

    'HPC': {
        'log_file': 'HPC/HPC_2k.log',
        'log_format': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>',
        'CT': 0.58,
        'lowerBound': 0.25,
        'regex': [r'=\d+']
        },

    'Thunderbird': {
        'log_file': 'Thunderbird/Thunderbird_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>',
        'CT': 0.3,
        'lowerBound': 0.2,
        'regex': [r'(\d+\.){3}\d+']
        },

    'Windows': {
        'log_file': 'Windows/Windows_2k.log',
        'log_format': '<Date> <Time>, <Level>                  <Component>    <Content>',
        'CT': 0.3,
        'lowerBound': 0.25,
        'regex': [r'0x.*?\s']
        },

    'Linux': {
        'log_file': 'Linux/Linux_2k.log',
        'log_format': '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>',
        'CT': 0.3,
        'lowerBound': 0.3,
        'regex': [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}']
        },

    'Andriod': {
        'log_file': 'Andriod/Andriod_2k.log',
        'log_format': '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>',
        'CT': 0.25,
        'lowerBound': 0.3,
        'regex': [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b']
        },

    'HealthApp': {
        'log_file': 'HealthApp/HealthApp_2k.log',
        'log_format': '<Time>\|<Component>\|<Pid>\|<Content>',
        'CT': 0.25,
        'lowerBound': 0.3,
        'regex': []
        },

    'Apache': {
        'log_file': 'Apache/Apache_2k.log',
        'log_format': '\[<Time>\] \[<Level>\] <Content>',
        'CT': 0.3,
        'lowerBound': 0.4,
        'regex': [r'(\d+\.){3}\d+']
        },

    'Proxifier': {
        'log_file': 'Proxifier/Proxifier_2k.log',
        'log_format': '\[<Time>\] <Program> - <Content>',
        'CT': 0.9,
        'lowerBound': 0.25,
        'regex': [r'<\d+\ssec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B'],
        },

    'OpenSSH': {
        'log_file': 'OpenSSH/OpenSSH_2k.log',
        'log_format': '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>',
        'CT': 0.78,
        'lowerBound': 0.25,
        'regex': [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+']
        },

    'OpenStack': {
        'log_file': 'OpenStack/OpenStack_2k.log',
        'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
        'CT': 0.9,
        'lowerBound': 0.25,
        'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+']
    },

    'Mac': {
        'log_file': 'Mac/Mac_2k.log',
        'log_format': '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>',
        'CT': 0.3,
        'lowerBound': 0.25,
        'regex': [r'([\w-]+\.){2,}[\w-]+']
        }
}

bechmark_result = []
for dataset, setting in benchmark_settings.iteritems():
    print('\n=== Evaluation on %s ==='%dataset)
    indir = os.path.join(input_dir, os.path.dirname(setting['log_file']))
    log_file = os.path.basename(setting['log_file'])

    parser = IPLoM.LogParser(log_format=setting['log_format'], indir=indir, outdir=output_dir,
                             CT=setting['CT'], lowerBound=setting['lowerBound'], rex=setting['regex'])
    parser.parse(log_file)
    
    F1_measure, accuracy = evaluator.evaluate(
                           groundtruth=os.path.join(indir, log_file + '_structured.csv'),
                           parsedresult=os.path.join(output_dir, log_file + '_structured.csv')
                           )
    bechmark_result.append([dataset, F1_measure, accuracy])


print('\n=== Overall evaluation results ===')
df_result = pd.DataFrame(bechmark_result, columns=['Dataset', 'F1_measure', 'Accuracy'])
df_result.set_index('Dataset', inplace=True)
print(df_result)
df_result.T.to_csv('IPLoM_bechmark_result.csv')
