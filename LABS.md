# All Open EL 8 Labs

Welcome to All Open Enterprise Linux 8 Labs!

If you have not already, start with reading [README](README.md) first.

# Prerequisites

All of the following labs work on any `Enterprise Linux 8`. The most popular choices are `Red Hat Enterprise Linux 8` and `CentOS 8` but everything should work on any derived distribution. To make it easier, I often call them `Enteprise Linux 8` or `EL 8` in short.

The following prerequisites must be met:

1. Runtime environment

Essentially, you need `EL 8` system up and running. There is quite a few options you can choose from.

| Option                                             | Supported OSes           | Description                                    |
| -------------------------------------------------- |:------------------------:| ---------------------------------------------- |
| [Installation](INSTALLATION.md) in Virtual Machine | `RHEL 8`, ~~`CentOS 8`~~ | Manually performed installation                |
| ~~Spinning up Vagrant Box~~                        | ~~`CentOS 8`~~           | ~~`vagrant init centos/8`~~ (not released yet) |
| Launching Cloud instance                           | `RHEL 8`, ~~`CentOS 8`~~ | Every major Public Cloud offers instance images, and a free tier to run them |
| Anything else                                      | may vary                 | Bare metal, Private Cloud, Moon Lander, anything else |

`CentOS 8` has not yet been released.

2. Root user

Root access is required.

3. Internet access

You will need to install lab RPM and often download packages from `yum` repositories.

4. Registration (`RHEL 8` only)

Your system needs an access to package repositories which may not be possible without prior system registration.
Run `subscription-manager` to do so.

5. Special lab requirements

Some labs pose additional requirements. Summary:
* Installation requires full access to virtual machine and its bootloader.
* Disk/filesystem labs may require extra disk attached.
* Cloud image lab requires cloud access.

However, majority of the labs can be accomplished even when additional requirements are not satisfied.

# Prerequisites - FAQ
> Can I run labs on an existing machine?

No, better get another one. Changes in boot process, networking and storage will render it unusable.

> Can I run lab inside a container?

No, unfortunately. Many labs require host-level access to kernel functions.

# Setup

Once you have you `EL 8` up and running, switch to root user and install lab RPM package.

TODO describe how lab RPM can be installed!

# Usage

RPM provides `all-open-lab` command capable of listing, preparing and grading labs.

To list of available labs type:
```
# all-open-lab list labs
(...)
```

In order to prepare your system for a given lab :
```
# all-open-lab setup <lab-name>
```

After you complete the lab check results with:
```
# all-open-lab grade <lab-name>
```

# Lab guide

List of labs:
* [prereq](#prereq)
* [packages](#packages)
* [dnf](#dnf)

## prereq

### Description
The purpose of this lab is to familarize you with `all-open-lab` tool, but also check if your system fulfills requirements.

### Setup
Execute the following command and make sure to have the same output:
```
# all-open-lab setup prereq
Preparing lab: Testing if prerequisites are met                                 [ OK ]
```

### Grading
Execute the following command and make sure to have the same output:
```
# all-open-lab grade prereq
Testing if prerequisites are met
    Checking if OS is running Enterprise Linux 8                                [ OK ]
    Checking if yum repo BaseOS is available                                    [ OK ]
    Checking if yum repo AppStream is available                                 [ OK ]
Overall lab status: [3/3]                                                       [ OK ]
```

## packages

### Description
The purpose of this lab is to explore new package management features.

Task list:

* Install `httpd` package without its weak dependencies

### Setup
Execute
```
# all-open-lab setup packages
```

### Grading
Execute
```
# all-open-lab grade packages
```

## dnf

### Description
The purpose of this lab is to configure DNF in accordance with organization requirements.

Task list:

* Make sure that `yum` command is available
* Make sure that `yum-utils` commands like `repoquery` are available
* Ensure performant `dnf` runs by having its cache always up-to-date
* Configure system to display pending security errata in MOTD (message of the day)

### Setup
Execute
```
# all-open-lab setup dnf
```

### Grading
Execute
```
# all-open-lab grade dnf
```
