Summary:	screen-cyrillic font
Summary(pl):	Font screen-cyrillic
Name:		xorg-font-font-screen-cyrillic
Version:	1.0.1
Release:	0.2
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-screen-cyrillic-%{version}.tar.bz2
# Source0-md5:	c8d5aef01c906c7aaea329702a8b1b63
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/cyrillic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
screen-cyrillic font.

%description -l pl
Font screen-cyrillic.

%prep
%setup -q -n font-screen-cyrillic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/cyrillic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_fontsdir}/cyrillic
mv fonts.scale fonts.scale.screen-cyrillic

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst cyrillic

%postun
fontpostinst cyrillic

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/cyrillic/*.gz
%{_fontsdir}/cyrillic/*.scale.*
# conflict with xorg-font-font-winitzki-cyrillic
#%ghost %{_fontsdir}/cyrillic/*.dir
