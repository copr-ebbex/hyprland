Name:           hyprland
Version:        0.55.4
Release:        %autorelease
Summary:        Dynamic tiling Wayland compositor that doesn't sacrifice on its looks

# hyprland: BSD-3-Clause
# ./subprojects/udis86: BSD-2-Clause
# ./protocols/kde-server-decoration.xml: LGPL-2.1-or-later
# ./protocols/wayland-drm.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-data-control-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-gamma-control-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-output-management-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/frog-color-management-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/xx-color-management-v4.xml: HPND-sell-variant and/or ntp_disclaimer
License:        BSD-3-Clause AND BSD-2-Clause AND LGPL-2.1-or-later AND HPND-sell-variant AND MIT
URL:            https://github.com/hyprwm/Hyprland
%global glaze_version 7.2.0
Source0:        %{url}/releases/download/v%{version}/source-v%{version}.tar.gz
Source1:        https://github.com/stephenberry/glaze/archive/refs/tags/v%{glaze_version}.tar.gz#/glaze-%{glaze_version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  python3

BuildRequires:  cmake(glslang)
BuildRequires:  cmake(hyprwayland-scanner) >= 0.3.10

BuildRequires:  pkgconfig(aquamarine) >= 0.9.3
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(hyprcursor) >= 0.1.7
BuildRequires:  pkgconfig(hyprgraphics) >= 0.5.1
BuildRequires:  pkgconfig(hyprland-protocols) >= 0.6.4
BuildRequires:  pkgconfig(hyprlang) >= 0.6.7
BuildRequires:  pkgconfig(hyprutils) >= 0.13.1
BuildRequires:  pkgconfig(hyprwire)
BuildRequires:  cmake(hyprwire-scanner)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.28
BuildRequires:  pkgconfig(muparser)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.47
BuildRequires:  pkgconfig(wayland-server) >= 1.22.91
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon) >= 1.11.0
BuildRequires:  pkgconfig(lua) >= 5.5

# udis86 is packaged in Fedora, but the copy bundled here is actually a
# modified fork.
Provides:       bundled(udis86) = 1.7.2^1.git5336633
Provides:       bundled(glaze) = %{glaze_version}

Requires:       xorg-x11-server-Xwayland%{?_isa}
Requires:       xdg-desktop-portal%{?_isa}
Requires:       aquamarine%{?_isa} >= 0.9.3
Requires:       hyprcursor%{?_isa} >= 0.1.7
Requires:       hyprutils%{?_isa} >= 0.13.1
Requires:       hyprgraphics%{?_isa} >= 0.5.1

# Used in the default configuration
Recommends:     kitty
Recommends:     wofi
Recommends:     playerctl
Recommends:     brightnessctl
# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Logind needs polkit to create a graphical session
Recommends:     polkit

Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

%description
Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice
on its looks. It supports multiple layouts, fancy effects, has a
very flexible IPC model allowing for a lot of customization, a powerful
plugin system and more.

%package        devel
Summary:        Meta package to install dependencies for hyprpm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       cpio
Requires:       gcc-c++
Requires:       cmake(glslang)
Requires:       cmake(hyprwayland-scanner) >= 0.3.10
Requires:       pkgconfig(aquamarine) >= 0.9.3
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(hyprcursor) >= 0.1.7
Requires:       pkgconfig(hyprgraphics) >= 0.5.1
Requires:       pkgconfig(hyprland-protocols) >= 0.6.4
Requires:       pkgconfig(hyprlang) >= 0.6.7
Requires:       pkgconfig(hyprutils) >= 0.13.1
Requires:       pkgconfig(lcms2)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libinput) >= 1.28
Requires:       pkgconfig(muparser)
Requires:       pkgconfig(pango)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(re2)
Requires:       pkgconfig(uuid)
Requires:       pkgconfig(wayland-protocols) >= 1.47
Requires:       pkgconfig(wayland-server) >= 1.22.91
Requires:       pkgconfig(xcb-composite)
Requires:       pkgconfig(xcb-errors)
Requires:       pkgconfig(xcb-icccm)
Requires:       pkgconfig(xcb-render)
Requires:       pkgconfig(xcb-res)
Requires:       pkgconfig(xcb-xfixes)
Requires:       pkgconfig(xcb)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xkbcommon) >= 1.11.0
Requires:       pkgconfig(lua) >= 5.5
Recommends:     git-core

%description    devel
%{summary}.


%prep
%autosetup -n %{name}-source -p1
rm -rf subprojects/{tracy,hyprland-protocols}

cp -p subprojects/udis86/LICENSE LICENSE-udis86

# -Wpedantic causes GCC to error on zero-length VTable arrays generated
# by hyprwayland-scanner; can't use build flags because CMake appends
# after RPM optflags
sed -i 's/-Wpedantic//' CMakeLists.txt

# Build glaze (header-only) and install to local prefix
tar xf %{SOURCE1}
cmake -S glaze-%{glaze_version} -B glaze-build \
    -DCMAKE_INSTALL_PREFIX=%{_builddir}/glaze-install \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF \
    -Dglaze_INSTALL=ON
cmake --install glaze-build

cp -p glaze-%{glaze_version}/LICENSE LICENSE-glaze


%build
%cmake -Dglaze_DIR=%{_builddir}/glaze-install/share/glaze
%cmake_build


%install
%cmake_install


%files
%license LICENSE LICENSE-udis86 LICENSE-glaze
%{_bindir}/hyprctl
%{_bindir}/Hyprland
%{_bindir}/hyprland
%{_bindir}/hyprpm
%{_bindir}/start-hyprland
%{_datadir}/hypr/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/wayland-sessions/%{name}-uwsm.desktop
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_mandir}/man1/hyprctl.1*
%{_mandir}/man1/Hyprland.1*
%{bash_completions_dir}/hypr*
%{fish_completions_dir}/hypr*.fish
%{zsh_completions_dir}/_hypr*

%files devel
%{_datadir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/


%changelog
%autochangelog
