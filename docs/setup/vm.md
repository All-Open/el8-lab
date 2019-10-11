# Installation in Virtual Machine

## To VM or not to VM?

This guide helps in organizing yor own `Enterprise Linux 8` (or `EL8` in short) installation environment.

Before you begin, keep in mind that there is a chance you don't need to perform full system installation. Possible reasons:

* Anaconda Installer does not introduce any significant changes so there is a little reason to learn it
* Installation process is lenghty and boring
* Cloud instances have `RHEL 8` and `CentOS 8` preinstalled
* Vagrant Box have `CentOS 8` preinstalled

!!! tip
    If you decided to launch `EL8` from image, proceed to the next section now!

## Download ISO Image

Grab ISO image. Choose one of the options:

* `RHEL 8`
    * Download [here](https://developers.redhat.com/products/rhel/download/)
    * Registration and subscription is required
    * [Developer Subscription](https://developers.redhat.com/blog/2016/03/31/no-cost-rhel-developer-subscription-now-available/) is free of charge

* `CentOS 8`
    * Just download [here](https://wiki.centos.org/Download)

# Hypervisor

You need some Hypervisor to run a Virtual Machine.

A popular choice is [VirtualBox](https://www.virtualbox.org/) that works on all major platforms.
The other option is your platform native Hypervisor, like KVM on Linux or Hyper-V on Windows.
VMware or oVirt installation are also feasible.

The choice is yours!

# Performing Installation

Create a new Virtual Machine, insert ISO image and complete the installation. All Open Labs don't require Graphical User Interface. For your convenience, you can install it anyway.

# After Installation

1. Click through First Boot dialog.
2. Ensure GUI and/or SSH access.

## Grading

The is no formal grading process. It's done when it's complete :)
