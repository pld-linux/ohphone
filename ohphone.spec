Summary:	Initiate, or receive, a H.323 IP telephony call
Summary(pl.UTF-8):   Inicjowanie i odbieranie połączeń telefonicznych H.323
Name:		ohphone
Version:	1.13.5
%define fver	%(echo %{version} | tr . _)
Release:	1
License:	MPL 1.0
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src.tar.gz
# Source0-md5:	755677eb1e6196b6d5e5b4560232dc1f
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-mak_files.patch
Patch2:		%{name}-novga.patch
URL:		http://www.openh323.org/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	openh323-devel >= 1.15
BuildRequires:	pwlib-devel >= 1.8
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ohphone is a command line application that can be used to listen for
incoming H.323 calls, or to initiate a call to a remote host. Although
originally intended as a test harneess for the OpenH323 project (see
http://www.openh323.org/) it has developed into a fully functional
H.323 endpoint application.

%description -l pl.UTF-8
ohphone to działająca z linii poleceń aplikacja, która może czekać na
nadchodzące połączenia H.323 lub inicjować połączenia z innym
komputerem. Oryginalnie miało to być narzędzie testowe dla projektu
OpenH323 (http://www.openh323.org/), ale zostało doprowadzone do
pełnej funkcjonalności.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	CXX="%{__cxx}" \
	OPTCCFLAGS="%{rpmcflags} -fno-exceptions" \
	XLIBDIR="/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
