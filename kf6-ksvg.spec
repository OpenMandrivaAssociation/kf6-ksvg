%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Svg
%define devname %mklibname KF6Svg -d
#define git 20240217

Name: kf6-ksvg
Version: 6.8.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/ksvg/-/archive/master/ksvg-master.tar.bz2#/ksvg-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/ksvg-%{version}.tar.xz 
%endif
Summary: Components for handling SVGs
URL: https://invent.kde.org/frameworks/ksvg
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xscrnsaver)
Requires: %{libname} = %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Components for handling SVGs

%package -n %{libname}
Summary: Components for handling SVGs
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Components for handling SVGs

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Components for handling SVGs

%files
%{_datadir}/qlogging-categories6/ksvg.*
%{_libdir}/qt6/qml/org/kde/ksvg

%files -n %{devname}
%{_includedir}/KF6/KSvg
%{_libdir}/cmake/KF6Svg
%{_qtdir}/doc/KF6Svg.*

%files -n %{libname}
%{_libdir}/libKF6Svg.so*
