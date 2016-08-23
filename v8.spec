%define        pre_built_dir /home/lesstif/v8

Name: v8
Summary: V8 is Google's open source high-performance JavaScript engine, written in C++ and used in Google Chrome, the open source browser from Google. It implements ECMAScript as specified in ECMA-262, 3rd edition, and runs on Windows XP or later, Mac OS X 10.5+, and Linux systems that use IA-32, ARM or MIPS processors. V8 can run standalone, or can be embedded into any C++ application.
Version: 5.2.371
Release: 1
License: BSD
Group: Development/Tools
URL: https://developers.google.com/v8/
Vendor:         The Chromium Project
Requires: glibc
Requires: libicu
BuildRoot: %{_tmppath}/%{name}

%description
%{summary}

%prep

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/{bin,include,lib64}
mkdir -p  %{buildroot}/usr/share/v8

## binary & lib
cp %{pre_built_dir}/out/x64.release/d8  %{buildroot}/usr/bin
cp %{pre_built_dir}/out/x64.release/obj.target/src/libv8_libplatform.a %{buildroot}/usr/lib64
cp %{pre_built_dir}/out/x64.release/lib.target/libv8.so  %{buildroot}/usr/lib64/libv8.so.%{version}

# create symlib link
ln -sf /usr/lib64/libv8.so.%{version}    %{buildroot}/usr/lib64/libv8.so.5
ln -sf /usr/lib64/libv8.so.5             %{buildroot}/usr/lib64/libv8.so

## header files
cp -R %{pre_built_dir}/include/*.h %{buildroot}/usr/include
cp -R %{pre_built_dir}/include/libplatform %{buildroot}/usr/include

## doc
cp %{pre_built_dir}/AUTHORS %{buildroot}/usr/share/v8
cp %{pre_built_dir}/ChangeLog %{buildroot}/usr/share/v8
cp %{pre_built_dir}/OWNERS      %{buildroot}/usr/share/v8
cp %{pre_built_dir}/LICENSE*    %{buildroot}/usr/share/v8
cp -R %{pre_built_dir}/samples  %{buildroot}/usr/share/v8

%clean

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datarootdir}/*

%changelog
* Mon Aug 22 2016 KwangSeob Jeong <lesstif@gmail.com>
- First Build
