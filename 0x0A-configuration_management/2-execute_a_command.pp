# Puppet Manifest for Killing a Process named "killmenow"
# Ensure all files end with a new line
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
