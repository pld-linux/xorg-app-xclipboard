Summary:	xclipboard application - X clipboard client
Summary(pl.UTF-8):	Aplikacja xclipboard - klient schowka X
Name:		xorg-app-xclipboard
Version:	1.1.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xclipboard-%{version}.tar.xz
# Source0-md5:	859712d44bbc024a0fb21efc703d8ce0
Source1:	xclipboard.desktop
Source2:	xclipboard.png
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.1
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xclipboard application is used to collect and display text selections
that are sent to the CLIPBOARD by other clients. It is typically used
to save CLIPBOARD selections for later use. It stores each CLIPBOARD
selection as a separate string, each of which can be selected.

%description -l pl.UTF-8
Aplikacja xclipboard służy do zbierania i wyświetlania zaznaczeń
tekstu wysyłanych przez innych klientów do schowka (CLIPBOARD). Zwykle
jest używana do zapisywania zaznaczeń schowka w celu późniejszego
użycia. Zapisuje każde zaznaczenie jako osobny łańcuch znaków, z
których każdy może być wybrany.

%prep
%setup -q -n xclipboard-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xclipboard.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xclipboard.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xclipboard
%attr(755,root,root) %{_bindir}/xcutsel
%{_datadir}/X11/app-defaults/XClipboard
%{_desktopdir}/xclipboard.desktop
%{_pixmapsdir}/xclipboard.png
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xcutsel.1*
