# Skopeo

## Description
The purpose of this lab is to manage container images with `skopeo`.

## Setup
Execute
```console
# all-open-lab setup skopeo
```

## Task list
* Make sure that `skopeo` is installed
* Using `skopeo`, copy `ubuntu:latest` from Docker Hub to the local container storage using `ubuntu:docker` tag
* Using `skopeo`, copy `ubuntu:latest` from Docker Hub to the local container storage using `ubuntu:oci` tag, but this time changing image format to OCI

## Grading

!!! warning "podman required!"
    Grading script requires `podman`. <br/>
    Make sure to install `podman` before grading.

Execute
```console
# all-open-lab grade skopeo
```
