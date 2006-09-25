#
#	TODO:
#		- build user have to be in the video group - build process
#		  needs access to /dev/fb0 - eliminate this.
#		- console locking mechanism is broken (as of 0.6.0) 
#		- have some bugs - pretty, but not 'rock solid stable' :-( 
#		- bcond for screensavers, x, ...
Summary:	Qingy - a replacement for getty
Summary(pl):	Qingy - zastêpca getty
Name:		qingy
Version:	0.9.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/qingy/%{name}-%{version}.tar.bz2
# Source0-md5:	87e7d3a7b06365b193d3486d3b14ab06
Patch0:		%{name}-ncurses.patch
URL:		http://qingy.sourceforge.net/
BuildRequires:	DirectFB-devel
BuildRequires:	autoconf
BuildRequires:	fbset
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:  xorg-proto-scrnsaverproto-devel
Requires:	DirectFB-font-ft2
Requires:	DirectFB-image-png
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qingy is a replacement for getty. It uses DirectFB to provide a fast,
nice GUI without the overhead of the X Window System. It allows the
user to log in and start the session of his choice (text terminal,
GNOME, KDE, wmaker, etc.).

Note: the console locking mechanism is broken in this release.

%description -l pl
Qingy jest zastêpc± getty. U¿ywa DirectFB aby zapewniæ szybkie, ³adne
GUI bez nadmiarowo¶ci X Window System. Pozwala u¿ytkownikom zalogowaæ
siê i wybraæ sesjê (terminal tekstowy, GNOME, KDE, wmaker, itp.).

Uwaga: mechanizm blokowania konsoli nie dzia³a poprawnie w tej wersji.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure \
	--enable-gpm-lock \
	--enable-optimizations \
	--enable-pam \
	--enable-x-support \
	--enable-DirectFB-support \
	--enable-screen-savers \
	
#--disable-shadow	don't use shadow for authentication
#--enable-static-build	compile qingy statically (default is no)
#--enable-crypto=<arg>	make qingy encrypt communications with its user interface. Supported crypto libraries are: none (no
#			encryption), openssl (openssl RSA encryption), libgcrypt (GNU libgcrypt RSA encryption)
#--with-screen-savers-dir specify screen savers directory
#--with-themes-dir       specify themes directory

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/Sessions

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/settings
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/welcomes
%{_sysconfdir}/%{name}/sessions
%{_datadir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pam.d/%{name}
%{_libdir}/%{name}
%attr(755,root,root) %{_sbindir}/*
%{_infodir}/*
%dir %{_sysconfdir}/X11/Sessions
