%define        pre_built_dir /home/lesstif/v8js
%define        module_dir %(php-config --extension-dir)
%define        ini_dir      /etc/php.d/

Name: v8js
Summary: PHP extension for Google's V8 Javascript engine. 
Version: 1.3.1
Release: 1
License: PHP
Group: Development/Tools
URL: https://github.com/phpv8/v8js
Requires: v8
BuildRoot: %{_tmppath}/%{name}

%description
The extension allows you to execute Javascript code in a secure sandbox from PHP. The executed code can be restricted using a time limit and/or memory limit. This provides the possibility to execute untrusted code with confidence.

%prep

echo EXT_DIR=%{module_dir}

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
%{_sysconfdir}/php.d/*
%{module_dir}/*

%post

## for Amazon Linux
if [ -d "/usr/lib64/php/7.0/modules/" ]; then
	ln -s /usr/lib64/php/modules/v8js.so /usr/lib64/php/7.0/modules/v8js.so
fi

%postun
## for Amazon Linux
if [ -d "/usr/lib64/php/7.0/modules/" ]; then
	rm -f /usr/lib64/php/7.0/modules/v8js.so
fi

%changelog
* Mon Aug 23 2016 KwangSeob Jeong <lesstif@gmail.com>
- First Build
