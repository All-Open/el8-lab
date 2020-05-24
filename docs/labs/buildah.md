# Buildah

## Description
The purpose of this lab is to build a container image without `Containerfile` or `Dockerfile` using `buildah`.

## Setup
Execute
```console
# all-open-lab setup buildah
```

## Task list
* Install `buildah`
* Use `buildah` commands to build a container image that:
    * Is built `from` `docker.io/library/centos:8`
    * It has `/root/all-open` file created
        * You can either use `mount` or `copy` or `add` command
    * Is `commit`ed with `centos:buildah` name
    * Make sure not to built  `Containerfile` or `Dockerfile` - `all-open-lab` checks that!

## Grading

!!! warning "podman required!"
    Grading script requires `podman`. <br/>
    Make sure to install `podman` before grading.

Execute
```console
# all-open-lab grade buildah
```
