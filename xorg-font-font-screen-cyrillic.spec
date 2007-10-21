Summary:	Screen Fixed Cyrillic font
Summary(pl.UTF-8):	Font Screen Fixed w cyrylicy
Name:		xorg-font-font-screen-cyrillic
Version:	1.0.1
Release:	3
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
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Screen Fixed Cyrillic font.

%description -l pl.UTF-8
Font Screen Fixed w cyrylicy.

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

# fonts.scale bogus, fonts.dir generated in post
rm -f $RPM_BUILD_ROOT%{_fontsdir}/cyrillic/fonts.{dir,scale}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst cyrillic

%postun
fontpostinst cyrillic

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/cyrillic/screen*.pcf.gz
