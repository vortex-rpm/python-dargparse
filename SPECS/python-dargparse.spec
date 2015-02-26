# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python-dargparse
Version:        0.2.5
Release:        3.vortex%{?dist}
Summary:        Declarative command-line argument parser for python
Group:          Development/Libraries
License:        MIT
URL:            http://pypi.python.org/pypi/dargparse
Source0:        http://pypi.python.org/packages/source/d/dargparse/dargparse-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools, python-argparse
Requires:	python-argparse

%description
Declarative command-line argument parser for Python.

%prep
%setup -q -n dargparse-%{version}

%install
rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
* Wed Feb 26 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.2.5-3.vortex
- Fix build and deps.

* Wed Feb 26 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.2.5-2.vortex
- Fix description.

* Wed Feb 25 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.2.5-1.vortex
- Initial packaging.
