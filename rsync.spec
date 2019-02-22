#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6C859FB14B96A8C5 (wayned@samba.org)
#
Name     : rsync
Version  : 3.1.3
Release  : 38
URL      : https://rsync.samba.org/ftp/rsync/src/rsync-3.1.3.tar.gz
Source0  : https://rsync.samba.org/ftp/rsync/src/rsync-3.1.3.tar.gz
Source1  : rsyncd.service
Source99 : https://rsync.samba.org/ftp/rsync/src/rsync-3.1.3.tar.gz.asc
Summary  : A fast, versatile, remote (and local) file-copying tool
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ X11
Requires: rsync-bin = %{version}-%{release}
Requires: rsync-license = %{version}-%{release}
Requires: rsync-man = %{version}-%{release}
Requires: rsync-services = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : popt-dev
Patch1: cve-2017-16548.nopatch

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
Requires: rsync-man = %{version}-%{release}
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
%setup -q -n rsync-3.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550796159
export LDFLAGS="${LDFLAGS} -fno-lto"
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --without-included-zlib
make  %{?_smp_mflags} make reconfigure && make V=1 %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1550796159
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rsync
cp COPYING %{buildroot}/usr/share/package-licenses/rsync/COPYING
cp popt/COPYING %{buildroot}/usr/share/package-licenses/rsync/popt_COPYING
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/rsyncd.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rsync

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rsync/COPYING
/usr/share/package-licenses/rsync/popt_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rsync.1
/usr/share/man/man5/rsyncd.conf.5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rsyncd.service
