# Podman

## Description
The purpose of this lab is to forget about `docker` and shamelessly start using `podman`. Like if it was `docker`!

## Task list
* Installation
    * Install `podman`
    * Make sure that `docker` redirects to `podman`
* Image management
    * Pull `docker.io/library/centos:8` image 
    * Tag it `all-open:8`
* Image Building
    * Create `Containerfile` containing `FROM scratch` or any other content
    * Build an OCI-formateed image tagged `all-open:oci`
    * Build a Docker-formatted imaged tagged `all-open:docker`
* Cockpit
    * Install `podman` plugin for Cockpit
    * Run `all-open:8` image with the following specification
        * Container name is `a-weema-weh`
        * It runs `sleep infinity` command
        * It has `all=open` environment variable defined (where `all` is the key, `open` is its value)

!!! tip
    If don't like GUI tools feel free to complete Cockpit part of this lab using CLI. <br/>
    Too score 100% you will need to install `podman` plugin for Cockpit though.

## Setup
Execute
```console
# all-open-lab setup podman
```

## Grading
Execute
```console
# all-open-lab grade podman
```
