%define upstream_name	 Compress-Bzip2
%define upstream_version 2.09

Summary:	Interface to Bzip2 compression library
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Compress/%{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires:	perl-devel

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2 compression
library (see "AUTHOR" for details about where to get Bzip2). A relevant subset
of the functionality provided by Bzip2 is available in Compress::Bzip2.

All string parameters can either be a scalar or a scalar reference.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress
%{_mandir}/man3/*

