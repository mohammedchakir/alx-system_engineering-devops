# Puppet manifest to increase Nginx traffic configuration
# Author: Mohammed-chakir <zerroukimedchakir@gmail.com>

# increase the ULIMIT using sed command
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
