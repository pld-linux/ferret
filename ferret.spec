Summary:	FERRET - a broadcast analysis tool
#Summary(pl.UTF-8):	-
Name:		ferret
Version:	1.1
Release:	2
License:	"all rights reserved"
Group:		Applications
Source0:	http://www.erratasec.com/Ferret-1_1.zip
# NoSource0-md5:	f9fbd4eb5eb178589584a59052b35d02
Patch0:		radiotap.patch
URL:		http://www.erratasec.com/ferret.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool gathers information broadcast by machines on the local
network The little bits of information can then be used together to
put together a picture of the user, the computer, and the internal
network where that machine comes from.

#%description -l pl.UTF-8
#TODO

%prep
%setup -q -n Ferret
%patch0 -p1
rm -rf bin/*/ bin/ferret tmp/*

%build
%{__make} -C build/linux-x86-gcc4

%install
rm -rf $RPM_BUILD_ROOT
install -D bin/ferret      $RPM_BUILD_ROOT%{_bindir}/ferret
install -D bin/ferret.conf $RPM_BUILD_ROOT%{_sysconfdir}/ferret.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.py
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*.conf
