# Installation Lab Introduction

This guide helps in organizing you own `Enterprise Linux 8` (or `EL8` in short) installation environment.

Before you begin, keep in mind that there is a chance you don't need to perform full system installation. Possible reasons:

* Anaconda Installer does not introduce any significant changes so there is a little reason to learn it
* Installation process is lenghty and boring
* Cloud instances have `RHEL 8` and `CentOS 8` preinstalled
* ~~Vagrant Box have `CentOS 8` preinstalled~~ (not released yet!)

Consult [lab setup](LABS.md#Setup) for details.

## Prerequisites

1. Grab ISO image. Choose one of two options:

  * `RHEL 8`
    * [Download from official site](https://developers.redhat.com/products/rhel/download/)
    * Registration is required, but Developer Subscription is free of charge
  * ~~`CentOS 8`~~
    * Not released yet!

2. Choose your hypervisor

A popular choice is [VirtualBox](https://www.virtualbox.org/) that works on all major platforms.
The other option is your platform native Hypervisor, like KVM on Linux or Hyper-V on Windows.
VMware or oVirt installation are also feasible.

The choice is yours!

## Lab - Performing Installation

Create a new Virtual Machine, insert ISO image and complete the installation.

## After Installation

1. Click through First Boot dialog.

2. [Register your system](https://access.redhat.com/solutions/253273) to make software repositories available (`RHEL 8` only).

The following command should do it:
```
# subscription-manager register --username <username> --password <password> --auto-attach
```

## Grading

The is no formal grading process. It's done when it's complete :)
