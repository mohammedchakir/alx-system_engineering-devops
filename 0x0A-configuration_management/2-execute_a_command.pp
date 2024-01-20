# Puppet Manifest for Killing a Process named "killmenow"
# Ensure all files end with a new line
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
