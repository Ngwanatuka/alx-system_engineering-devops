# Puppet class to configure Nginx with a custom response header

class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => @(END_CONFIG)
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm;

        server_name _;

        location / {
            try_files $uri $uri/ =404;
            add_header X-Served-By $hostname;
        }
    }
    END_CONFIG
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}
