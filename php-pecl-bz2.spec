%define		php_name	php%{?php_suffix}
%define		modname	bz2
%define		status		stable
Summary:	%{modname} - A bzip2 management system
Summary(pl.UTF-8):	%{modname} - Zarządzanie plikami bzip2
Name:		%{php_name}-pecl-%{modname}
Version:	1.0
Release:	7
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	f6af3f931c582c90417177b66197f9cd
URL:		http://pecl.php.net/package/bz2/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	bzip2-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{modname} is an extension to create and parse bzip2 compressed data.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
%{modname} jest rozszerzeniem udostępniającym obsługę danych
skompresowanych do formatu bzip2.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
