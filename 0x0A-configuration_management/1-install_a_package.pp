package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  install_options => ['--ignore-installed', 'flask==2.1.0']
}

