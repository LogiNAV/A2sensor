#! /bin/bash
set -x


#-------------------------------------------------------------
#Instalaciones necesarias
#-------------------------------------------------------------

apt-get install nginx -y
apt-get install python3-pip -y
pip3 install flask uwsgi -y
#----
pip install -U Jinja2 -y
pip install PyMySQL -y

#-------------------------------------------------------------
#Mover archivos GitHub
#-------------------------------------------------------------

cd ~

mv A2sensor/flaskweb flaskweb
mv A2sensor/loop loop
mv A2sensor/utility utility
rm -R A2sensor


#-------------------------------------------------------------
#Crear APP Flask
#-------------------------------------------------------------

chown www-data /home/pi/flaskweb

#Configurar NGINX para usar uWSGI

rm /etc/nginx/sites-enabled/default
mv utility/flaskweb_proxy /etc/nginx/sites-available/flaskweb_proxy
ln -s /etc/nginx/sites-available/flaskweb_proxy /etc/nginx/sites-enabled
systemctl restart nginx

#Crear servicio para uWSGI y APP

mv utility/uwsgi.service /etc/systemd/system/uwsgi.service
mv utility/udp_db.service /etc/systemd/system/udp_db.service
mv utility/estado.service /etc/systemd/system/estado.service
mv utility/consulta.service /etc/systemd/system/consulta.service
#----
systemctl daemon-reload
#----
systemctl start uwsgi.service
systemctl enable uwsgi.service
#----
systemctl start udp_db.service
systemctl enable udp_db.service
#----
systemctl start estado.service
systemctl enable estado.service
#----
systemctl start consulta.service
systemctl enable consulta.service