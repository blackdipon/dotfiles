#!/usr/bin/env bash

# Touchpad
xinput set-prop 12 "libinput Tapping Enabled" 1
xinput set-prop 12 "libinput Natural Scrolling Enabled" 1

# Polkit
lxpolkit &

# Picom
picom -CGb

# Wallpaper
feh --bg-scale /usr/share/backgrounds/Arch-Wallpaper.jpg
