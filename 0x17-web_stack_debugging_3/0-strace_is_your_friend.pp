# This Puppet manifest fixes the issue causing Apache to return a 500 error
# Tmux find that the error is a "phpp" located in /var/www/html/wp-settings.php
# Uses of exec to correct line in wp-settings.php using sed
exec { 'fix_wp_settings_error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/',
}

# Define Apache service to ensure it's running
service { 'apache2':
  ensure => running,
  enable => true,
}
