%define name	python-googl
%define version	0.2.2
%define release %mkrel 1

Summary:	Python wrapper for goo.gl URL shortener
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://python-googl.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Python wrapper for goo.gl URL shortener.

%prep
%setup -q

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)

