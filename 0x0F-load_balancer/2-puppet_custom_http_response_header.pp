# 2-puppet_custom_http_response_header.pp
# Puppet Manifest to configure Nginx with custom HTTP response header on a new Ubuntu machine.

class { 'nginx':
  ensure  => 'installed',
  service => 'running',
}

file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    add_header X-Served-By $hostname;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}\n",
  require => Class['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello, World!',
  require => File['/etc/nginx/sites-available/default'],
}

exec { 'remove default Nginx welcome page':
  command => 'rm -rf /var/www/html/*',
  path    => ['/bin', '/usr/bin'],
  require => File['/var/www/html/index.html'],
}

service { 'nginx':
  ensure  => 'running',
  require => [File['/etc/nginx/sites-available/default'], Exec['remove default Nginx welcome page']],
}

