Summary:	Python wrapper for goo.gl URL shortener
Name:		python-googl
Version:	0.2.2
Release:	4
Source0:	https://files.pythonhosted.org/packages/16/b8/3cd10b97c268633dc73a9f8a1c5232776c34db3a6c1fc86085e79c29fc0f/%{name}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/python-googl/
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
%{python_sitelib}/googl/__pycache__/__init__.cpython-*.opt-1.pyc



%changelog
* Mon Sep 26 2011 Lev Givon <lev@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 701208
- imported package python-googl

