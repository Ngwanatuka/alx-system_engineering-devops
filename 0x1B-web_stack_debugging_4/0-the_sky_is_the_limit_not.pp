# a script that increases nginx traffic
# and edit the ulimit

exec { 'edit-file':
    command => 'sed -i "s/15/4096" /etc/default/nginx',
    path    => ['/usr/local/bin', '/bin']
}

exec { 'restart-nginx':
    command => 'service nginx restart',
    path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}
