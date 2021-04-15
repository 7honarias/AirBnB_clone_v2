#!/usr/bin/env bash
# script that create web_static
sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "42i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx start
