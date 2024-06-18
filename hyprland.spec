Name:           hyprland
Version:        0.39.1
Release:        %autorelease
Summary:        Dynamic tiling Wayland compositor that doesn't sacrifice on its looks

# hyprland: BSD-3-Clause
# subprojects/hyprland-protocols: BSD-3-Clause
# subprojects/wlroots-hyprland: MIT
# subproject/udis86: BSD-2-Clause
# protocols/ext-workspace-unstable-v1.xml: HPND-sell-variant
# protocols/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant
# protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant
# protocols/idle.xml: LGPL-2.1-or-later
License:        BSD-3-Clause AND MIT AND BSD-2-Clause AND HPND-sell-variant AND LGPL-2.1-or-later
URL:            https://github.com/hyprwm/Hyprland
Source:         %{url}/releases/download/v%{version}/source-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  jq
BuildRequires:  meson

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprcursor)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.23.0
BuildRequires:  pkgconfig(libliftoff) >= 0.4.1
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22.0
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

# Upstream insists on always building against very current snapshots of
# wlroots, and doesn't provide a method for building against a system copy.
# https://github.com/hyprwm/Hyprland/issues/302
Provides:       bundled(wlroots-hyprland) = 0.18.0~1.git611a4f2

# udis86 is packaged in Fedora, but the copy bundled here is actually a
# modified fork.
Provides:       bundled(udis86) = 1.7.2^1.git5336633

Requires:       xorg-x11-server-Xwayland%{?_isa}
Requires:       xdg-desktop-portal%{?_isa}
Requires:       libdrm%{?_isa} >= 2.4.120
Requires:       hyprcursor%{?_isa} >= 0.1.7

# Both are used in the default configuration
Recommends:     kitty
Recommends:     wofi
# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Logind needs polkit to create a graphical session
Recommends:     polkit

Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots that doesn't
sacrifice on its looks. It supports multiple layouts, fancy effects, has a
very flexible IPC model allowing for a lot of customization, a powerful
plugin system and more.

%package        devel
Summary:        Meta package to install dependencies for hyprpm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       cpio
Requires:       meson
Requires:       ninja-build
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(hwdata)
Requires:       pkgconfig(hyprlang)
Requires:       pkgconfig(libdisplay-info)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libinput) >= 1.23.0
Requires:       pkgconfig(libliftoff) >= 0.4.1
Requires:       pkgconfig(libseat)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(pango)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(pixman-1) >= 0.42.0
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-scanner)
Requires:       pkgconfig(wayland-server) >= 1.22.0
Requires:       pkgconfig(xcb-composite)
Requires:       pkgconfig(xcb-dri3)
Requires:       pkgconfig(xcb-ewmh)
Requires:       pkgconfig(xcb-icccm)
Requires:       pkgconfig(xcb-present)
Requires:       pkgconfig(xcb-render)
Requires:       pkgconfig(xcb-renderutil)
Requires:       pkgconfig(xcb-res)
Requires:       pkgconfig(xcb-shm)
Requires:       pkgconfig(xcb-util)
Requires:       pkgconfig(xcb-xfixes)
Requires:       pkgconfig(xcb-xinput)
Requires:       pkgconfig(xcb)
Requires:       pkgconfig(xkbcommon)
Requires:       pkgconfig(xwayland)
Recommends:     git-core

%description    devel
%{summary}.


%prep
%autosetup -n %{name}-source -p1
rm -rf subprojects/{tracy,hyprland-protocols}

cp -p subprojects/udis86/LICENSE LICENSE-udis86
cp -p subprojects/wlroots-hyprland/LICENSE LICENSE-wlroots


%build
%meson \
       -Dwlroots-hyprland:examples=false \
       -Dwlroots-hyprland:xcb-errors=disabled \
       -Dwlroots-hyprland:werror=false
%meson_build


%install
%meson_install --skip-subprojects wlroots-hyprland
mkdir -p %{buildroot}%{bash_completions_dir}
mv %{buildroot}%{_datadir}/bash-completion/hyprctl %{buildroot}%{bash_completions_dir}/hyprctl
mv %{buildroot}%{_datadir}/bash-completion/hyprpm %{buildroot}%{bash_completions_dir}/hyprpm
rm -rf %{buildroot}%{_includedir}/%{name}
rm -rf %{buildroot}%{_datadir}/pkgconfig/%{name}.pc


%files
%license LICENSE LICENSE-udis86 LICENSE-wlroots
%{_bindir}/hyprctl
%{_bindir}/Hyprland
%{_bindir}/hyprpm
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_mandir}/man1/hyprctl.1*
%{_mandir}/man1/Hyprland.1*
%{bash_completions_dir}/hypr*
%{fish_completions_dir}/hypr*.fish
%{zsh_completions_dir}/_hypr*

%files devel


%changelog
%autochangelog
