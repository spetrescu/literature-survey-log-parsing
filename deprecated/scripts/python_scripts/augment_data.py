import re
import random
import sys

n = len(sys.argv)

print("Running ", sys.argv[0])

print("Arguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")
print()

AUGMENT_TIMES = int(sys.argv[1])
DATASET = str(sys.argv[2])

list_of_augmentable_datasets = ['HDFS']

def Android():
    print("You typed zero.\n")


def Apache():
    print("You typed zero.\n")


def BGL():
    print("You typed zero.\n")


def Hadoop():
    print("You typed zero.\n")


def HDFS():
    file = open(f'../data/initial_data/{DATASET}/{DATASET}_2k.log', 'r')
    print(f'Reading /data/initial_data/{DATASET}/{DATASET}_2k.log')
    lines = file.read().splitlines()

    with open(f"../data/augmented_data/{DATASET}/{DATASET}_augmented_{AUGMENT_TIMES * 2 + 2}k.log", 'w+') as f:
        for line in lines:
            f.write(line + '\n')
            # print(line)
            for _ in range(AUGMENT_TIMES):
                augmented_line = HDFS_augment_line(line)
                f.write(augmented_line + '\n')
    print(f"Finished creating /data/augmented_data/{DATASET}/{DATASET}_augmented_{AUGMENT_TIMES * 2 + 2}k_augmented.log\n")


def HealthApp():
    print("You typed zero.\n")


def HPC():
    print("You typed zero.\n")


def Linux():
    print("You typed zero.\n")


def Mac():
    print("You typed zero.\n")


def OpenSSH():
    print("You typed zero.\n")


def OpenStack():
    print("You typed zero.\n")


def Proxifier():
    print("You typed zero.\n")


def Spark():
    print("You typed zero.\n")


def Proxifier():
    print("You typed zero.\n")


def Thunderbird():
    print("You typed zero.\n")


def Windows():
    print("You typed zero.\n")


def Zookeeper():
    print("You typed zero.\n")


# map the inputs to the function blocks
options = {"Android": Android,
           "Apache": Apache,
           "BGL": BGL,
           "Hadoop": Hadoop,
           "HDFS": HDFS,
           "HealthApp": HealthApp,
           "HPC": HPC,
           "Linux": Linux,
           "Mac": Mac,
           "OpenSSH": OpenSSH,
           "OpenStack": OpenStack,
           "Proxifier": Proxifier,
           "Spark": Spark,
           "Thunderbird": Thunderbird,
           "Windows": Windows,
           "Zookeeper": Zookeeper
           }

def HDFS_augment_line(line):
    counter = 1
    newstring = ''
    start = 0
    for m in re.finditer(r"blk_(|-)[0-9]+", line):
        end, newstart = m.span()
        newstring += line[start:end]
        randomly_shuffled_dynamic_blk = ''.join(random.sample(m.group()[4:], len(m.group()[4:])))
        rep = str("blk_") + str(randomly_shuffled_dynamic_blk)
        newstring += rep
        start = newstart
        counter += 1
    newstring += line[start:]
    augmented_line = newstring
    return augmented_line

def augment_data(dset):
    if dset in list_of_augmentable_datasets:
        options[dset]()
    else:
        print("Cannot augment data for ", dset)

augment_data(DATASET)
