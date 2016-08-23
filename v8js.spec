%define        pre_built_dir /home/lesstif/v8js
%define        module_dir `php-config --extension-dir`
%define        ini_dir      /etc/php.d/

Name: v8js
Summary: PHP extension for Google's V8 Javascript engine. The extension allows you to execute Javascript code in a secure sandbox from PHP. The executed code can be restricted using a time limit and/or memory limit. This provides the possibility to execute untrusted code with confidence.
Version: 1.3.1
Release: 1
License: PHP
Group: Development/Tools
URL: https://github.com/phpv8/v8js
Requires: v8
BuildRoot: %{_tmppath}/%{name}

%description
%{summary}

%prep

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/%{module_dir}
mkdir -p  %{buildroot}/%{ini_dir}

## module
cp %{pre_built_dir}/modules/v8js.so  %{buildroot}/%{module_dir}

## ini
echo -e "; Enable v8js extension module\nextension=v8js.so" >  %{buildroot}/%{ini_dir}/v8js.ini

%clean

%files
%defattr(-,root,root,-)
%{_sysconfdir}/*
%{module_dir}/*

%changelog
* Mon Aug 23 2016 KwangSeob Jeong <lesstif@gmail.com>
- First Build
