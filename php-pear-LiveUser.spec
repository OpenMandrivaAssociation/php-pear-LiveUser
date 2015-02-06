%define		_class		LiveUser
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.16.12
Release:	10
Summary:	User authentication and permission management framework
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/LiveUser/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Perm_LiveUser is a set of classes for dealing with user authentication
and permission management. Basically, there are three main elements
that make up this package:
- The LoginManager,
- The Auth containers,
- The Perm containers.

The LoginManager class takes care of the login process and can be
configured to use a certain permission container and one or more
different auth containers. That means, you can have your users' data
scattered amongst many data containers and have the LoginManager try
each defined container until the user is found. For example, you can
have all website users who can apply for a new account online on the
webserver's local database. Also, you want to enable all your
company's employees to login to the site without the need to create
new accounts for all of them. To achieve that, a second container can
be defined to be used by the LoginManager. You can also define a
permission container of your choice that will manage the rights for
each user. Depending on the container, you can implement any kind of
permission schemes for your application while having one consistent
API. Using different permission and auth containers, it's easily
possible to integrate newly written applications with older ones that
have their own ways of storing permissions and user data. Just make a
new container type and you're ready to go! Currently available are
RDBMS containers using PEAR::DB. More are soon to follow.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%doc %{upstream_name}-%{version}/sql
%{_datadir}/pear/%{_class}
%{_datadir}/pear/LiveUser.php
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.12-8mdv2012.0
+ Revision: 742029
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.12-7
+ Revision: 679382
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.16.12-6mdv2011.0
+ Revision: 613698
- the mass rebuild of 2010.1 packages

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16.12-5mdv2010.1
+ Revision: 473552
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.16.12-4mdv2010.0
+ Revision: 441241
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.16.12-3mdv2009.1
+ Revision: 322272
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.16.12-2mdv2009.0
+ Revision: 236905
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.16.12-1mdv2007.1
+ Revision: 140450
- 0.16.12
- add a bunch of missing files

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.16.11-1mdv2007.1
+ Revision: 81993
- Import php-pear-LiveUser

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.16.11-1mdk
- 0.16.11

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.16.8-1mdk
- 0.16.8
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-1mdk
- initial Mandriva package (PLD import)

