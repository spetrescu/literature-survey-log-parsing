#!/bin/bash

usage="$(basename "$0") [-h] [-m method] [-d dataset] -- run scalability experiment for a specific method

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
    d) if [ "$OPTARG" != "Android" ] && [ "$OPTARG" != "SSH" ] && [ "$OPTARG" != "Apache" ] && [ "$OPTARG" != "BGL" ] && [ "$OPTARG" != "Hadoop" ] && [ "$OPTARG" != "HDFS" ] && [ "$OPTARG" != "HealthApp" ] && [ "$OPTARG" != "HPC" ] && [ "$OPTARG" != "Linux" ] && [ "$OPTARG" != "Mac" ] && [ "$OPTARG" != "OpenSSH" ] && [ "$OPTARG" != "OpenStack" ] && [ "$OPTARG" != "Proxifier" ] && [ "$OPTARG" != "Spark" ] && [ "$OPTARG" != "Thunderbird" ] && [ "$OPTARG" != "Windows" ] && [ "$OPTARG" != "Zookeeper" ] ; then
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

python3.7 python_scripts/create_results_files.py $method "scalability_experiments/${method}_results/"

cd ..
cd demo/

for d in Android HDFS Thunderbird Windows
do
  #for i in 1 2 4 10 20 50 100 200 300 500 1000
  for i in 1
  do
      echo $value
      #for j in 1 2 3 4 5 6 7 8 9 10
      for j in 1 2
      do
          echo "\nRun $j for $method parsing "$i"k logs\n"
          python3.7 "$method"_demo.py $d $i $j $method "scalability_experiments/${method}_results/${method}_results.csv"
      done
  done
done

for d in SSH
do
  #for i in 1 2 10 20 50 100 200 300 500
  for i in 1
  do
      echo $value
      #for j in 1 2 3 4 5 6 7 8 9 10
      for j in 1 2
      do
          echo "\nRun $j for $method parsing "$i"k logs\n"
          python3.7 "$method"_demo.py $d $i $j $method "scalability_experiments/${method}_results/${method}_results.csv"
      done
  done
done

for d in BGL
do
  #for i in 1 2 10 20 50 100 200 300
  for i in 1
  do
      echo $value
      #for j in 1 2 3 4 5 6 7 8 9 10
      for j in 1 2
      do
          echo "\nRun $j for $method parsing "$i"k logs\n"
          python3.7 "$method"_demo.py $d $i $j $method "scalability_experiments/${method}_results/${method}_results.csv"
      done
  done
done

echo "Finished running scalability experiments for $method!"
