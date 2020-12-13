# Install and configure Nginx server

package { 'nginx':
  ensure => present,
  name   => 'nginx',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => Exec['redirect'],
}

file { '/var/www/html/index.html':
  ensure  =>  present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School for the win!',
}

exec { 'redirect':
  command     => 'sudo sed -i "/# SSL configuration/ i\ \trewrite ^/redirect_me google.com permanent;\n" /etc/nginx/sites-enabled/default',
  path        => ['/usr/bin', '/bin'],
}
