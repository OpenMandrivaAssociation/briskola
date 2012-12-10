# This spec is based on Alberto Altieri work in MIB

Name:		briskola
Version:	1.0.0
Release:	%mkrel 1
Summary:	Clone of the Italian card game Briscola
Group:		Games/Cards
URL:		http://www.briskola.net
Source:		http://www.briskola.net/files/briskola-%{version}.tar.gz
Patch:		briskola.desktop.patch
License:	GPLv3+
BuildRequires:	cmake
BuildRequires:	glibc-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	freetype2-devel
BuildRequires:	libglib-devel
BuildRequires:	libice-devel
BuildRequires:	libopenssl-devel
BuildRequires:	png-devel
BuildRequires:	qt4-devel
BuildRequires:	libsm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	X11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxfixes-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxrender-devel
BuildRequires:	zlib-devel

%description
BrisKola is a clone of the Italian card game Briscola.
This is a classic Italian game, surely one of the most popular,
thanks to the simplicity of the rules
and the modest skills required to players. 

%prep
%setup -q
%patch -p1

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/briskola
%{_datadir}/applications/briskola.desktop
%{_datadir}/briskola/background/*.png
%{_datadir}/briskola/cards/*.png
%{_datadir}/briskola/decks/*.png
%{_datadir}/briskola/icons/*.png
%{_datadir}/briskola/misc/*.png
%{_datadir}/briskola/text/*.png
%{_datadir}/pixmaps/*.png



%changelog
* Tue Feb 21 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.0-1mdv2012.0
+ Revision: 778704
- Update BuildRequires
- imported package briskola

