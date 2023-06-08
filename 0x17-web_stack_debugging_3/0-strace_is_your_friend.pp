# fix a php error on php typo
class apache500 {
  $php_rout = '/var/www/html/wp-settings.php'

  file_line { 'fix_php_typo':
    path    => $php_rout,
    line    => "php",
    match   => "phpp",
    replace => true,
  }
}
