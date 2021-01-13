# Installs en configures a nginx server with a custom header

exec {'nginx':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && sudo sed -i "15i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo service nginx restart',
  provider => shell,
}
