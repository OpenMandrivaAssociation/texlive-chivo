%global tl_name chivo
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Using the free Chivo fonts with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/chivo
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chivo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chivo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chivo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This work provides the necessary files to use the Chivo fonts with
LaTeX. Chivo is a set of eight fonts provided by Hector Gatti & Omnibus
Team under the Open Font License (OFL), version 1.1. The fonts are
copyright (c) 2011-2019, Omnibus-Type.

