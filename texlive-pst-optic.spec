# revision 19704
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-optic
# catalog-date 2010-07-29 16:44:20 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-pst-optic
Version:	1.01
Release:	1
Summary:	Drawing optics diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-optic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-optic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package for drawing both reflective and refractive optics
diagrams. The package requires pstricks later than version
1.10.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-optic/pst-optic.tex
%{_texmfdistdir}/tex/latex/pst-optic/pst-optic.sty
%doc %{_texmfdistdir}/doc/generic/pst-optic/Changes
%doc %{_texmfdistdir}/doc/generic/pst-optic/README
%doc %{_texmfdistdir}/doc/generic/pst-optic/more_docs/dtk.pdf
%doc %{_texmfdistdir}/doc/generic/pst-optic/more_docs/pst-optic-examples.pdf
%doc %{_texmfdistdir}/doc/generic/pst-optic/more_docs/pst-optic-examples.tex
%doc %{_texmfdistdir}/doc/generic/pst-optic/pst-optic-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-optic/pst-optic-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-optic/pst-optic-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-optic/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
