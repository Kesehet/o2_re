#Installing CouchDB only for MASTER
sudo apt update
sudo apt install -y curl apt-transport-https gnupg
curl https://couchdb.apache.org/repo/keys.asc | gpg --dearmor | sudo tee /usr/share/keyrings/couchdb-archive-keyring.gpg >/dev/null 2>&1 source /etc/os-release
echo "deb [signed-by=/usr/share/keyrings/couchdb-archive-keyring.gpg] https://apache.jfrog.io/artifactory/couchdb-deb/ focal main" | sudo tee /etc/apt/sources.list.d/couchdb.list >/dev/null
sudo apt update
sudo apt install -y couchdb
sudo systemctl start couchdb
sudo nano /opt/couchdb/etc/local.ini
sudo systemctl restart couchdb



curl -u admin:admin -X PUT http://localhost:8443/users
curl -u admin:admin -X POST http://localhost:8443/users -H "Content-Type: application/json" -d '{"name":"Hamood Siddiqui", "email":"hamood.siddiqui@gmail.com","AccessIDs":[0,1,2,3],"db":""}'




