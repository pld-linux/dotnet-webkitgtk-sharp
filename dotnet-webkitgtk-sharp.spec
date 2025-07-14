Summary:	C# bindings for WebKitGTK+ 3.0 using GObject Introspection
Summary(pl.UTF-8):	Wiązania C# do biblioteki WebKitGTK+ 3.0 wykorzystujące GObject Introspection
Name:		dotnet-webkitgtk-sharp
Version:	2.0.0
Release:	1
License:	LGPL v3
Group:		Libraries
Source0:	https://github.com/xDarkice/webkitgtk-sharp/releases/download/%{version}/webkitgtk-sharp-%{version}.tar.gz
# Source0-md5:	259d1b85975a93b878fa1bdc4254e83f
Patch0:		pkgconfig.patch
URL:		https://github.com/xDarkice/webkitgtk-sharp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp3-devel >= 2.99.2
BuildRequires:	dotnet-soup-sharp-devel
BuildRequires:	gtk-webkit3-devel >= 2.0
BuildRequires:	libtool >= 2:2
BuildRequires:	mono-csharp >= 1.1.0
BuildRequires:	mono-devel
BuildRequires:	monodoc >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	gtk-webkit3 >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser. It is made to be
embedded in other applications, such as mail readers, or web browsers.

This package provides Mono bindings for WebKitGTK+ 3.0 libraries.

%description -l pl.UTF-8
WebKit to silnik przeglądarki internetowej, wywodzący się z projektów
KHTML i KJS dla platformy KDE, używany głównie w przeglądarce Safari
firmy Apple. Stworzony został aby móc osadzać go w innych aplikacjach,
takich jak czytniki poczty czy przeglądarki stron internetowych.

Ten pakiet dostarcza dowiązań Mono do bibliotek WebKitGTK+ 3.0.

%package devel
Summary:	WebKitGTK# 3 development files
Summary(pl.UTF-8):	Pliki programistyczne WebKitGTK# 3
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc >= 2.6

%description devel
WebKitGTK# 3 development files.

%description devel -l pl.UTF-8
Pliki programistyczne WebKitGTK# 3.

%prep
%setup -q -n webkitgtk-sharp-%{version}
%patch -P0 -p1

install -d doc/en

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwebkitgtksharpglue-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkitgtksharpglue-1.10.2.so
%{_prefix}/lib/mono/gac/webkitgtk-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/webkitgtk-sharp
%{_datadir}/gapi-3.0/webkitgtk-sharp-api.xml
%{_pkgconfigdir}/webkitgtk-sharp-3.0.pc
%{_prefix}/lib/monodoc/sources/webkitgtk-sharp-docs.*
