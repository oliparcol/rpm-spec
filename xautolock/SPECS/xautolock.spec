Name:           xautolock
Summary:        A program that launches a given program when your X session has been idle for a given time.
Version:        2.2
Release:        1
License:        GPL2
Group:          Screensavers
URL:            http://www.ibiblio.org/pub/linux/X11/screensavers/!INDEX.html
Source0:        http://www.ibiblio.org/pub/linux/X11/screensavers/%{name}-%{version}.tgz

Requires:  libX11
Requires:  libXScrnSaver
BuildRequires:  imake
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel

%description
A program that launches a given program when your X session has been idle
for a given time.

%files
%{_bindir}/xautolock

%prep
%setup -q

%build
xmkmf
PREFIX=%{_prefix} DESTDIR=%{buildroot} make

%install
PREFIX=%{_prefix} DESTDIR=%{buildroot} make install

%changelog

* Wed Jul 27 2016 oparent <oliparcol@gmail.com> 2.16.1-2
- Make it compatible with RHEL
