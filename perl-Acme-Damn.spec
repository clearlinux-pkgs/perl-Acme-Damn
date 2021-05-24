#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Acme-Damn
Version  : 0.08
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/I/IB/IBB/Acme-Damn-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IB/IBB/Acme-Damn-0.08.tar.gz
Summary  : "'Unbless' Perl objects."
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Acme-Damn-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
NAME
Acme::Damn - 'Unbless' Perl objects.
SYNOPSIS
use Acme::Damn;
my $ref = ... some reference ...
my $obj = bless $ref , 'Some::Class';

... do something with your object ...

%package dev
Summary: dev components for the perl-Acme-Damn package.
Group: Development
Provides: perl-Acme-Damn-devel = %{version}-%{release}
Requires: perl-Acme-Damn = %{version}-%{release}

%description dev
dev components for the perl-Acme-Damn package.


%package perl
Summary: perl components for the perl-Acme-Damn package.
Group: Default
Requires: perl-Acme-Damn = %{version}-%{release}

%description perl
perl components for the perl-Acme-Damn package.


%prep
%setup -q -n Acme-Damn-0.08
cd %{_builddir}/Acme-Damn-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
/usr/share/man/man3/Acme::Damn.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Acme/Damn.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Acme/Damn/Damn.so
