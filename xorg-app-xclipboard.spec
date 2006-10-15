Summary:	xclipboard application
Summary(pl):	Aplikacja xclipboard
Name:		xorg-app-xclipboard
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xclipboard-%{version}.tar.bz2
# Source0-md5:	2c6ecedb10dc51adbb64c95f22fd99c2
Source1:	xclipboard.desktop
Source2:	xclipboard.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xclipboard application.

%description -l pl
Aplikacja xclipboard.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xclipboard
%attr(755,root,root) %{_bindir}/xcutsel
%{_datadir}/X11/app-defaults/XClipboard
%{_desktopdir}/xclipboard.desktop
%{_pixmapsdir}/xclipboard.png
%{_mandir}/man1/xclipboard.1x*
%{_mandir}/man1/xcutsel.1x*
