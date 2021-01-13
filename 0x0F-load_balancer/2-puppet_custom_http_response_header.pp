exec {'Install Nginx':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && echo "Holberton School for the win!" | sudo tee /var/www/html/index.html && sudo sed -i "/^.*sendfile.*/i add_header X-Served-By $hostname;" /etc/nginx/nginx.conf && sudo service nginx restart',
  provider => shell,
}
