Summary:	Login anomaly detection system
Name:		lads
Version:	0.10
Release:	%mkrel 10
License:	GPL
Group:		System/Base
URL:		http://www.lepied.com/lads/
Source0:	http://www.lepied.com/lads/%{name}-%{version}.tar.bz2
# (fc) 0.10-7mdv add LSB header
Patch0:		0001-LSB-initscript.patch
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires:	python-fam, sendmail-command, mailx
Suggests:	python-geoip
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
LADS detects anomalies in login/logout.

%prep

%setup -q
%patch0 -p1 -b .lsb

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_initrddir}
mv %{buildroot}%{_sysconfdir}/init.d/lads %{buildroot}%{_initrddir}/lads

%clean
rm -rf %{buildroot}

%post
%_post_service lads

%preun
%_preun_service lads

%files
%defattr(-,root,root)
%doc TODO README
%{_initrddir}/lads
%config(noreplace) %{_sysconfdir}/security/lads.conf
%{_datadir}/lads


