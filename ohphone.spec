Summary:	Initiate, or receive, a H.323 IP telephony call
Summary(pl):	Inicjowanie i odbieranie po��cze� telefonicznych H.323
Name:		ohphone
Version:	1.3.7
Release:	1.1
License:	MPL 1.0
Group:		Applications/Communications
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	eba2fe0f7eb2d68d57a89b65e3736042
Patch0:		%{name}-mak_files.patch
Patch1:		%{name}-novga.patch
Patch2:		%{name}-update.patch
URL:		http://www.openh323.org/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	openh323-devel >= 1.12.0
BuildRequires:	pwlib-devel >= 1.5.0
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ohphone is a command line application that can be used to listen for
incoming H.323 calls, or to initiate a call to a remote host. Although
originally intended as a test harneess for the OpenH323 project (see
http://www.openh323.org/) it has developed into a fully functional
H.323 endpoint application.

%description -l pl
ohphone to dzia�aj�ca z linii polece� aplikacja, kt�ra mo�e czeka� na
nadchodz�ce po��czenia H.323 lub inicjowa� po��czenia z innym
komputerem. Oryginalnie mia�o to by� narz�dzie testowe dla projektu
OpenH323 (http://www.openh323.org/), ale zosta�o doprowadzone do
pe�nej funkcjonalno�ci.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

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
