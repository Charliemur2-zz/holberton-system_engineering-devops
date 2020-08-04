#!/usr/bin/env bash
#  using Puppet to make changes to our configuration file. Just as in the previous 
# configuration file task, we’d like you to set up your client SSH configuration file 
# so that you can connect to a server without typing a password.
file_line {'disable password login':
    path => '/etc/ssh/sshd_config',
    line => 'PasswordAuthentication yes',
}
file_line {'pad to add the private key':
    path => 'etc/ssh/sshd_config',
    line => 'IdentityFile ~/.ssh/holberton'
}
