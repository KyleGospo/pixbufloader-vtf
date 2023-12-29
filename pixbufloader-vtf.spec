Name:       pixbufloader-vtf
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    Load Valve Texture Files in Gtk+ applications

License:    LGPLv2.1
URL:        https://github.com/panzi/pixbufloader-vtf
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

Requires:   VTFLib

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: g++
Buildrequires: VTFLib-devel
BuildRequires: pkgconfig(VTFLib)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)

# Disable debug packages
%define debug_package %{nil}

%description
GDK PixBuf plugin to load Valve Texture Files (read-only). Using this you will be able to view VTF files in Gtk+ programs like Eye of GNOME.

%prep
{{{ git_dir_setup_macro }}}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license LGPL.txt
%doc README.md
%{_libdir}/gdk-pixbuf-*/*/loaders/libpixbufloader-vtf.so
