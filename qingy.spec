#
# TODO:
#	- fix stupid prefix
# if prefix is not set
# etc goes to /usr

Summary:	Qingy - a replacement for getty
Summary(pl):	Qingy - zastêpca getty
Name:		qingy
Version:	0.2.3
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	aff76c982645ea7afc948fedb475fc00
URL:		http://qingy.sourceforge.net/
BuildRequires:	DirectFB-devel
BuildRequires:	fbset
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qingy is a replacement for getty. It uses DirectFB to provide a fast,
nice GUI without the overhead of the X Window System. It allows the user
to log in and start the session of his choice (text terminal, GNOME,
KDE, wmaker, etc.).

%description -l pl
Qingy jest zastêpc± getty. U¿ywa DirectFB aby zapewniæ szybkie, ³adne
GUI bez nadmiarowo¶ci X Window System. Pozwala u¿ytkownikom zalogowaæ
siê i wybraæ sesjê (terminal tekstowy, GNOME, KDE, wmaker, itp.).

%prep
%setup -q

%build
%{__autoconf}
%configure \
	--prefix=/

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_sysconfdir}/%{name}
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/settings
%{_sysconfdir}/%{name}/sessions
%{_sysconfdir}/%{name}/themes
%{_sysconfdir}/pam.d/%{name}
%{_sysconfdir}/directfbrc.qingy
%attr(755,root,root) %{_sbindir}/*
