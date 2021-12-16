cd ..
cd data/
cd scalability/
pip install gdown
gdown https://drive.google.com/uc?id=13vP-a2axw0CRJynLIdE_9L2uDMN4a2cv
tar -xvf scalability.tgz
rm scalability.tgz
mv -v scalability/* ./
rm -rf scalability/