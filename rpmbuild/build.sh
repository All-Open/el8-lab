#!/usr/bin/env bash

cont_name="all-open/el8"
work_dir="rpmbuild"
pkg_name="all-open-el8-lab"

set -eux

if [ "$#" -eq 1 ] && [ "$1" == "magic" ]; then
    # install previously built RPM and execute bash in a cotainer
    user_arg="0"
    target="sh -c"
    args="yum localinstall --disablerepo=* -y /rpmbuild/RPMS/noarch/*.rpm; bash"
elif [ "$#" -gt 0 ];  then
    # execute command like bash in a cotainer
    user_arg="0"
    target="sh -c"
    args="$@"
else
    # execute this script in a container
    # to start RPM build
    user_arg="$(id -u):$(id -g)"
    target="${work_dir}/$0"
    args=""
fi

if ! [ -f /.dockerenv ]; then
    docker build -t ${cont_name} .
    docker run \
        -v "$(pwd)":/${work_dir}:z \
        -u ${user_arg} \
        -ti ${cont_name} ${target} "${args}"
    exit 0
fi

# in a container
cd ${work_dir}
rpmlint *.spec
rm -rf {BUILD*,SOURCES}
mkdir -p SOURCES/
tar zcvfp SOURCES/${pkg_name}.tar.gz ${pkg_name}/
rpmbuild -ba *.spec
