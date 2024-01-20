# Puppet Manifest for Installing Flask using pip3
package { 'werkzeug':
  ensure   => '0.16.1',
  provider => 'pip',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
