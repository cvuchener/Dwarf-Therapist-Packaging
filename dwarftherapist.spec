Name:		dwarftherapist
Version:	42.0.0
Release:	1%{?dist}
Summary:	Dwarf management tool for Dwarf Fortress
URL:		https://github.com/Dwarf-Therapist/Dwarf-Therapist/
License:	MIT

%global repo_owner  Dwarf-Therapist
%global repo_name   Dwarf-Therapist

Source: https://github.com/%{repo_owner}/%{repo_name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: 0001-remove-readme-license.patch

BuildRequires: cmake, gcc-c++, qt5-qtbase-devel, qt5-qtdeclarative-devel


%description
Makes managing your dwarves' jobs and psychology easy!


%prep
%setup -n "%{repo_name}-%{version}"
%patch -p 1 -P 0


%build
%cmake 
%cmake_build


%install
%cmake_install


%files
%license LICENSE.txt
%doc README.rst CHANGELOG.txt
%{_bindir}/dwarftherapist
%{_datadir}/dwarftherapist
%{_datadir}/icons
%{_datadir}/applications


%changelog

