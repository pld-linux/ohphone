Summary:	initiate, or receive, a H.323 IP telephony call
Summary(pl):	Inicjowanie i odbieranie po³±czeñ telefonicznych H.323
Name:		ohphone
Version:	1.2.7
Release:	1
License:	MPL
Group:		Applications/Communications
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
Patch0:		%{name}-mak_files.patch
Patch1:		%{name}-novga.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel
BuildRequires:	pwlib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ohphone is a command line application that can be used to listen for
incoming H.323 calls, or to initiate a call to a remote host. Although
originally intended as a test harneess for the OpenH323 project (see
http://www.openh323.org/) it has developed into a fully functional
H.323 endpoint application.

%description -l pl
ohphone to dzia³aj±ca z linii poleceñ aplikacja, która mo¿e czekaæ na
nadchodz±ce po³±czenia H.323 lub inicjowaæ po³±czenia z innym
komputerem. Oryginalnie mia³o to byæ narzêdzie testowe dla projektu
OpenH323 (http://www.openh323.org/), ale zosta³o doprowadzone do
pe³nej funkcjonalno¶ci.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	OPTCCFLAGS="%{!?debug:$RPM_OPT_FLAGS}  -fno-rtti -fno-exceptions"

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
