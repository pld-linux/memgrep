Summary:	Search, replace or dump memory from running apps and core files
Summary(pl):	Przeszukiwanie, modyfikacja lub zrzucanie pami�ci z aplikacji lub plik�w core
Name:		memgrep
Version:	0.8.0
Release:	1
License:	unknown
Group:		Applications
Source0:	http://www.hick.org/code/skape/memgrep/%{name}-%{version}.tar.gz
# Source0-md5:	b52da1eb88313206fd8ced1db9df1830
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
memgrep is a tool to search, replace, or dump arbitrary memory from
running applications and core files. Potential applications for
memgrep include reverse engineering, debugging, and vulnerability
assessment.

%description -l pl
memgrep to narz�dzie do przeszukiwania, modyfikowania lub zrzucania
zawarto�ci pami�ci z dzia�aj�cych aplikacji lub plik�w core.
Potencjalne zastosowania memgrepa obejmuj� reverse engineering,
odpluskwianie oraz szacowanie dziur.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
