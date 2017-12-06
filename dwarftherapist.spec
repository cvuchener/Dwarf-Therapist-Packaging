Name:		dwarftherapist
Version:	39.1.1
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
make %{?_smp_mflags}


%install
%make_install


%files
%license LICENSE.txt
%doc README.rst CHANGELOG.txt
%{_bindir}/DwarfTherapist
%{_datadir}/dwarftherapist
%{_datadir}/icons
%{_datadir}/applications


%changelog

