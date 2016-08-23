# v8 and v8js RPM binary spec




## Install from RPM Package

- You can install prebuilt rpm binary package from here.


```bash
$ curl -O  https://github.com/lesstif/v8js-rpm/
$ sudo yum localinstall -y 
```

## Building the RPM

### Prerequisites:

- GNU make 
- g++ 4.8 or newer
- libicu-devel


```bash
yum install gcc-c++ make libicu-devel
```

### compile v8

1. install depot_tools

```bash
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
cd depot_tools
```

1. adding PATH variable

```bash
export PATH=`pwd`/depot_tools:"$PATH"
```

1. download v8 source

```bash
fetch v8
cd v8
```

1. All build dependencies are fetched by running:

```bash
gclient sync
```

1. checkout tag

```bash
git checkout tags/5.2.371
```

1. setting build variable

```bash
# use libicu of operating system
export GYPFLAGS="-Duse_system_icu=1"
 
# Build (with internal snapshots)
export GYPFLAGS="${GYPFLAGS} -Dv8_use_snapshot=true -Dv8_use_external_startup_data=0 "
 
# eliminates swarming_client dependency
export GYPFLAGS="${GYPFLAGS} -Dtest_isolation_mode=noop"
 
# Force gyp to use system-wide ld.gold
export GYPFLAGS="${GYPFLAGS} -Dlinux_use_bundled_gold=0"
```

1. compile

```bash
make x64.release library=shared snapshot=on i18nsupport=on -j8
```

### create binary rpm package

change */home/lesstif/v8* to your v8 directory.

```bash
rpmbuild -bb v8.spec --buildroot=/tmp/v8 --define="pre_built_dir /home/lesstif/v8"
```

### compile v8js


1. clone v8js

```bash
git clone https://github.com/phpv8/v8js
```

1. checkout tag

```bash
git checkout tags/1.3.1
```

1. compile

```bash
phpize
./configure
make
make test
```

