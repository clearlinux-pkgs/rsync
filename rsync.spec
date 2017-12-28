#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6C859FB14B96A8C5 (wayned@samba.org)
#
Name     : rsync
Version  : 3.1.2
Release  : 28
URL      : https://rsync.samba.org/ftp/rsync/src/rsync-3.1.2.tar.gz
Source0  : https://rsync.samba.org/ftp/rsync/src/rsync-3.1.2.tar.gz
Source1  : rsyncd.service
Source99 : https://rsync.samba.org/ftp/rsync/src/rsync-3.1.2.tar.gz.asc
Summary  : A fast, versatile, remote (and local) file-copying tool
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ X11
Requires: rsync-bin
Requires: rsync-config
Requires: rsync-doc
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : popt-dev
Patch1: sync_to_master.patch
Patch2: 0001-Handle-archaic-checksums-properly.patch
Patch3: 0002-Don-t-forget-to-tweak-sum_update.patch
Patch4: 0003-Only-allow-a-modern-checksum-method-for-passwords.patch
Patch5: cve-2017-15994.nopatch
Patch6: cve-2017-16548.patch
Patch7: cve-2017-17433.patch
Patch8: cve-2017-17434.patch
Patch9: cve-2017-17434-1.patch

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
Requires: rsync-config

%description bin
bin components for the rsync package.


%package config
Summary: config components for the rsync package.
Group: Default

%description config
config components for the rsync package.


%package doc
Summary: doc components for the rsync package.
Group: Documentation

%description doc
doc components for the rsync package.


%prep
%setup -q -n rsync-3.1.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514411732
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%reconfigure --disable-static
make  %{?_smp_mflags} make reconfigure && make V=1 %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1514411732
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/rsyncd.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rsync

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/rsyncd.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
