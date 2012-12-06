Summary:	Small Footprint CIM Client Library
Summary(pl.UTF-8):	Biblioteka kliencka CIM o małym narzucie
Name:		sblim-sfcc
Version:	2.2.4
Release:	3
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	1b901c459fcc7eb93167f1dcde7762d7
URL:		http://sblim.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The small footprint CIM client library (SFCC) is a C API allowing
client applications to interface with CIM implementations (e.g. CIM
servers). Due to its small memory and disk footprint it is well-suited
for embedded environments.

%description -l pl.UTF-8
Biblioteka kliencka CIM o małym narzucie (SFCC) to API C pozwalające
aplikacjom klienckim współpracować z implementacjami CIM (np.
serwerami CIM). Dzięki małym zużyciu pamięci i dysku biblioteka nadaje
się do wykorzystania w środowiskach wbudowanych.

%package devel
Summary:	Header files for CIM client libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek klienckich CIM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel

%description devel
Header files for CIM client libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek klienckich CIM.

%package static
Summary:	Static CIM client libraries
Summary(pl.UTF-8):	Statyczne biblioteki klienckie CIM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CIM client libraries.

%description static -l pl.UTF-8
Statyczne biblioteki klienckie CIM.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcimcClientXML.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcimcClientXML.so.0
%attr(755,root,root) %{_libdir}/libcimcclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcimcclient.so.0
%attr(755,root,root) %{_libdir}/libcmpisfcc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmpisfcc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcimcClientXML.so
%attr(755,root,root) %{_libdir}/libcimcclient.so
%attr(755,root,root) %{_libdir}/libcmpisfcc.so
%{_libdir}/libcimcClientXML.la
%{_libdir}/libcimcclient.la
%{_libdir}/libcmpisfcc.la
%{_includedir}/CimClientLib
%{_includedir}/cimc
%{_mandir}/man3/CMCIClient*.3*
%{_mandir}/man3/CMPI*.3*
%{_mandir}/man3/cmciConnect.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcimcClientXML.a
%{_libdir}/libcimcclient.a
%{_libdir}/libcmpisfcc.a
