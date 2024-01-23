# Puppet manifest to install and configure Nginx with 301 redirect

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  hasrestart => true,
}

# Create a basic HTML file for the root page
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Configure Nginx for the root page
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80;
    listen [::]:80;

    server_name _;

    location / {
        root /var/www/html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

