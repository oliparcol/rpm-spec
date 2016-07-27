Name:           feh
Summary:        Image viewer at heart, though it does other cool stuff
Version:        2.16.1
Release:        2
License:        MIT
Group:          Graphics
URL:            http://feh.finalrewind.org/
Source0:        http://feh.finalrewind.org/%{name}-%{version}.tar.bz2

Requires:  imlib2
Requires:  libXt
Requires:  libXinerama
Requires:  libcurl
Requires:  libpng
Requires:  libjpeg
BuildRequires:  imlib2-devel
BuildRequires:  libXt-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel

%description
Feh is an image viewer, but it does a whole lot of other cool stuff as
well. There are simply too many to mention them here so please check the
docs/homepage.

%files
%doc AUTHORS ChangeLog README TODO examples
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop

%prep
%setup -q

%build
PREFIX=%{_prefix} DESTDIR=%{buildroot} make

%install
PREFIX=%{_prefix} DESTDIR=%{buildroot} make install

#let files section handle docs
rm -r %{buildroot}%{_docdir}

# removing prefix in feh.desktop file
sed -i "s|%{buildroot}||g" %{buildroot}/usr/share/applications/feh.desktop

%changelog

* Wed Jul 27 2016 oparent <oliparcol@gmail.com> 2.16.1-2
- Make it compatible with RHEL

* Sat Jul 02 2016 abfonly <abfonly@gmail.com> 2.16.1-1
- (89b301c) Log: Update to 2.16.1
- (89b301c) enabled and fixed tests
