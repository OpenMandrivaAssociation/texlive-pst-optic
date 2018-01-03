Name:		texlive-pst-optic
Version:	1.02
Release:	1
Summary:	Drawing optics diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-optic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for drawing both reflective and refractive optics
diagrams. The package requires pstricks later than version
1.10.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-optic
%{_texmfdistdir}/tex/latex/pst-optic
%doc %{_texmfdistdir}/doc/generic/pst-optic

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
