# Kills killmenow process

exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/',
}
