cd ..
cd data/
cd scalability/
pip install gdown
gdown https://drive.google.com/uc?id=1YBALSVclnFLMCLCnE7I50-tXF335cF1T
tar -xvf scalability.tgz
rm scalability.tgz
mv -v scalability/* ./
rm -rf scalability/