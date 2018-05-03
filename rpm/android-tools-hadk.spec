Name:       android-tools-hadk

Summary:    Minimal set of android tools
Version:    5.1.1_r38
Release:    1
Group:      Tools
License:    Apache 2.0
Source0:    android-tools-hadk-%{version}.tar.gz
Source1:    adb.mk
Source2:    fastboot.mk
Source3:    mkbootimg.mk
Patch0:     0001-Ignore-selinux.patch
Patch1:     0001-Add-vendors.patch
Patch2:     0001-Use-mmap-for-fastboot-data.patch
Patch3:     0001-mkbootimg-add-dt-parameter.patch

BuildRequires:  pkgconfig(openssl)
BuildRequires:  python
BuildRequires:  zlib

%description
android-tools for HADK

The upstream tarball is based of these upstream Android git repos:
  git clone https://android.googlesource.com/platform/system/core
  git clone https://android.googlesource.com/platform/system/extras

with unneeded files removed.

%package -n sudo-for-abuild
Summary:    Install this to allow OBS abuild user to use sudo in build
Group:      Development
Requires:   %{name} = %{version}-%{release}
Requires:   sudo

%description -n sudo-for-abuild
Allow abuild user to execute sudo in an OBS build root.

%prep
%setup -q
%patch0 -p1 -d extras
%patch1 -p1 -d core
%patch2 -p1 -d core
%patch3 -p1 -d core

%build
make -f %{SOURCE1} -C core/adb
make -f %{SOURCE2} -C core/fastboot
make -f %{SOURCE3} -C core/mkbootimg

%install
rm -rf %{buildroot}
install -D -m 755  core/adb/adb %{buildroot}%{_bindir}/adb
install -D -m 755  core/fastboot/fastboot %{buildroot}%{_bindir}/fastboot
install -D -m 755  core/mkbootimg/mkbootimg %{buildroot}%{_bindir}/mkbootimg
install -D -m 755  split_bootimg.pl %{buildroot}%{_bindir}/split_bootimg
install -D -m 755  mer-android-chroot %{buildroot}%{_bindir}/ubu-chroot
install -D -m 755  mer-ubusdk-bash-setup %{buildroot}%{_datadir}/ubu-chroot/mer-ubusdk-bash-setup
# For sudo-for-abuild
install -D -m 755  sudoers.abuild %{buildroot}%{_sysconfdir}/sudoers.d/abuild

%files
%defattr(-,root,root,-)
%{_bindir}/adb
%{_bindir}/fastboot
%{_bindir}/split_bootimg
%{_bindir}/mkbootimg
%{_bindir}/ubu-chroot
%{_datadir}/ubu-chroot/*

%files -n sudo-for-abuild
%defattr(-,root,root,-)
%{_sysconfdir}/sudoers.d/abuild
