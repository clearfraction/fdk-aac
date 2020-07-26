Name:           fdk-aac
Version:        2.0.1
Release:        6%{?dist}
Summary:        Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library for Android

License:        FDK-AAC
URL:            https://sourceforge.net/projects/opencore-amr
Source0:        https://github.com/mstorsjo/fdk-aac/archive/v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  automake libtool
BuildRequires:  yasm
%description
The Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library
for Android is software that implements part of the MPEG Advanced Audio Coding
("AAC") encoding and decoding scheme for digital audio.


%package        dev
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    dev
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%setup -n %{name}-%{version}
autoreconf -vif

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install INSTALL="install"
find %{buildroot} -name '*.la' -print -delete

%post -p /usr/bin/ldconfig
%postun -p /usr/bin/ldconfig

%files
%doc ChangeLog
%license NOTICE
%{_libdir}/*.so.*

%files dev
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac
%{_includedir}/fdk-aac/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc


%changelog
# based on https://koji.fedoraproject.org/koji/packageinfo?packageID=27608
