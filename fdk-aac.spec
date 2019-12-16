Name:           fdk-aac
Version:        2.0.1
Release:        5%{?dist}
Summary:        Fraunhofer FDK AAC Codec Library

License:        Apache License V2.0
URL:            https://sourceforge.net/projects/opencore-amr
Source0:        https://github.com/mstorsjo/fdk-aac/archive/v%{version}.tar.gz
BuildRequires:  libtool 
BuildRequires:  gettext
BuildRequires:  autoconf 
BuildRequires:  automake 
BuildRequires:  m4
BuildRequires:  pkg-config
BuildRequires:  glibc-dev
BuildRequires:  yasm	


%description
The Fraunhofer FDK AAC Codec Library ("FDK AAC Codec") is software that
implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio.


%package        dev
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    dev
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -n %{name}-%{version}


%build
libtoolize
aclocal
automake --add-missing
autoreconf
./configure --prefix=/usr --libdir=%{_libdir}/fdk-aac-freeworld --includedir=%{_includedir}/fdk-aac-freeworld --enable-shared --disable-static
# make gcc5/gcc6 happy
make 
# CXXFLAGS='%{optflags} -std=c++11 -Wno-narrowing' V=1 %{?_smp_mflags}



%install
make install DESTDIR=$RPM_BUILD_ROOT 
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

mkdir -p %{buildroot}/usr/share/pkgconfig/
mv -f %{buildroot}/%{_libdir}/fdk-aac-freeworld/pkgconfig %{buildroot}/usr/share/

mv -f %{buildroot}/%{_includedir}/fdk-aac-freeworld/fdk-aac/*.h %{buildroot}/%{_includedir}/fdk-aac-freeworld
rm -rf %{buildroot}/%{_includedir}/fdk-aac-freeworld/fdk-aac


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog NOTICE
%{_libdir}/fdk-aac-freeworld/*.so.*

%files dev
%defattr(-,root,root,-)
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac-freeworld
%{_includedir}/fdk-aac-freeworld/*.h
%{_libdir}/fdk-aac-freeworld/*.so
%{_datadir}/pkgconfig/%{name}.pc


%changelog

* Tue Oct 08 2019 David Va <davidva AT tuta DOT io> - 2.0.1-5
- Updated to 2.0.1-1

* Sat Jun 22 2019 David Va <davidva AT tuta DOT io> - 2.0.0-4
- Changes for avoid conflicts with fdk-aac-free

* Thu Nov 22 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 2.0.0-3
- Updated to 2.0.0

* Wed Mar 07 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.6-3
- Updated to 0.1.6-3

* Tue Sep 26 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.5-3
- Updated to 0.1.5-3

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.4-3
- Massive rebuild

* Tue Feb 23 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.4-2
- Rebuilt

* Fri Oct 30 2015 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.4-1
- Initial build
