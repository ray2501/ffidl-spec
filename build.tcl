#!/usr/bin/tclsh

set arch "x86_64"
set base "ffidl"

if {[file exists $base]} {
    file delete -force $base
}

set var [list git clone https://github.com/prs-de/ffidl.git $base]
exec >@stdout 2>@stderr {*}$var

if {[file exists $base]} {
    file delete -force $base/.git
}

set var2 [list tar cjvf ${base}.tar.bz2 $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.bz2 build/SOURCES
file copy -force ffidl.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb ffidl.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete -force $base.tar.bz2

