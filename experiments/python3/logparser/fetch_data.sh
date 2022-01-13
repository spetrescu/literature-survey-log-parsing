apt-get update -y
apt-get install -y uni2ascii
pip install memory_profiler

pip install gdown
gdown https://drive.google.com/uc?id=1o_PZFPKf7caOggEh-TrTpeXRH_0b0AJW

tar -xvf scalability.tgz
rm scalability.tgz

rm scalability/Andriod/Andriod_2k.log
cd scalability/
cd Andriod/
for s in 1 4 10 20 50 100 200 300 500 1000
do
    uni2ascii Andriod_${s}k.log > ${s}k.log && mv ${s}k.log Andriod_${s}k.log
done
cd ..
cd ..
cp -v scalability/Andriod/* logs/Andriod/

rm scalability/BGL/BGL_2k.log
cd scalability/
cd BGL/
for s in 1 4 10 20 50 100 200 300
do
    uni2ascii BGL_${s}k.log > ${s}k.log && mv ${s}k.log BGL_${s}k.log
done
cd ..
cd ..
cp -v scalability/BGL/* logs/BGL/

rm scalability/HDFS/HDFS_2k.log
cd scalability/
cd HDFS/
for s in 1 4 10 20 50 100 200 300 500 1000
do
    uni2ascii HDFS_${s}k.log > ${s}k.log && mv ${s}k.log HDFS_${s}k.log
done
cd ..
cd ..
cp -v scalability/HDFS/* logs/HDFS/

rm scalability/OpenSSH/OpenSSH_2k.log
cd scalability/
cd OpenSSH/
for s in 1 4 10 20 50 100 200 300 500
do
    uni2ascii OpenSSH_${s}k.log > ${s}k.log && mv ${s}k.log OpenSSH_${s}k.log
done
cd ..
cd ..
cp -v scalability/OpenSSH/* logs/OpenSSH/

rm scalability/Thunderbird/Thunderbird_2k.log
cd scalability/
cd Thunderbird/
for s in 1 4 10 20 50 100 200 300 500 1000
do
    uni2ascii Thunderbird_${s}k.log > ${s}k.log && mv ${s}k.log Thunderbird_${s}k.log
done
cd ..
cd ..
cp -v scalability/Thunderbird/* logs/Thunderbird/

rm scalability/Windows/Windows_2k.log
cd scalability/
cd Windows/
for s in 1 4 10 20 50 100 200 300 500 1000
do
    uni2ascii Windows_${s}k.log > ${s}k.log && mv ${s}k.log Windows_${s}k.log
done
cd ..
cd ..
cp -v scalability/Windows/* logs/Windows/

rm -rf scalability/