# Puppet Manifest for Creating a File in /tmp
# Ensure all files end with a new line
file { '/tmp/school':
ensure  => file,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
