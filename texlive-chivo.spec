Name:		texlive-chivo
Version:	65029
Release:	1
Summary:	Using the free Chivo fonts with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chivo
License:	ofl lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chivo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chivo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chivo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This work provides the necessary files to use the Chivo fonts
with LaTeX. Chivo is a set of eight fonts provided by Hector
Gatti & Omnibus Team under the Open Font License
[(OFL)](http://scripts.sil.org/OFL), version 1.1. The fonts are
copyright (c) 2011-2019, Omnibus-Type.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/chivo
%{_texmfdistdir}/tex/latex/chivo
%{_texmfdistdir}/fonts/vf/public/chivo
%{_texmfdistdir}/fonts/type1/public/chivo
%{_texmfdistdir}/fonts/tfm/public/chivo
%{_texmfdistdir}/fonts/opentype/public/chivo
%{_texmfdistdir}/fonts/map/dvips/chivo
%{_texmfdistdir}/fonts/enc/dvips/chivo
%doc %{_texmfdistdir}/doc/fonts/chivo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
