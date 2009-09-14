%define		_class		LiveUser
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - user authentication and permission management framework
Name:		php-pear-%{_pearname}
Version:	0.16.12
Release:	%mkrel 4
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/LiveUser/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{Auth,Perm}/Storage

install -m0644 %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear
install -m0644 %{_pearname}-%{version}/Auth/*.php %{buildroot}%{_datadir}/pear/%{_class}/Auth
install -m0644 %{_pearname}-%{version}/Perm/*.php %{buildroot}%{_datadir}/pear/%{_class}/Perm
install -m0644 %{_pearname}-%{version}/Auth/Storage/*.php %{buildroot}%{_datadir}/pear/%{_class}/Auth/Storage
install -m0644 %{_pearname}-%{version}/Perm/Storage/*.php %{buildroot}%{_datadir}/pear/%{_class}/Perm/Storage

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,sql}
%dir %{_datadir}/pear/%{_class}/Auth
%dir %{_datadir}/pear/%{_class}/Perm
%dir %{_datadir}/pear/%{_class}/Auth/Storage
%dir %{_datadir}/pear/%{_class}/Perm/Storage
%{_datadir}/pear/%{_class}/Auth/*.php
%{_datadir}/pear/%{_class}/Perm/*.php
%{_datadir}/pear/%{_class}/Auth/Storage/*.php
%{_datadir}/pear/%{_class}/Perm/Storage/*.php
%{_datadir}/pear/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


