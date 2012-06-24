#
# TODO:
#	- fix stupid prefix
#	- pl desc
# if prefix is not set
# etc goes to /usr

Summary:	Qingy is a replacement for getty
Summary(pl):	Qingy to zastepca getty
Name:		qingy
Version:	0.2
Release:	0.2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	2c9e7d20200f5c72e90b4cb974821b35
BuildRequires:	DirectFB-devel
BuildRequires:	pam-devel
URL:		http://qingy.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qingy is a replacement for getty. It uses DirectFB to provide a fast,
nice GUI without the overhead of the X Window System. It allows the user
to log in and start the session of his choice (text terminal, GNOME,
KDE, wmaker, etc.).

%description -l pl
Qingy jest zast�pc� getty. U�ywa DirectFB aby zapewni� szybkie, �adne
GUI bez nadmiarowo�ci X Window System. Pozwala u�ytkownikom zalogowa�
si� i wybra� sesj� (terminal tekstowy, GNOME, KDE, wmaker, itp.).

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
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/%{name}/settings
/etc/%{name}/default/*
%attr(755,root,root) %{_sbindir}/*
