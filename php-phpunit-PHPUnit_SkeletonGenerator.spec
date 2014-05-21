%define		status		stable
%define		pearname	PHPUnit_SkeletonGenerator
%define		php_min_version 5.3.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Tool that can generate skeleton test classes from production code classes and vice versa
Name:		php-phpunit-PHPUnit_SkeletonGenerator
Version:	1.2.0
Release:	3
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	c752da8f8b0c604b65eb5457f965640a
URL:		http://pear.phpunit.de/package/PHPUnit_SkeletonGenerator/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(reflection)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-ezc-ConsoleTools >= 1.6
Requires:	php-pear >= 1.3.14-2
Requires:	php-phpunit-Text_Template >= 1.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool that can generate skeleton test classes from production code
classes and vice versa.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/PHPUnit_SkeletonGenerator/* .

# some mess?
#mv .%{php_pear_dir}/SebastianBergmann/PHPUnit .%{php_pear_dir}/
for a in .%{php_pear_dir}/SebastianBergmann/PHPUnit/SkeletonGenerator/template/*.tpl.dist; do
	mv $a ${a%.dist}
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install

install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc ChangeLog.markdown LICENSE README.markdown
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/phpunit-skelgen
%dir %{php_pear_dir}/SebastianBergmann
%dir %{php_pear_dir}/SebastianBergmann/PHPUnit
%{php_pear_dir}/SebastianBergmann/PHPUnit/SkeletonGenerator
