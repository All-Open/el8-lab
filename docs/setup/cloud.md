# Using Cloud Instance

## Which One?

You can run `EL 8` on any cloud - there's no preffered one.

Each major Public Cloud vendor offers free credits.

## Instance T-Shirt Size

Instance should have 2 GiB of RAM and 20 GiB disk space.

## Image Minor Version

Image versions tend to lag behind the official `EL 8` releases. If you fail to find the latest minor version, just run `dnf update`.

## Image

Use one of the official images.

| Operating System | Cloud Vendor     | Comment     |
|:----------------:|:----------------:|:-----------:|
| `RHEL 8`         | [AWS](https://aws.amazon.com/marketplace/pp/Amazon-Web-Services-Red-Hat-Enterprise-Linux-8/B07T4SQ5RZ) | `t2.small` minimum |
| `CentOS 8`       | AWS              | n/a <br /> Only third-party images are available |
| `OL 8`           | [AWS](https://aws.amazon.com/marketplace/pp/Supported-Images-Oracle-Linux-8/B0844ZYYJ6) | `t2.small` minimum |
| `RHEL 8`         | [Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/endorsed-distros) | `Standard_D1` is good |
| `CentOS 8`       | [Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/endorsed-distros) | `Standard_D1` is good |
| `OL 8`           | Azure            | n/a         |
| `RHEL 8`         | [GCP](https://console.cloud.google.com/marketplace/details/rhel-cloud/rhel-8) | `n1-standard-1` is good |
| `CentOS 8`       | [GCP](https://console.cloud.google.com/marketplace/details/centos-cloud/centos-8) | `n1-standard-1` is good |
| `OL 8`           | GCP              | n/a         |

## Launch

Start your `EL 8` instance and proceed to the next step.
