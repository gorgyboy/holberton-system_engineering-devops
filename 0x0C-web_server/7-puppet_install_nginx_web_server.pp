# Install and configure Nginx server

exec { 'Install Nginx':
  command => 'sudo apt-get update && sudo apt-get -y install nginx',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Config index.html':
  command => 'echo "Holberton School for the win!" | sudo tee /var/www/html/index.html',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Config redirection page':
  command => 'sudo sed -i "$(grep -n \'default_server\' /etc/nginx/sites-enabled/default | tail -1 | cut -f1 -d\':\') a\\ \n\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Restart Nginx service':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
}
