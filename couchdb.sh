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



curl -u 'admin:6Jr9Z8L#k5F!@yxBM7%$S&KPcAfX3G2d' -X PUT http://localhost:5984/users
curl -u 'admin:6Jr9Z8L#k5F!@yxBM7%$S&KPcAfX3G2d' -X POST http://localhost:5984/users -H "Content-Type: application/json" -d '{"name":"Hamood Siddiqui", "email":"hamood.siddiqui@gmail.com","AccessIDs":[0,1,2,3],"db":""}'


sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy




echo 6Jr9Z8L#k5F!@yxBM7%$S&KPcAfX3G2d


