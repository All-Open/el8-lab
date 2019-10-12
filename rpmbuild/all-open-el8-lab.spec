Name:		all-open-el8-lab
Version:	0.1.0
Release:	1.el8
Summary:	All Open Labs for Enterprise Linux 8 In Action course

License:	GPLv3
URL:		https://github.com/All-Open/el8-lab
Source0:	%{name}.tar.gz

Recommends: bash-completion

BuildArch: noarch

%description
All Open Labs for Enterprise Linux 8 In Action course.
Official course site: https://all-open.com/enterprise-linux-8-in-action-training-workshop
Officual labs site: https://el8-lab.all-open.com

%prep
%setup -n %{name}

%install
cp -a . %{buildroot}

%files
/etc/bash_completion.d/*
%{_usr}/bin/*
%{_usr}/lib/*

%changelog

