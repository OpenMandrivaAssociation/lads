Summary:	Login anomaly detection system
Name:		lads
Version:	0.10
Release:	19
License:	GPLv2
Group:		System/Base
Url:		http://www.lepied.com/lads/
Source0:	http://www.lepied.com/lads/%{name}-%{version}.tar.bz2
# (fc) 0.10-7mdv add LSB header
Patch0:		0001-LSB-initscript.patch
BuildArch:	noarch

Requires(post,postun):	rpm-helper
Requires:	mailx
Requires:	python-fam
Requires:	sendmail-command
Suggests:	python-geoip

%description
LADS detects anomalies in login/logout.

%prep
%setup -q
%apply_patches

%install
%makeinstall_std

install -d %{buildroot}%{_initrddir}
mv %{buildroot}%{_sysconfdir}/init.d/lads %{buildroot}%{_initrddir}/lads

%post
%_post_service lads

%preun
%_preun_service lads

%files
%doc TODO README
%{_initrddir}/lads
%config(noreplace) %{_sysconfdir}/security/lads.conf
%{_datadir}/lads

