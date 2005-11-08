#
#	TODO:
#		- build user have to be in the video group - build process
#		  needs access to /dev/fb0 - eliminate this.
# 
Summary:	Qingy - a replacement for getty
Summary(pl):	Qingy - zastêpca getty
Name:		qingy
Version:	0.6.0
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	4815233c4258f54ffbfe822e4ab45152
URL:		http://qingy.sourceforge.net/
BuildRequires:	DirectFB-devel
BuildRequires:	autoconf
BuildRequires:	fbset
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
Requires:	DirectFB-font-ft2
Requires:	DirectFB-image-png
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qingy is a replacement for getty. It uses DirectFB to provide a fast,
nice GUI without the overhead of the X Window System. It allows the
user to log in and start the session of his choice (text terminal,
GNOME, KDE, wmaker, etc.).

%description -l pl
Qingy jest zastêpc± getty. U¿ywa DirectFB aby zapewniæ szybkie, ³adne
GUI bez nadmiarowo¶ci X Window System. Pozwala u¿ytkownikom zalogowaæ
siê i wybraæ sesjê (terminal tekstowy, GNOME, KDE, wmaker, itp.).

%prep
%setup -q

%build
%{__autoconf}
%configure --enable-pam --disable-gpm-lock --disable-optimizations

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
