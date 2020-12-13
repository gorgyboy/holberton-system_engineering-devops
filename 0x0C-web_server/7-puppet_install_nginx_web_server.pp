# Install and configure Nginx server

exec { 'Install Nginx':
  command => 'sudo apt-get update';
  command => 'sudo apt-get -y install nginx';
  command => 'echo "Holberton School for the win!" | sudo tee /var/www/html/index.html';
  command => 'sudo sed -i "$(grep -n \'default_server\' /etc/nginx/sites-enabled/default | tail -1 | cut -f1 -d\':\') a\\ \\n\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default';
  command => 'sudo service nginx restart';
}
