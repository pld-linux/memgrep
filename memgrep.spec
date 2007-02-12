Summary:	Search, replace or dump memory from running apps and core files
Summary(pl.UTF-8):   Przeszukiwanie, modyfikacja lub zrzucanie pamięci z aplikacji lub plików core
Name:		memgrep
Version:	0.8.0
Release:	1
License:	unknown
Group:		Applications
Source0:	http://www.hick.org/code/skape/memgrep/%{name}-%{version}.tar.gz
# Source0-md5:	b52da1eb88313206fd8ced1db9df1830
Patch0:		%{name}-linux.patch
URL:		http://www.uninformed.org/main.pl?action=codeView&codeId=19
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
memgrep is a tool to search, replace, or dump arbitrary memory from
running applications and core files. Potential applications for
memgrep include reverse engineering, debugging, and vulnerability
assessment.

%description -l pl.UTF-8
memgrep to narzędzie do przeszukiwania, modyfikowania lub zrzucania
zawartości pamięci z działających aplikacji lub plików core.
Potencjalne zastosowania memgrepa obejmują reverse engineering,
odpluskwianie oraz szacowanie dziur.

%package devel
Summary:	Header file for memgrep library
Summary(pl.UTF-8):   Plik nagłówkowy biblioteki memgrep
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for memgrep library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki memgrep.

%package static
Summary:	Static memgrep library
Summary(pl.UTF-8):   Statyczna biblioteka memgrep
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static memgrep library.

%description static -l pl.UTF-8
Statyczna biblioteka memgrep.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags} -I`pwd`/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install memgrep $RPM_BUILD_ROOT%{_bindir}
install *.so *.a $RPM_BUILD_ROOT%{_libdir}
install include/memgrep.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/memgrep
%attr(755,root,root) %{_libdir}/heaplist.so
%attr(755,root,root) %{_libdir}/libmemgrep.so

%files devel
%defattr(644,root,root,755)
%doc docs/html/*.{css,html,png}
%{_includedir}/memgrep.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmemgrep.a
