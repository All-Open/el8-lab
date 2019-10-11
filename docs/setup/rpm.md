# Installing All Open Labs

## Enable `yum` Repository

As `root` user, execute the following command to start consuming All Open Labs repository:
```console
# curl https://repo.all-open.com/All-Open.repo -o /etc/yum.repos.d/All-Open.repo
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   160  100   160    0     0   1441      0 --:--:-- --:--:-- --:--:--  1454
```

You can confirm it works with:
```console
# yum repolist | grep All
Last metadata expiration check: 0:01:02 ago on pią, 11 paź 2019, 14:37:08.
All-Open                    All Open Package Repository                       2
```

## Install All Open Lab RPM

Just type:
```console
# yum install -y all-open-el8-lab
Dependencies resolved.
==============================================================================================================================================================================================
 Package                                            Arch                                     Version                                         Repository                                  Size
==============================================================================================================================================================================================
Installing:
 all-open-el8-lab                                   noarch                                   0.1.1-1.el8                                     All-Open                                    10 k

Transaction Summary
==============================================================================================================================================================================================
Install  1 Package

Total download size: 10 k
Installed size: 8.2 k
Downloading Packages:
all-open-el8-lab-0.1.1-1.el8.noarch.rpm                                                                                                                       6.9 kB/s |  10 kB     00:01
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                         6.9 kB/s |  10 kB     00:01
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                                                      1/1
  Installing       : all-open-el8-lab-0.1.1-1.el8.noarch                                                                                                                                  1/1
  Running scriptlet: all-open-el8-lab-0.1.1-1.el8.noarch                                                                                                                                  1/1
  Verifying        : all-open-el8-lab-0.1.1-1.el8.noarch                                                                                                                                  1/1

Installed:
  all-open-el8-lab-0.1.1-1.el8.noarch

Complete!
```
