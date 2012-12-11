%define upstream_name    String-Util
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Handy string processing utilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Debug::ShowStuff)

BuildArch:	noarch

%description
String::Util provides a collection of small, handy utilities
for processing strings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 656968
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 597088
- update to

* Sat Apr 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.0.0-1mdv2010.1
+ Revision: 533543
- import perl-String-Util


* Sat Apr 10 2010 cpan2dist 0-12-1mdv
- initial mdv release, generated with cpan2dist
