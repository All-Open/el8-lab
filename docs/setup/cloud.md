# Using Cloud Instance

## Which One?

You can run `EL 8` on any cloud - there's no preffered one.

Each major Public Cloud vendor offers free credits.

## Instance T-Shirt Size

Instance should have 2 GiB of RAM and 20 GiB disk space.

## Image

Use one of official images.

| Operating System | Cloud Vendor     | Description |
|:----------------:|:----------------:|:-----------:|
| `RHEL 8`         | [AWS](https://aws.amazon.com/marketplace/pp/Amazon-Web-Services-Red-Hat-Enterprise-Linux-8/B07T4SQ5RZ) | `t2.small` type is good enough |
| `CentOS 8`       | AWS              | n/a         |
| `RHEL 8`         | Azure            | n/a         |
| `CentOS 8`       | Azure            | n/a         |
| `RHEL 8`         | [GCP](https://cloud.google.com/compute/docs/images#unshielded-images) | Currently available without Shielded VM support <br /> `n1-standard-1` type is good enough |
| `CentOS 8`       | [GCP](https://cloud.google.com/compute/docs/images#unshielded-images) | Currently available without Shielded VM support <br /> `n1-standard-1` type is good enough |

## Launch

Start your `EL 8` instance and proceed to the next step.
