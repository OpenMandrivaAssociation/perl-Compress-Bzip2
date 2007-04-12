%define module	Compress-Bzip2
%define name	perl-%{module}
%define version 2.09
%define release %mkrel 2

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Interface to Bzip2 compression library
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}
Source:		    http://www.cpan.org/modules/by-module/Compress/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2 compression
library (see "AUTHOR" for details about where to get Bzip2). A relevant subset
of the functionality provided by Bzip2 is available in Compress::Bzip2.

All string parameters can either be a scalar or a scalar reference.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress
%{_mandir}/*/*

