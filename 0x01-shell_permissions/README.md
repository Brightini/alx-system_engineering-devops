# SHELL PERMISSIONS

This project covers basic shell permission commands

## Editors

vi, vim or emacs.

## Tests

All scripts were tested on Ubuntu 20.04 LTS

## [0-iam_betty](https://github.com/Brightini/alx-system_engineering-devops/blob/master/0x01-shell_permissions/0-iam_betty): A script that switches the current user to the user `betty`
This will give the user, `betty`, temporary access to the superuser's privileges. When run, you will be prompted to input the superuser's password.
```bash 
bright@ubuntu:/alx-system_engineering-devops/0x01-shell_permissions$ ./0-iam_betty
Password:
root@ubuntu:/alx-system_engineering-devops/0x01-shell_permissions#
```
If successful, the prompt will be changed from `$` to `#`, indicating that you now have access to the root/superuser's privileges.

## [1-who_am_i](https://github.com/Brightini/alx-system_engineering-devops/blob/master/0x01-shell_permissions/1-who_am_i): A script that prints the effective username of the current user.
This prints the name associated with the current user id
```bash
bright@ubuntu:/alx-system_engineering-devops/0x01-shell_permissions$ ./0-iam_betty
bright
bright@ubuntu:/alx-system_engineering-devops/0x01-shell_permissions$
```


## Author
Bright Okon
