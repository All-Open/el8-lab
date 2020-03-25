# Setting Up `Vagrant` Box

## Use `VirtualBox`!

I failed to find working `Vagrant` images for any hypervisor except `VirtualBox` so far.

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

### Oracle Linux 8

```console
mkdir all-open-lab && cd all-open-lab
vagrant init generic/oracle8
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

## Your Millage May Vary

Vagrant images (boxes) are not always updated to the latest minor version release of `EL 8`. Not only `RHEL 8`, `CentOS 8` and `OL 8` have independent release lifecycles, but also their Vagrant images lag from a few to weeks to a few months.

Visit [the generic boxes page](https://app.vagrantup.com/generic) for the detailed version information. Don't worry, it's extremally likely that you've got the right image. If not, simply run `dnf update`.

