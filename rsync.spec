#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6C859FB14B96A8C5 (wayned@samba.org)
#
Name     : rsync
Version  : 3.2.7
Release  : 51
URL      : https://rsync.samba.org/ftp/rsync/src/rsync-3.2.7.tar.gz
Source0  : https://rsync.samba.org/ftp/rsync/src/rsync-3.2.7.tar.gz
Source1  : rsyncd.service
Source2  : https://rsync.samba.org/ftp/rsync/src/rsync-3.2.7.tar.gz.asc
Summary  : A fast, versatile, remote (and local) file-copying tool
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ X11
Requires: rsync-bin = %{version}-%{release}
Requires: rsync-license = %{version}-%{release}
Requires: rsync-man = %{version}-%{release}
Requires: rsync-services = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : popt-dev
BuildRequires : pypi-commonmark
BuildRequires : zstd-dev

%description
Rsync is a fast and extraordinarily versatile file copying tool.  It can
copy locally, to/from another host over any remote shell, or to/from a
remote rsync daemon.  It offers a large number of options that control
every aspect of its behavior and permit very flexible specification of the
set of files to be copied.  It is famous for its delta-transfer algorithm,
which reduces the amount of data sent over the network by sending only the
differences between the source files and the existing files in the
destination.  Rsync is widely used for backups and mirroring and as an
improved copy command for everyday use.

%package bin
Summary: bin components for the rsync package.
Group: Binaries
Requires: rsync-license = %{version}-%{release}
Requires: rsync-services = %{version}-%{release}

%description bin
bin components for the rsync package.


%package license
Summary: license components for the rsync package.
Group: Default

%description license
license components for the rsync package.


%package man
Summary: man components for the rsync package.
Group: Default

%description man
man components for the rsync package.


%package services
Summary: services components for the rsync package.
Group: Systemd services

%description services
services components for the rsync package.


%prep
%setup -q -n rsync-3.2.7
cd %{_builddir}/rsync-3.2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666732239
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-lz4 \
--disable-xxhash
make  %{?_smp_mflags}  reconfigure && make V=1 %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1666732239
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rsync
cp %{_builddir}/rsync-%{version}/COPYING %{buildroot}/usr/share/package-licenses/rsync/4e462074002131183d7e67bccc2356b3391597e0
cp %{_builddir}/rsync-%{version}/popt/COPYING %{buildroot}/usr/share/package-licenses/rsync/61bb7a8ea669080cfc9e7dbf37079eae70b535fb
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/rsyncd.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rsync
/usr/bin/rsync-ssl

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rsync/4e462074002131183d7e67bccc2356b3391597e0
/usr/share/package-licenses/rsync/61bb7a8ea669080cfc9e7dbf37079eae70b535fb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rsync-ssl.1
/usr/share/man/man1/rsync.1
/usr/share/man/man5/rsyncd.conf.5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rsyncd.service
