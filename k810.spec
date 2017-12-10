Summary:            Logitech K810 Keyboard Configurator
Name:               k810-conf
Version:            0.1
Release:            1%{?dist}
License:            GPL-3
Source:             http://blog.chschmid.com/media/k810_conf-v%{version}.tar.bz2
URL:                https://github.com/orpiske/gru
BuildRequires:      gcc


%description
This utility can be used to configure Logitech K810 keyboards


%build
./build.sh

%install
install -D k810_conf -m755  %{_buildrootdir}/%{_bindir}/k810_conf



%changelog
* Sun Dec 10 2017 Otavio R. Piske <angusyoung@gmail.com> - 0.1-1
- Initial packaging
