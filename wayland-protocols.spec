Name:           wayland-protocols
Version:        1.14
Release:        1%{?dist}
Summary:        Wayland protocols that adds functionality not available in the core protocol

License:        MIT
URL:            http://wayland.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  wayland-devel

%description
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%package devel
Summary:        Wayland protocols that adds functionality not available in the core protocol

%description devel
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%prep
%autosetup

%build
%configure

%install
%make_install

%files devel
%license COPYING
%doc README
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/

%changelog
* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 1.14-1
- Update to 1.14
- Resolves: #1554439

* Tue Sep 19 2017 Olivier Fourdan <ofourdan@redhat.com> - 1.10-1
- Update to 1.10

* Wed Jul 19 2017 Kalev Lember <klember@redhat.com> - 1.9-1
- Update to 1.9

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 16 2016 Kalev Lember <klember@redhat.com> - 1.7-1
- Update to 1.7

* Fri Aug 12 2016 Kalev Lember <klember@redhat.com> - 1.6-1
- Update to 1.6

* Tue Jul 26 2016 Kalev Lember <klember@redhat.com> - 1.5-1
- Update to 1.5

* Tue May 24 2016 Kalev Lember <klember@redhat.com> - 1.4-1
- Update to 1.4

* Mon Apr 11 2016 Kalev Lember <klember@redhat.com> - 1.3-1
- Update to 1.3

* Mon Mar 07 2016 Kalev Lember <klember@redhat.com> - 1.2-1
- Update to 1.2

* Thu Feb 18 2016 Kalev Lember <klember@redhat.com> - 1.1-1
- Update to 1.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-2
- Fix description

* Thu Nov 26 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-1
- Update to released 1.0
- Move XMLs to devel pkg
- Drop non-interesting part of description

* Sun Nov 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.0-0.gitf828a43
- Initial package
