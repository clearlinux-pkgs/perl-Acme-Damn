#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Acme-Damn
Version  : 0.08
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/I/IB/IBB/Acme-Damn-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IB/IBB/Acme-Damn-0.08.tar.gz
Summary  : "'Unbless' Perl objects."
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Acme-Damn-lib
Requires: perl-Acme-Damn-man
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

%package lib
Summary: lib components for the perl-Acme-Damn package.
Group: Libraries

%description lib
lib components for the perl-Acme-Damn package.


%package man
Summary: man components for the perl-Acme-Damn package.
Group: Default

%description man
man components for the perl-Acme-Damn package.


%prep
%setup -q -n Acme-Damn-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Acme/Damn.pm

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Acme/Damn/Damn.so

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Acme::Damn.3
