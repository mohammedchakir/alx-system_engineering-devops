# Puppet manifest to increase Nginx traffic configuration
# Author: Mohammed-chakir <zerroukimedchakir@gmail.com>

# increase the ULIMIT using sed command
exec { 'fix_nginx_configuration':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Define Nginx service
exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/'
}
