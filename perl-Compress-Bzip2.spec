%define upstream_name	 Compress-Bzip2
%define upstream_version 2.09

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    %mkrel 7

Summary:	    Interface to Bzip2 compression library
License:	    GPL+ or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{upstream_name}
Source0:	    http://www.cpan.org/modules/by-module/Compress/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2 compression
library (see "AUTHOR" for details about where to get Bzip2). A relevant subset
of the functionality provided by Bzip2 is available in Compress::Bzip2.

All string parameters can either be a scalar or a scalar reference.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.90.0-5mdv2012.0
+ Revision: 765099
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.90.0-4
+ Revision: 763560
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.90.0-3
+ Revision: 667048
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-2mdv2011.0
+ Revision: 555228
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-1mdv2010.0
+ Revision: 402134
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.09-6mdv2009.0
+ Revision: 256037
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.09-4mdv2008.1
+ Revision: 151465
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.09-3mdv2008.0
+ Revision: 86184
- rebuild


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.09-2mdv2007.0
- spec cleanup

* Tue Aug 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.09-1mdk
- New release 2.09

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.08-2mdk 
- don't ship useless empty dirs
- spec cleanup

* Fri May 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.08-1mdk
- 2.08

* Sun Apr 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.03-1mdk
- New version 2.03
- Add Changes in doc, and tests

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 1.02-3mdk
- Rebuild for new perl

* Sun Aug 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-2mdk 
- fix line too long

* Sun Aug 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-1mdk 
- first mdk release

