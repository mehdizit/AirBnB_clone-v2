#!/usr/bin/env bash
# Configured nginx server and sets up web server for deployment

sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir -p /data
sudo mkdir -p /data//web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Holberton School it's AirBnB" > /data/web_static/releases/test/index.html
sudo ln -sf data/web_static/releases/test/ data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;

    location /hbnb_static {
        alias /data/web_static/current;
    }
    location /redirect_me {
        return 301  http://google.com/;
    }
    error_page 404 /custom_404.html;
    location = /custom_404.html {
		internal;
	}

}" > /etc/nginx/sites-available/default
sudo service nginx restart
