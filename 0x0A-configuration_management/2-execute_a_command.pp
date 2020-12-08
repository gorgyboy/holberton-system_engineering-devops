# Kills killmenow process

exec { 'killmenow':
  command => 'pkill killmenow'
}
