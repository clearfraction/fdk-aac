%global gitdate 2021
%global commit 801f67f671929311e0c9952c5f92d6e147c7b003
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fdk-aac
Version:        2.0.3
Release:        100.%{shortcommit}
Summary:        Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library for Android
License:        FDK-AAC
URL:            https://sourceforge.net/projects/opencore-amr
Source:         https://github.com/mstorsjo/fdk-aac/archive/%{commit}/%{name}-%{shortcommit}.tar.gz  
BuildRequires:  gcc
BuildRequires:  automake libtool
BuildRequires:  yasm nasm
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
%setup -n %{name}-%{commit}
autoreconf -vif

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
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
