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
  subscribe  => File_line['redirect'],
}

file { '/var/www/html/index.html':
  ensure  =>  present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School for the win!',
}

file_line { 'redirect':
  ensure  => present,
  after   => '\tlisten [::]:80 default_server;',
  path    => '/etc/nginx/sites-enabled/default',
  line    => '\trewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
