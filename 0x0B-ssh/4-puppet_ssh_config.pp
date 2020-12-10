# Set up client SSH configuration file to connect to a server without 
# typing a password

$str = "PasswordAuthentication no\n
        IdentityFile ~/.ssh/holberton\n
        ForwardAgent yes
        "

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => $str,
}
