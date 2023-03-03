sudo apt update
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install curl net-tools



git checkout main
git pull
git merge origin/main

#Install Azure CLI only for MASTER
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

#For All
sudo apt-get -y install python3-pip
source ./venv/bin/activate
pip install -t lib flask 
pip install -t lib waitress 
pip install -t lib psutil
pip install -t lib google-auth google-auth2-tool google-auth-httplib2 google-api-python-client --upgrade
pip install -t lib google-auth google-auth-httplib2 google-api-python-client --upgrade
pip install -t lib --upgrade google-auth google-auth-httplib2 google-api-python-client
pip install -t lib azure
pip install -t lib azure-mgmt-compute azure-mgmt-network azure-common azure-identity msrestazure
sudo apt-get -y update
sudo apt-get -y upgrade

python3 -m main