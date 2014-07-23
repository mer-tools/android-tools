# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       android-tools

# >> macros
# << macros

Summary:    Minimal set of android tools
Version:    4.2.2_git20130218
Release:    9
Group:      Tools
License:    Apache 2.0
Source0:    android-tools-4.2.2_git20130218.tar.gz
Source1:    adb.mk
Source2:    fastboot.mk
Source3:    mkbootimg.mk
Source100:  android-tools.yaml
Patch0:     0001-Ignore-selinux-android.h.patch
Patch1:     0002-Original-split_bootimg.pl-from-http-www.enck.org-too.patch
Patch2:     0003-Provide-command-line-to-use-mkbootimg-to-recreate-th.patch
Patch3:     0004-Add-mer-android-chroot-to-enter-the-ubu-chroot-from-.patch
Patch4:     0005-Added-libmincrypt-for-building-mkbootimg.patch
Patch5:     0006-Require-r-option-Fix-broken-mount-for-HOME-in-some-i.patch
Patch6:     0007-Add-support-for-.mersdkubu.profile.patch
Patch7:     0008-Support-multiple-chroot-entry-invocation-to-support-.patch
BuildRequires:  pkgconfig(openssl)
BuildRequires:  libselinux-devel
BuildRequires:  python
BuildRequires:  zlib

%description
android-tools for Mer

The upstream tarball is based of these upstream Android git repos:
  git clone https://android.googlesource.com/platform/system/core
  git clone https://android.googlesource.com/platform/system/extras

with unneeded files removed.

Based on Debian android-tools package


%prep
%setup -q -n src

# 0001-Ignore-selinux-android.h.patch
%patch0 -p1
# 0002-Original-split_bootimg.pl-from-http-www.enck.org-too.patch
%patch1 -p1
# 0003-Provide-command-line-to-use-mkbootimg-to-recreate-th.patch
%patch2 -p1
# 0004-Add-mer-android-chroot-to-enter-the-ubu-chroot-from-.patch
%patch3 -p1
# 0005-Added-libmincrypt-for-building-mkbootimg.patch
%patch4 -p1
# 0006-Require-r-option-Fix-broken-mount-for-HOME-in-some-i.patch
%patch5 -p1
# 0007-Add-support-for-.mersdkubu.profile.patch
%patch6 -p1
# 0008-Support-multiple-chroot-entry-invocation-to-support-.patch
%patch7 -p1
# >> setup
# << setup

%build
# >> build pre
make -f %{SOURCE1} -C core/adb
make -f %{SOURCE2} -C core/fastboot
make -f %{SOURCE3} -C core/mkbootimg
#make -f `pwd`/ext4_utils.mk -C extras/ext4_utils
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
install -D -m 755  core/adb/adb %{buildroot}%{_bindir}/adb
install -D -m 755  core/fastboot/fastboot %{buildroot}%{_bindir}/fastboot
install -D -m 755  core/mkbootimg/mkbootimg %{buildroot}%{_bindir}/mkbootimg
install -D -m 755  split_bootimg.pl %{buildroot}%{_bindir}/split_bootimg
install -D -m 755  mer-android-chroot %{buildroot}%{_bindir}/ubu-chroot
install -D -m 755  mer-ubusdk-bash-setup %{buildroot}%{_datadir}/ubu-chroot/mer-ubusdk-bash-setup
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_bindir}/adb
%{_bindir}/fastboot
%{_bindir}/split_bootimg
%{_bindir}/mkbootimg
%{_bindir}/ubu-chroot
%{_datadir}/ubu-chroot/*
# >> files
# << files
