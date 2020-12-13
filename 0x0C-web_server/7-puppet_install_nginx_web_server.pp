# Install and configure Nginx server

exec { 'Install Nginx':
  command => 'sudo apt-get update && sudo apt-get -y install nginx',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Config index.html':
  command => 'sudo echo "Holberton School for the win!" > /var/www/html/index.html',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Config redirection page':
  command => 'sudo sed -i "/# SSL configuration/ i\\ \\trewrite ^/redirect_me https://www.google.com permanent;\n" /etc/nginx/sites-enabled/default',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Restart Nginx service':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
}
