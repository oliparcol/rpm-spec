%global commit0 33b413b83234d457b9512219cf4c1020eb99a3de
%global gittag0 GIT-TAG
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           pa-applet
Version:        %{shortcommit0}
Release:        0%{?dist}
Summary:        PulseAudio control applet
Group:          Productivity/Multimedia/Sound/Mixers
License:        BSD
URL:            https://github.com/fernandotcl/pa-applet
Source0:        https://github.com/fernandotcl/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libnotify-devel
BuildRequires:  pulseaudio-libs-devel

Requires:       glib2
Requires:       gtk3
Requires:       libnotify
Requires:       pulseaudio-libs

%description
PulseAudio control applet

%prep
%autosetup -n %{name}-%{commit0}

%build
./autogen.sh
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/pa-applet
%{_mandir}/man1/*

%changelog
* Wed Jul 20 2016 Olivier Parent-Colombel <oliparcol@gmail.com> - 33b413b-0
- Initial RPM release.
