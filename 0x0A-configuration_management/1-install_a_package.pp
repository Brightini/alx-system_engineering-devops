# This manifest installs a package, flask
package { 'flask'
    name   => 'flask-2.1.0'
    ensure => 'installed'
    source => 'pip3'
}
