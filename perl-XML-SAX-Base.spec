#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-XML-SAX-Base
Version  : 1.09
Release  : 41
URL      : https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-SAX-Base-1.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-SAX-Base-1.09.tar.gz
Summary  : 'Base class for SAX Drivers and Filters'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl
Requires: perl-XML-SAX-Base-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
XML::SAX::Base is intended for use as a base class for SAX filter modules
and XML parsers generating SAX events.

%package dev
Summary: dev components for the perl-XML-SAX-Base package.
Group: Development
Provides: perl-XML-SAX-Base-devel = %{version}-%{release}
Requires: perl-XML-SAX-Base = %{version}-%{release}

%description dev
dev components for the perl-XML-SAX-Base package.


%package perl
Summary: perl components for the perl-XML-SAX-Base package.
Group: Default
Requires: perl-XML-SAX-Base = %{version}-%{release}

%description perl
perl components for the perl-XML-SAX-Base package.


%prep
%setup -q -n XML-SAX-Base-1.09
cd %{_builddir}/XML-SAX-Base-1.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::SAX::Base.3
/usr/share/man/man3/XML::SAX::BuildSAXBase.3
/usr/share/man/man3/XML::SAX::Exception.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
