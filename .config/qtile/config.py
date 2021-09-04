# -*- coding: utf-8 -*-

# Import Standard Library
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# Config depandency library
from os import getenv
import subprocess

mod = "mod4"            # Windows key as mod key
home = getenv("HOME")   # Set Home directory
terminal = "alacritty"      # Set terminal emulator
shell = " -e fish"      # Set Shell

keys = [
    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma",
        lazy.prev_screen(), desc='Move focus to prev monitor'),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or up/down
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h",
        lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n",
        lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Window view control
    Key([mod], "m",
        lazy.layout.maximize(), desc='toggle window size minimum and maximum'),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Essential control keys
    Key([mod], "w",
        lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r",
        lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q",
        lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r",
        lazy.spawncmd(),desc="Spawn a command using a prompt widget"),
    # Special Key
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("xbacklight -inc 5"), desc="BrightnessUp"),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("xbacklight -dec 5"), desc="BrightnessDown"),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+"), desc="RaiseVolume"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%-"), desc="LowerVolume"),
    Key([], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle"), desc="LowerVolume"),
    
    # Shutdown script
    Key([mod, "control"], "e",
        lazy.spawn(home+"/.config/bin/shutdown.sh"), desc="Shutdown Prompt with dmenu"),

    # Launch Terminal
    Key([mod], "Return",
        lazy.spawn(terminal+shell), desc="Launch terminal"),

    # Launch dmenu
    Key([mod, "shift"],"Return",
        lazy.spawn("dmenu_run -p 'Run:'"), desc="Run dmenu"),
    
    # Change Scaling Governor
    Key([mod, "shift"],"g",
        lazy.spawn(home+"/.config/bin/chane-governor.sh"), desc="Scaling Governor"),

    # Start Stop On Demand Services
    Key([mod, "shift"],"s",
        lazy.spawn(home+"/.config/bin/services.sh"), desc="On Demand Services"),

]

groups = [Group(i, label="⊚") for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Colors set for theme
colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens

widget_defaults = dict(
    font='sans',
    fontsize=13,
    padding=0,
    background = "#212B30"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 2,
                    foreground = "#3A4449",
                    background = "#3A4449"
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i1.png',
                    background = "#353F44",
                    margin = 0
                ),
                widget.GroupBox(
                    background = "#353F44",
                    fontsize = 17,
                    highlight_method = 'block',
                    inactive = "#4DD0E1",
                    active = "#00B0FF",
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i2.png',
                    background = "#303A3F",
                    margin = 0
                ),
                widget.CPU(
                    format = '{load_percent}%',
                    background = "#303A3F",
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i3.png',
                    background = "#2B353A",
                    margin = 0
                ),
                widget.Memory(
                    format = '{MemUsed:.0f}{mm}',
                    background = "#2B353A",
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i4.png',
                    background = "#263035",
                    margin = 0
                ),
                widget.ThermalSensor(
                    background = "#263035",
                    tag_sensor = "Package id 0"
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i5.png',
                    background = "#212B30",
                    margin = 0
                ),
                widget.Prompt(background = "#212B30"),
                widget.WindowName(background = "#212B30"),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i6.png',
                    background = "#263035",
                    margin = 0
                ),
                widget.Backlight(
                    backlight_name='intel_backlight',
                    background = "#263035"
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i5.png',
                    background = "#2B353A",
                    margin = 0
                ),
                widget.Volume(
                    background = "#2B353A"
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i4.png',
                    background = "#303A3F",
                    margin = 0
                ),
                widget.Wlan(
                    interface='wlp2s0',
                    background = "#303A3F"
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i3.png',
                    background = "#353F44",
                    margin = 0
                ),
                widget.Battery(
                    update_interval=1,
                    format='{percent:2.0%}',
                    background = "#353F44"
                ),
                widget.BatteryIcon(
                    update_interval=1,
                    theme_path= '/home/black/.config/qtile/src/bat',
                    background = "#353F44"
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i2.png',
                    background = "#3A4449",
                    margin = 0
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background = "#3A4449"
                ),
                widget.Image(
                    filename = '/home/black/.config/qtile/src/sep/i1.png',
                    background = "#3F494E",
                    margin = 0
                ),
                widget.Systray(background="#3F494E"),
            ],
            26,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='xdman-Main'), # XDM
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Startup Hook
@hook.subscribe.startup_once
def autostart():
    subprocess.call([home+"/.config/qtile/autostart.sh"])

wmname = "LG3D"
