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
pip install flask 
pip install waitress 
pip install psutil
pip install google-auth google-auth2-tool google-auth-httplib2 google-api-python-client --upgrade
pip install google-auth google-auth-httplib2 google-api-python-client --upgrade
pip install --upgrade google-auth google-auth-httplib2 google-api-python-client
pip install azure-mgmt-compute
pip install azure-mgmt-network
pip install azure-common 
pip install msrestazure
pip install azure-identity
sudo apt-get -y update
sudo apt-get -y upgrade

python3 -m main