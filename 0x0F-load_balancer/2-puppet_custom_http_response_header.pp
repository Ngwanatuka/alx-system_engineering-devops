# Puppet class to configure Nginx with a custom response header
class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => 'Hello World!',
  }

  file { '/var/www/html/error404.html':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => "Ceci n'est pas une page",
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

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /error404.html;

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
