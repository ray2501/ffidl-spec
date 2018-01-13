Summary: Extension for Calling C Libraries from Tcl
Name: ffidl
Version: 0.7
Release: 1
License: BSD
Group: Development/Libraries/Tcl
BuildRequires: tcl-devel >= 8.6
BuildRequires: libffi-devel
Requires: tcl >= 8.6
URL: https://github.com/prs-de/ffidl
Source0: %{name}.tar.bz2
Patch0: ffidl.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ffidl allows you to define Tcl/Tk extensions with pure Tcl wrappers
calling any shared library installed on your system, including the Tcl
and Tk core libraries.

%prep
%setup -q -n %name
%patch0

%build
autoconf
./configure \
	--with-tcl=%_libdir \
	--libdir=%tcl_archdir \
	--enable-libffi=system \
	--enable-stubs \
	--enable-callbacks
make
find -name '*.tcl' |
     xargs sed -i 's,/usr/local/bin/tclsh8.2,/usr/bin/tclsh,'

%check
make test

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt doc/* license.terms demos
%tcl_archdir/*


%changelog
* Mon Aug  3 2009 Reinhard Max <max@suse.de> - 0.6-1
- Fix path to tclsh in demo scripts
- Move "make test" to %check section

* Tue Jul 22 2008 Reinhard Max <max@suse.de> - 
- Initial build.


