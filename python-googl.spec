Summary:	Python wrapper for goo.gl URL shortener
Name:		python-googl
Version:	0.2.2
Release:	2
Source0:	%{name}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://python-googl.googlecode.com/
BuildArch:	noarch
Requires:	python-httplib2
BuildRequires:	python-setuptools

%description
Python wrapper for goo.gl URL shortener.

%prep
%setup -q

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST



%changelog
* Mon Sep 26 2011 Lev Givon <lev@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 701208
- imported package python-googl

