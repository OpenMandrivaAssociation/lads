Summary:	Login anomaly detection system
Name:		lads
Version:	0.10
Release:	%mkrel 13
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10-11mdv2011.0
+ Revision: 666056
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-10mdv2011.0
+ Revision: 606394
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-9mdv2010.1
+ Revision: 523159
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.10-8mdv2010.0
+ Revision: 425500
- rebuild

* Thu Mar 19 2009 Frederic Crozat <fcrozat@mandriva.com> 0.10-7mdv2009.1
+ Revision: 357881
- Patch0: add LSB header to initscript
- suggest python-geoip

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.10-6mdv2009.1
+ Revision: 351345
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.10-5mdv2009.0
+ Revision: 222014
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2008.1
+ Revision: 134103
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2008.1
+ Revision: 128318
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-3mdv2007.1
+ Revision: 145400
- Import lads

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-3mdv2007.1
- use the %%mrel macro

* Fri Aug 19 2005 Frederic Lepied <flepied@mandriva.com> 0.10-2mdk
- fix requires

* Sun Jan 02 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.10-1mdk
- New release 0.10

* Mon Oct 11 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.9-1mdk
- New release 0.9: fix bug in non FAM mode and start after xinetd to
have a chance to run in FAM mode

