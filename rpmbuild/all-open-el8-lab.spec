Name:		all-open-el8-lab
Version:	0.0.1
Release:	1.el8
Summary:	All Open Labs for Introduction to Enterprise Linux 8 course

License:	GPL
URL:		https://github.com/All-Open/
Source0:	%{name}.tar.gz

BuildArch: noarch

%description
All Open Labs for Introduction to Enterprise Linux 8 course.
Visit https://all-open.com and https://github.com/All-Open/ for details.

%prep
%setup -n %{name}

%install
cp -a . %{buildroot}

%files
/etc/bash_completion.d/*
%{_usr}/bin/*
%{_usr}/lib/*

%changelog

