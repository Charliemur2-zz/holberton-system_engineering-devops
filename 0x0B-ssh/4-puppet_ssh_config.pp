#  using Puppet to make changes to our configuration file.
file_line {'disable password login':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}
file_line {'pad to add the private key':
    path => 'etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/holberton'
}
