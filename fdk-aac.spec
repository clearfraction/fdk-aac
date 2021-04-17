%global gitdate 20210407
%global commit 5329a829a0349bdf76a743efbb2d3f416b285e94
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fdk-aac
Version:        2.0.1
Release:        7.%{shortcommit}
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
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
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
