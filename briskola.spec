Summary:	Clone of the Italian card game Briscola
Name:		briskola
Version:	1.0.0
Release:	2
License:	GPLv3+
Group:		Games/Cards
Url:		http://www.briskola.net
Source0:	http://www.briskola.net/files/briskola-%{version}.tar.gz
Patch0:		briskola.desktop.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel

%description
BrisKola is a clone of the Italian card game Briscola. This is a classic
Italian game, surely one of the most popular, thanks to the simplicity of
the rules and the modest skills required to players.

%files
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

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build


