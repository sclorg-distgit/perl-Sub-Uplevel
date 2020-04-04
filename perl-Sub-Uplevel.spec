%{?scl:%scl_package perl-Sub-Uplevel}

Name:           %{?scl_prefix}perl-Sub-Uplevel
Summary:        Apparently run a function in a higher stack frame
Epoch:          1
Version:        0.2800
Release:        10%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sub-Uplevel
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Sub-Uplevel-%{version}.tar.gz 
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.17
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
# Optional:
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.120900
# Explicit Run-time:
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)

# Remove bogus perl(DB) provide
%global __provides_exclude ^%{?scl_prefix}perl\\(DB\\)$

%description
Like Tcl's uplevel() function, but not quite so dangerous. The idea is
just to fool caller(). All the really naughty bits of Tcl's uplevel()
are avoided.

%prep
%setup -q -n Sub-Uplevel-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes CONTRIBUTING.mkdn README examples/
%{perl_vendorlib}/Sub/
%{_mandir}/man3/Sub::Uplevel.3*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.2800-10
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2800-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.2800-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2800-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2800-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.2800-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2800-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2800-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.2800-2
- Perl 5.26 rebuild

* Mon Apr  3 2017 Paul Howarth <paul@city-fan.org> - 1:0.2800-1
- Update to 0.2800
  - Tests now work if '.' is not in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2600-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug  5 2016 Paul Howarth <paul@city-fan.org> - 1:0.2600-1
- Update to 0.2600
  - Optimized calls to caller()
- Simplify find command using -delete

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.25-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.25-2
- Perl 5.22 rebuild

* Tue Jan 27 2015 Paul Howarth <paul@city-fan.org> - 1:0.25-1
- Update to 0.25
  - Fixed: 00-compile.t failures under Windows (CPAN RT#98230)
  - The 00-compile.t file has been moved to a release test and is no longer
    shipped
  - Moved bug tracker to Github
  - Updated repo files explaining how to contribute
  - Enabled Travis CI
- Specify all dependencies
- Use %%license
- Make %%files list more explicit

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.24-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1:0.24-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1:0.24-2
- Perl 5.16 rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:0.24-1
- 0.24 bump

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:0.22-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.22-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.22-3
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.22-2
- Mass rebuild with perl-5.12.0

* Sat Feb 13 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- don't run tests explicitly marked as "AUTHOR"
- add perl_default_filter
- auto-update by cpan-spec-update 0.002
- Add epoch of 1 (0.2002 => 0.22)
- added a new br on perl(Carp) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.2002-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Steven Pritchard <steve@kspei.com> 0.2002-1
- Update to 0.2002.
- BR Test::More.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1901-2
- Rebuild for perl 5.10 (again)

* Wed Feb 20 2008 Steven Pritchard <steve@kspei.com> 0.1901-1
- Update to 0.1901.
- Use fixperms macro instead of our own chmod incantation.
- Reformat to match cpanspec output.

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.18-2
- rebuild for new perl

* Mon Dec 17 2007 Ralf Corsépius <rc040203@freenet.de> - 0.18-1
- Update to 0.18.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.14-1
- Update to 0.14.

* Fri Jun 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.13-1
- Update to 0.13.

* Sat May 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.12-1
- Update to 0.12.
- Makefile.PL -> Build.PL.

* Fri Apr 21 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.10-1
- Update to 0.10.
- New upstream maintainer.
- Patch dropped.

* Wed Feb 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.09-4
- Uplevel.pm patch (perl 5.8.8). See bugzilla entry #182488.

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.09-3
- Dist tag.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.09-2
- rebuilt

* Thu Jul  8 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.09-1
- Update to 0.09 (with license info).

* Sun Jul  4 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.08-0.fdr.1
- First build.
