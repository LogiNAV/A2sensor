#! /bin/bash
set -x


#-------------------------------------------------------------
#Instalaciones necesarias
#-------------------------------------------------------------

sudo apt-get install nginx -s
sudo apt-get install python3-pip -s
sudo pip3 install flask uwsgi -s
#----
sudo pip install -U Jinja2 -s
sudo pip install PyMySQL -s


#-------------------------------------------------------------
#Mover archivos GitHub
#-------------------------------------------------------------

cd ~

sudo mv A2sensor/flaskweb flaskweb
sudo mv A2sensor/loop loop
sudo mv A2sensor/utility utility
sudo rm -R A2sensor


#-------------------------------------------------------------
#Crear APP Flask
#-------------------------------------------------------------

sudo chown www-data /home/pi/flaskweb

#Configurar NGINX para usar uWSGI

sudo rm /etc/nginx/sites-enabled/default
sudo mv utility/flaskweb_proxy /etc/nginx/sites-available/flaskweb_proxy
sudo ln -s /etc/nginx/sites-available/flaskweb_proxy /etc/nginx/sites-enabled
sudo systemctl restart nginx

#Crear servicio para uWSGI y APP

sudo mv utility/uwsgi.service /etc/systemd/system/uwsgi.service
sudo mv utility/udp_db.service /etc/systemd/system/udp_db.service
sudo mv utility/estado.service /etc/systemd/system/estado.service
sudo mv utility/consulta.service /etc/systemd/system/consulta.service
#----
sudo systemctl daemon-reload
#----
sudo systemctl start uwsgi.service
sudo systemctl enable uwsgi.service
#----
sudo systemctl start udp_db.service
sudo systemctl enable udp_db.service
#----
sudo systemctl start estado.service
sudo systemctl enable estado.service
#----
sudo systemctl start consulta.service
sudo systemctl enable consulta.service
