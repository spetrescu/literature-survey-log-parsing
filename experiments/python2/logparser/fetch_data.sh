pip install gdown
gdown https://drive.google.com/uc?id=1zVaXpR7lOy3p1VwCLouHMDP6vtx69kLC

tar -xvf scalability.tgz
rm scalability.tgz

rm scalability/Andriod/Andriod_2k.log
cp -v scalability/Andriod/* logs/Andriod/

rm scalability/BGL/BGL_2k.log
cp -v scalability/BGL/* logs/BGL/

rm scalability/HDFS/HDFS_2k.log
cp -v scalability/HDFS/* logs/HDFS/

rm scalability/OpenSSH/OpenSSH_2k.log
cp -v scalability/OpenSSH/* logs/OpenSSH/

rm scalability/Thunderbird/Thunderbird_2k.log
cp -v scalability/Thunderbird/* logs/Thunderbird/

rm scalability/Windows/Windows_2k.log
cp -v scalability/Windows/* logs/Windows/

rm -rf scalability/
