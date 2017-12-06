Name:		dwarftherapist-doc
Version:	23.2beta
Release:	2%{?dist}
Summary:	Dwarf Therapist Guide
URL:		https://github.com/Dwarf-Therapist/Manual/
License:	MIT
BuildArch:	noarch
Requires:	dwarftherapist

%global repo_owner  Dwarf-Therapist
%global repo_name   Manual

Source: https://github.com/%{repo_owner}/%{repo_name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake, ImageMagick, texlive-bibtex, texlive-cm, texlive-hyphen-english, texlive-latex-bin, texlive-makeindex, texlive-mfware, texlive-preprint, texlive-sidecap, texlive-wrapfig


%description
Dwarf Therapist Guide


%prep
%setup -n "%{repo_name}-%{version}"
rm -rf %{_buildir}/out


%build
%cmake -DLATEX_OUTPUT_PATH=%{_builddir}/out
make %{?_smp_mflags}


%install
%make_install


%files
"%{_docdir}/dwarftherapist/Dwarf Therapist.pdf"


%changelog

