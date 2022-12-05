# SHELL REDIRACTION
```DevOps``` ```Bash``` ```Shell```
This project covers basic shell redirection commands

## Editors
vi, vim or emacs

## Tests
All srcipts were tested on Ubuntu 20.04 LTS

[0-hello_world](https://github.com/Brightini/alx-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world): A script that prints “Hello, World”, followed by a new line to the standard output
```bash
bright@ubuntu:/0x02-shell_redirections$ ./0-hello_world
Hello World
```

[1-confused_smiley](https://github.com/Brightini/alx-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley): A script that displays a confused smiley ```"(Ôo)'```
```bash
bright@ubuntu:/0x02-shell_redirections$ ./1-confused_smiley
"(Ôo)'
```

[2-hellofile](https://github.com/Brightini/alx-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile): A script that displays the content of the /etc/passwd file
```bash
bright@ubuntu:/0x02-shell_redirections$ ./2-hellofile
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
_lp:*:26:26:Printing Services:/var/spool/cups:/usr/bin/false
_postfix:*:27:27:Postfix Mail Server:/var/spool/postfix:/usr/bin/false
_scsd:*:31:31:Service Configuration Service:/var/empty:/usr/bin/false
_ces:*:32:32:Certificate Enrollment Service:/var/empty:/usr/bin/false
_mcxalr:*:54:54:MCX AppLaunch:/var/empty:/usr/bin/false
_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false
```

[3-twofiles](https://github.com/Brightini/alx-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles): A script that displays the content of /etc/passwd and /etc/hosts
```bash
bright@ubutu:/0x02-shell_redirections$ ./3-twofiles
User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting. Do not change this entry.
##
127.0.0.1   localhost
255.255.255.255 broadcasthost
::1 localhost
$
```







