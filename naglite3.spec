# naglite3 - add-on overview webpage for Nagios or Icinga
#

Name:      naglite3
Summary:   naglite3 - Nagios status monitor for a NOC or operations room.
Version:   1.6
Release:   0.1
Vendor:    Erick Calder <ecalder@cpan.org>
Packager:  Nico Kadel-Garcia <nkadel@gmail.com>
License:   GPLv2
Group:     Applications/System
URL:       https://github.com/saz/naglite3/
BuildRoot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildArch: noarch

Requires:  httpd
Requires:  php >= 5.2
# Either Nagios or Icinga are compatible
#Requires: nagios
#Requires: icinga

Source:    Naglite3-%{version}.tar.gz
Source1:   naglite3.conf
Source2:   README.md
Patch1:	   Naglite3-1.6-heading.patch
Patch2:	   Naglite3-1.6-nagios.patch

%description
Nagios or Icinga status monitor for a NOC or operations room.


%prep
%setup -q -n Naglite3-%{version}
%patch1 -p1
%patch2 -p1

%build
# No build needed, this is just 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_var}/www/naglite3/
%{__install} -m0664 * %{buildroot}%{_var}/www/naglite3/.

%{__install} -D -m0664 -Dp %{SOURCE1} %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README.fedora

%{__install} -D -m0664 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/naglite3.conf

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %{_var}/www/naglite3
%{_var}/www/naglite3/*
# config.php is created locally by installer
%ghost %{_var}/www/naglite3/config.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/naglite3.conf
%doc %{_defaultdocdir}/%{name}-%{version}/README.fedora

%changelog
* Sun Mar 10 2013 <nkadel@gmail.com>
- Create first naglite3 RPM.
- Patch v1.6 tag to use optional headers from master.
- Add notes on Nagios RHEL compatible configurations.
