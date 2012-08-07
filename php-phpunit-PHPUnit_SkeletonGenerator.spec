%define		status		stable
%define		pearname	PHPUnit_SkeletonGenerator
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Tool that can generate skeleton test classes from production code classes and vice versa
Name:		php-phpunit-PHPUnit_SkeletonGenerator
Version:	1.1.0
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	ef27a64ced03907608716a44397003ac
URL:		http://pear.phpunit.de/package/PHPUnit_SkeletonGenerator/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(pcre)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-ezc-ConsoleTools >= 1.6
Requires:	php-pear
Requires:	php-phpunit-Text_Template >= 1.1.1
Requires:	php-reflection
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool that can generate skeleton test classes from production code
classes and vice versa.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/PHPUnit_SkeletonGenerator/* .

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
%{php_pear_dir}/PHPUnit/SkeletonGenerator.php
%{php_pear_dir}/PHPUnit/SkeletonGenerator
