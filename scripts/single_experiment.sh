#!/bin/bash

usage="$(basename "$0") [-h] [-m method] [-d dataset] -- run single experiment using specific method & specific dataset

where:
    -h  show instructions to run the script
    -m  set the method (default: Drain)
    -d  set the dataset (default: HDFS)

allowed methods:
 AEL
 Drain
 IPLoM
 LenMa
 LFA
 LKE
 LogCluster
 logmatch
 LogMine
 LogSig
 MoLFI
 SHISO
 SLCT
 Spell

allowed datasets:
 Android
 Apache
 BGL
 Hadoop
 HDFS
 HealthApp
 HPC
 Linux
 Mac
 OpenSSH
 OpenStack
 Proxifier
 Spark
 Thunderbird
 Windows
 Zookeeper"


method="Drain"
dataset="HDFS"
while getopts ':h:m:d:' option; do
  case "$option" in
    h) echo "$usage"
       exit
       ;;
    m) if [ "$OPTARG" != "AEL" ] && [ "$OPTARG" != "Drain" ] ; then
       #if [ "$OPTARG" != "Android" ] && [ "$OPTARG" != "Apache" ] && [ "$OPTARG" != "BGL" ] && [ "$OPTARG" != "Hadoop" ] && [ "$OPTARG" != "HDFS" ] && [ "$OPTARG" != "HealthApp" ] && [ "$OPTARG" != "HPC" ] && [ "$OPTARG" != "Linux" ] && [ "$OPTARG" != "Mac" ] && [ "$OPTARG" != "OpenSSH" ] && [ "$OPTARG" != "OpenStack" ] && [ "$OPTARG" != "Proxifier" ] && [ "$OPTARG" != "Spark" ] && [ "$OPTARG" != "Thunderbird" ] && [ "$OPTARG" != "Windows" ] && [ "$OPTARG" != "Zookeeper" ] ; then
        printf "The argument \"$OPTARG\" is invalid. Please change it to a method present in the list.\n\nAllowed methods: \n AEL\n Drain\n IPLoM\n LenMa\n LFA\n LKE\n LogCluster\n logmatch\n LogMine\n LogSig\n MoLFI\n SHISO\n SLCT\n Spell\n"
        exit
       fi
       method=$OPTARG
       ;;
    d) if [ "$OPTARG" != "Android" ] && [ "$OPTARG" != "Apache" ] && [ "$OPTARG" != "BGL" ] && [ "$OPTARG" != "Hadoop" ] && [ "$OPTARG" != "HDFS" ] && [ "$OPTARG" != "HealthApp" ] && [ "$OPTARG" != "HPC" ] && [ "$OPTARG" != "Linux" ] && [ "$OPTARG" != "Mac" ] && [ "$OPTARG" != "OpenSSH" ] && [ "$OPTARG" != "OpenStack" ] && [ "$OPTARG" != "Proxifier" ] && [ "$OPTARG" != "Spark" ] && [ "$OPTARG" != "Thunderbird" ] && [ "$OPTARG" != "Windows" ] && [ "$OPTARG" != "Zookeeper" ] ; then
        printf "The argument \"$OPTARG\" is invalid. Please change it to a dataset present in the list.\n\nAllowed datasets: \n Android\n Apache\n BGL\n Hadoop\n HDFS\n HealthApp\n HPC\n Linux\n Mac\n OpenSSH\n OpenStack\n Proxifier\n Spark\n Thunderbird\n Windows\n Zookeeper\n"
        exit
       fi
       dataset=$OPTARG
       ;;
    :) printf "Missing argument for -%s\n" "$OPTARG" >&2
       #printf "Plase add argument from the list of methods: \n AEL\n Drain\n IPLoM\n LenMa\n LFA\n LKE\n LogCluster\n logmatch\n LogMine\n LogSig\n MoLFI\n SHISO\n SLCT\n Spell\n"
       printf "\nFor complete instructions on how to run the script use flag -h\n"
       exit 1
       ;;
   \?) printf "Illegal option: -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
shift $((OPTIND - 1))

echo "$method"
echo "$dataset"

#for i in 2 4 10 20 50 100 200 300
#do
#    for j in {1..10}
#    do
#        echo "Run number $j for dataset of size $i"
#    done
#done
ls
python3.7 python_scripts/create_results_files.py $method $dataset

cd ..
cd demo/

#python3.7 "$method"_demo.py $dataset 2 1

#declare -a StringArray=("AEL" "Drain" "IPLoM" "LenMa" "LFA" "LKE" "LogCluster" "logmatch" "LogMine" "LogSig" "MoLFI" "SHISO" "SLCT" "Spell")
declare -a StringArray=("Drain")

for value in ${StringArray[@]}
  do
  for i in 2 4
  do
      echo $value
      for j in 1 2 3 4 5
      do
          echo "\nRun $j for $method parsing "$i"k logs\n"
          python3.7 "$method"_demo.py $dataset $i $j $method
      done
  done
done

#for i in 2 4 10
#do
#    for j in {1..10}
#    do
#        echo "\nRun $j for $method parsing "$i"k logs\n"
#        python3.7 "$method"_demo.py $dataset $i $j
#    done
#done

#python3.7 Drain_demo.py HDFS 2
#python3.7 Drain_demo.py HDFS 2

#python3.7 {method}_demo.py [dataset] [size]
#python3.7 {Drain}_demo.py
#python python_scripts/augment_data.py 0 $dataset #2k logs
#python python_scripts/augment_data.py 1 $dataset #4k logs
#python python_scripts/augment_data.py 4 $dataset #10k logs
#python python_scripts/augment_data.py 9 $dataset #20k logs
#python python_scripts/augment_data.py 24 $dataset #50k logs
#python python_scripts/augment_data.py 49 $dataset #100k logs
#python python_scripts/augment_data.py 99 $dataset #200k logs
#python python_scripts/augment_data.py 149 $dataset #300k logs

echo "Finished running experiments for $method!"
echo "Done experiment"
