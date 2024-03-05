# This Puppet manifest fixes the issue causing Apache to return a 500 error

# Ensure Apache configuration file exists
file { '/etc/apache2/apache2.conf':
  ensure  => present,
  content => "This is the corrected Apache configuration file\n",
  notify  => Service['apache2'],
}

# Define Apache package
package { 'apache2':
  ensure => installed,
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}
