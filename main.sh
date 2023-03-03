sudo apt update
sudo apt-get update
sudo apt-get upgrade
sudo apt install curl net-tools

#Install Azure CLI only for MASTER
#curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

#For All
sudo apt install python3-pip
source ./venv/bin/activate
pip install flask waitress psutil
pip install -t lib google-auth google-auth2-tool google-auth-httplib2 google-api-python-client --upgrade
pip install -t lib google-auth google-auth-httplib2 google-api-python-client --upgrade
pip install --upgrade google-auth google-auth-httplib2 google-api-python-client
pip install azure-mgmt-compute azure-mgmt-network azure-common azure-identity msrestazure
pip install couchdb
sudo apt-get update
sudo apt-get upgrade


python3 -m main





