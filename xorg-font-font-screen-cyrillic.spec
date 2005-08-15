# $Rev: 3216 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-screen-cyrillic
Summary(pl):	font-screen-cyrillic
Name:		xorg-font-font-screen-cyrillic
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-screen-cyrillic-%{version}.tar.bz2
# Source0-md5:	8b50c5570076d96c15911a4f8268ca7d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-screen-cyrillic-%{version}-root-%(id -u -n)

%description
font-screen-cyrillic

%description -l pl
font-screen-cyrillic


%prep
%setup -q -n font-screen-cyrillic-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/cyrillic/*
