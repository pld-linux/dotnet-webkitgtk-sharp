# TODO
# - fix docs build
# - update descs (this is dor gtk3)
# - cleanup/update deps
# - ./configure[12519]: CHECK_MONOCAIRO: not found
# - ./configure[12520]: CHECK_SOUPSHARP: not found
#
# Conditional build:
%bcond_with	doc		# build with tests

%include	/usr/lib/rpm/macros.mono
Summary:	C# bindings for WebKitGTK+ 3.0 using GObject Introspection
Summary(pl.UTF-8):	WebKit# - wiązanie WebKit dla Mono
Name:		dotnet-webkitgtk-sharp
Version:	2.0.0
Release:	0.2
License:	X11/MIT
Group:		Libraries
Source0:	https://github.com/xDarkice/webkitgtk-sharp/releases/download/%{version}/webkitgtk-sharp-%{version}.tar.gz
# Source0-md5:	259d1b85975a93b878fa1bdc4254e83f
Patch0:		pkgconfig.patch
URL:		https://github.com/xDarkice/webkitgtk-sharp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.3
BuildRequires:	gtk-webkit-devel >= 1.1.15
BuildRequires:	mono-csharp >= 1.1.0
BuildRequires:	monodoc >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser. It is made to be
embedded in other applications, such as mail readers, or web browsers.

This package provides Mono bindings for WebKit libraries.

%description -l pl.UTF-8
WebKit to silnik przeglądarki internetowej, wywodzący się z projektów
KHTML i KJS dla platformy KDE, używany głównie w przeglądarce Safari
firmy Apple. Stworzony został aby móc osadzać go w innych aplikacjach,
takich jak czytniki poczty czy przeglądarki stron internetowych.

Ten pakiet dostarcza dowiązań Mono do bibliotek WebKit.

%package devel
Summary:	WebKit# development files
Summary(pl.UTF-8):	Pliki programistyczne WebKit#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc >= 2.6

%description devel
WebKit# development files.

%description devel -l pl.UTF-8
Pliki programistyczne WebKit#.

%prep
%setup -q -n webkitgtk-sharp-%{version}
%patch0 -p1

%{__sed} -i -e '/SUBDIRS/ s/doc//' Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}
%{?with_doc:%{__make} -C doc}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwebkitgtksharpglue-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_prefix}/lib/mono/gac/webkitgtk-sharp
%attr(755,root,root) %{_libdir}/libwebkitgtksharpglue-1.10.2.so
# -devel or runtime resource?
%{_datadir}/gapi-3.0/webkitgtk-sharp-api.xml

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/webkitgtk-sharp
%{_pkgconfigdir}/webkitgtk-sharp-3.0.pc
# docs subpackage?
%{?with_doc:%{_prefix}/lib/monodoc/sources/webkit-sharp-docs*}
