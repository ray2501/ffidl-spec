Summary: Extension for Calling C Libraries from Tcl
Name: ffidl
Version: 0.8b0
Release: 1
License: BSD
Group: Development/Libraries/Tcl
BuildRequires: autoconf
BuildRequires: tcl-devel >= 8.6
BuildRequires: libffi-devel
Requires: tcl >= 8.6
URL: https://github.com/prs-de/ffidl
Source0: %{name}-%{version}.tar.gz
Patch0:  ffidl.c.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ffidl allows you to define Tcl/Tk extensions with pure Tcl wrappers
calling any shared library installed on your system, including the Tcl
and Tk core libraries.

%prep
%setup -q -n %name-%version
%patch0

%build
autoconf
./configure \
    --enable-64bit \
	--with-tcl=%_libdir \
	--libdir=%tcl_archdir \
	--with-libffi \
    --enable-libffi-static=no \
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


