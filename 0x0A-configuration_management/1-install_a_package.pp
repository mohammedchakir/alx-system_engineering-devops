# Puppet Manifest for Installing Flask using pip3

# Ensure all files end with a new line
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}