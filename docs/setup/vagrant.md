# Setting Up `Vagrant` Box

## Use `VirtualBox`!

I failed to find working `Vagrant` images for any hypervisor expect for `VirtualBox` so far.

Prerequisites:

* `VirtualBox` [installed](https://www.virtualbox.org/wiki/Downloads)
* `Vagrant` [installed](https://www.vagrantup.com/downloads.html)

## Quick setup scripts

Become `root` (or any other) user capable of spinning up Virtual Machines using `Vagrant` command.

### RHEL 8

```console
mkdir all-open-lab && cd all-open-lab
vagrant init generic/rhel8
vagrant up --provider=virtualbox
```

### CentOS 8

```console
mkdir all-open-lab && cd all-open-lab
vagrant init generic/centos8
vagrant up --provider=virtualbox
```

### OL 8

```console
mkdir all-open-lab && cd all-open-lab
vagrant box add --name ol8 https://yum.oracle.com/boxes/oraclelinux/ol80/ol80.box --provider=virtualbox
vagrant init ol8
vagrant up --provider=virtualbox
```

## Accessing Virtual Machine

```console
vagrant ssh
```

## Becoming `root`

```console
sudo -i
```
