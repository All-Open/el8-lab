# Getting Started

## All Open Enterprise Linux 8 Labs

Welcome to All Open Enterprise Linux 8 Labs! If you have not already, read [langing page](/) first.

All Open Labs are distributed as a single RPM package that works on any `Enterprise Linux 8`. The most popular choices are `Red Hat Enterprise Linux 8` (`RHEL 8`), `CentOS 8` and `Oracle Linux 8` (`OL 8`) but everything should work on any derived distribution. To make it easier, I often call them `Enteprise Linux 8` or `EL 8` in short.

## Understading Lab Ecosystem

All you need to get started is any `Enterprise Linux 8` system up and running with `root` user and Internet access.

You can choose one of two paths. Either launch a virtual machine to install `EL 8` yourself or use existing cloud or `Vagrant` image.

Here's summary of available options:

| Option                                             | Description                                    |
|:--------------------------------------------------:|:----------------------------------------------:|
| Installation in Virtual Machine                    | Manually performed installation |
| Spinning up Vagrant Box                            | Using `Vagrant` to create VM |
| Launching Cloud instance                           | Public Clouds offer instance images with free credits to run them |
| Anything else                                      |  Bare metal, Private Cloud, Moon Lander |

<!---
## Special Lab Requirements

Some labs pose additional requirements. Summary:

* Installation requires full access to virtual machine and its bootloader.
* Disk/filesystem labs may require extra disk attached.
* Cloud image lab requires cloud access.

However, majority of the labs can be accomplished even when additional requirements are not satisfied.
--->

## FAQ

> Can I run labs on an existing machine?

No, better get another one. Changes in boot process, networking and storage could render it unusable.

> Can I run lab inside a container?

No, unfortunately. Many labs require host-level access to kernel functions.
