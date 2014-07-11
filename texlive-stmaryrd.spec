# revision 22027
# category Package
# catalog-ctan /fonts/stmaryrd
# catalog-date 2009-10-10 00:51:28 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-stmaryrd
Version:	20110409
Release:	3
Summary:	St Mary Road symbols for theoretical computer science
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/stmaryrd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stmaryrd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stmaryrd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stmaryrd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts were originally distributed as MetaFont sources only,
but Adobe Type 1 versions are also now available. Macro support
is provided for use under LaTeX; the package supports the
"only" option (provided by the somedefs package) to restrict
what is loaded, for those who don't need the whole font.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/stmaryrd/stmary10.afm
%{_texmfdistdir}/fonts/afm/public/stmaryrd/stmary5.afm
%{_texmfdistdir}/fonts/afm/public/stmaryrd/stmary6.afm
%{_texmfdistdir}/fonts/afm/public/stmaryrd/stmary7.afm
%{_texmfdistdir}/fonts/afm/public/stmaryrd/stmary8.afm
%{_texmfdistdir}/fonts/afm/public/stmaryrd/stmary9.afm
%{_texmfdistdir}/fonts/map/dvips/stmaryrd/stmaryrd.map
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmary10.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmary5.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmary6.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmary7.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmary8.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmary9.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmaryaj.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmaryba.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmarych.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmaryjg.mf
%{_texmfdistdir}/fonts/source/public/stmaryrd/stmaryrd.mf
%{_texmfdistdir}/fonts/tfm/public/stmaryrd/stmary10.tfm
%{_texmfdistdir}/fonts/tfm/public/stmaryrd/stmary5.tfm
%{_texmfdistdir}/fonts/tfm/public/stmaryrd/stmary6.tfm
%{_texmfdistdir}/fonts/tfm/public/stmaryrd/stmary7.tfm
%{_texmfdistdir}/fonts/tfm/public/stmaryrd/stmary8.tfm
%{_texmfdistdir}/fonts/tfm/public/stmaryrd/stmary9.tfm
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary10.pfb
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary10.pfm
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary5.pfb
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary5.pfm
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary6.pfb
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary6.pfm
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary7.pfb
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary7.pfm
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary8.pfb
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary8.pfm
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary9.pfb
%{_texmfdistdir}/fonts/type1/public/stmaryrd/stmary9.pfm
%{_texmfdistdir}/tex/latex/stmaryrd/Ustmry.fd
%{_texmfdistdir}/tex/latex/stmaryrd/stmaryrd.sty
%doc %{_texmfdistdir}/doc/fonts/stmaryrd/INSTALL
%doc %{_texmfdistdir}/doc/fonts/stmaryrd/README
%doc %{_texmfdistdir}/doc/fonts/stmaryrd/README.hoekwater
%doc %{_texmfdistdir}/doc/fonts/stmaryrd/stmaryrd.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/stmaryrd/stmaryrd.dtx
%doc %{_texmfdistdir}/source/fonts/stmaryrd/stmaryrd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
