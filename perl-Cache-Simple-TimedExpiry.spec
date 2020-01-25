#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Cache
%define	pnam	Simple-TimedExpiry
Summary:	Cache::Simple::TimedExpiry - cache for a period of time
Summary(pl.UTF-8):	Cache::Simple::TimedExpiry - buforowanie na określony czas
Name:		perl-Cache-Simple-TimedExpiry
Version:	0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ef124ab7776f3c257b9ffbed917e67a
URL:		http://search.cpan.org/dist/Cache-Simple-TimedExpiry/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cache::Simple::TimedExpiry - cache for a period of time.

%description -l pl.UTF-8
Cache::Simple::TimedExpiry - buforowanie na określony czas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Cache/Simple
%{perl_vendorlib}/Cache/Simple/*.pm
%{_mandir}/man3/*
