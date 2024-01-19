# Puppet Manifest for Killing a Process named "killmenow"

# Ensure all files end with a new line
exec { 'killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
