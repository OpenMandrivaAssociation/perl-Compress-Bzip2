%define upstream_name	 Compress-Bzip2
%define upstream_version 2.28

Summary:	Interface to Bzip2 compression library
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Compress/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2 compression
library (see "AUTHOR" for details about where to get Bzip2). A relevant subset
of the functionality provided by Bzip2 is available in Compress::Bzip2.

All string parameters can either be a scalar or a scalar reference.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="%{optflags}"
%make_build

%check

# we have pbzip2 which seems to produce slightly
# difference outputs which this uses as reference
# so use std one to avoid a failing test
ln -s /usr/bin/bzip2-st ./bzip2
export PATH=$PWD:$PATH
%make_build test

%install
%make_install

%files 
%doc README.md Changes
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress
%{_mandir}/man3/*
