#!/bin/bash

usage="$(basename "$0") [-h] [-d dataset] -- augment data for specific dataset

where:
    -h  show instructions to run the script
    -d  set the dataset (default: HDFS)"

dataset="HDFS"
while getopts ':hd:' option; do
  case "$option" in
    h) echo "$usage"
       exit
       ;;
    d) if [ "$OPTARG" != "Android" ] && [ "$OPTARG" != "Apache" ] && [ "$OPTARG" != "BGL" ] && [ "$OPTARG" != "Hadoop" ] && [ "$OPTARG" != "HDFS" ] && [ "$OPTARG" != "HealthApp" ] && [ "$OPTARG" != "HPC" ] && [ "$OPTARG" != "Linux" ] && [ "$OPTARG" != "Mac" ] && [ "$OPTARG" != "OpenSSH" ] && [ "$OPTARG" != "OpenStack" ] && [ "$OPTARG" != "Proxifier" ] && [ "$OPTARG" != "Spark" ] && [ "$OPTARG" != "Thunderbird" ] && [ "$OPTARG" != "Windows" ] && [ "$OPTARG" != "Zookeeper" ] ; then
        printf "The argument \"$OPTARG\" is invalid. Please change it to a dataset present in the list.\n\nAllowed datasets: \n Android\n Apache\n BGL\n Hadoop\n HDFS\n HealthApp\n HPC\n Linux\n Mac\n OpenSSH\n OpenStack\n Proxifier\n Spark\n Thunderbird\n Windows\n Zookeeper\n"
        exit
       fi
       dataset=$OPTARG
       ;;
    :) printf "missing argument for -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
   \?) printf "illegal option: -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
shift $((OPTIND - 1))

python python_scripts/augment_data.py 0 $dataset #2k logs
python python_scripts/augment_data.py 1 $dataset #4k logs
python python_scripts/augment_data.py 4 $dataset #10k logs
python python_scripts/augment_data.py 9 $dataset #20k logs
python python_scripts/augment_data.py 24 $dataset #50k logs
python python_scripts/augment_data.py 49 $dataset #100k logs
python python_scripts/augment_data.py 99 $dataset #200k logs
python python_scripts/augment_data.py 149 $dataset #300k logs

echo "Finished data augmentation for $dataset!"