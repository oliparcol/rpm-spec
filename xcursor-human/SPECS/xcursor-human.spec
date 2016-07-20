# Taken from https://aur.archlinux.org/packages/xcursor-human/
Name:           xcursor-human
Version:        0.6
Release:        0%{?dist}
Summary:        Ubuntu's default cursor theme
Group:          User Interface/X
License:        CCPL:by-sa
URL:            https://launchpad.net/human-cursors-theme/
Source0:        https://launchpad.net/ubuntu/+archive/primary/+files/human-cursors-theme_%{version}.tar.gz
Source1:        index.theme

BuildArch:      noarch
BuildRequires:  python-setuptools

%description
Ubuntu's default cursor theme.

%prep
%setup -n human-cursors-theme-%{version}

%install
python setup.py install --prefix=/usr --root="%{buildroot}" --optimize=1
install -Dm644 %{SOURCE1} "%{buildroot}/usr/share/icons/Human/index.theme"
# removing useless python egg description
rm -rf "%{buildroot}/usr/lib"

%files
%defattr(-,root,root,-)
#%doc CHANGES FAQ TODO
%{_datadir}/icons/Human/*
%{_datadir}/themes/Human/cursor.theme

%changelog
* Wed Jul 20 2016 Olivier Parent-Colombel <oliparcol@gmail.com> 0.6-1
- Initial RPM release.
