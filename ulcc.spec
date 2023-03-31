Name:           ulcc
Version:        1.0.1
Release:        2
Summary:        Teaching children by pictures
Group:          Education
License:        GPLv3+
Url:            https://bitbucket.org/admsasha/ulcc
Source0:        https://bitbucket.org/admsasha/ulcc/downloads/%{name}-%{version}.tar.gz

BuildRequires:	qt5-linguist-tools
BuildRequires:  qt5-macros
BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Multimedia)

%description
Teaching children by pictures is admirable facilities
to imparting knowledges.

%prep
%setup -q

%build
%qmake_qt5
%make

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README* CONTRIBUTORS
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
