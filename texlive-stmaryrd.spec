%global tl_name stmaryrd
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	St Mary Road symbols for theoretical computer science
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/stmaryrd
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stmaryrd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stmaryrd.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stmaryrd.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts were originally distributed as Metafont sources only, but
Adobe Type 1 versions are also now available. Macro support is provided
for use under LaTeX; the package supports the "only" option (provided by
the somedefs package) to restrict what is loaded, for those who don't
need the whole font.

