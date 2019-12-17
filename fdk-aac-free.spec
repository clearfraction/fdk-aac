Name:           fdk-aac-free
Version:        2.0.0
Release:        2%{?dist}
Summary:        Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library for Android

License:        FDK-AAC
URL:            https://cgit.freedesktop.org/~wtay/fdk-aac/log/?h=fedora
# Source0:      https://people.freedesktop.org/~wtay/fdk-aac-free-%%{version}.tar.gz
Source0:        https://0x0.st/z0A7.gz

BuildRequires:  gcc
BuildRequires:  automake libtool

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
%setup
autoreconf -vif

%build
%configure \
  --disable-silent-rules \
  --disable-static

%make_build


%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -print -delete

%ldconfig_scriptlets

%files
%doc ChangeLog README.fedora
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
