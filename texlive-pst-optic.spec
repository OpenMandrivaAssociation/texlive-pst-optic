# revision 19704
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-optic
# catalog-date 2010-07-29 16:44:20 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-pst-optic
Version:	1.01
Release:	9
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 755391
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 719375
- texlive-pst-optic
- texlive-pst-optic
- texlive-pst-optic
- texlive-pst-optic

