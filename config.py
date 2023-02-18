from libqtile import bar, hook, layout, widget
from libqtile.config import Group, Key, Match, Screen
from libqtile.dgroups import simple_key_binder
from libqtile.lazy import lazy

import os
import subprocess

# ---------------------------------------------------------
# --- QTile Colors
# ---------------------------------------------------------

MOCHA_COLOR = {
    "WINDOW_BORDER_FOCUS": "#F5E0DC",
    "WINDOW_BORDER_NORMAL": "#313244",
    "TOP_BAR_BORDER": "#313244",
    "BACKGROUND": "#1E1E2E",
    "FOREGROUND": "#CDD6F4",
    "RED": "#F38BA8",
    "GREEN": "#A6E3A1",
    "YELLOW": "#F9E2AF",
    "BLUE": "#89B4FA",
    "MAGENTA": "#CBA6F7",
    "CYAN": "#89DCEB",
}

# ---------------------------------------------------------
# --- QTile Constants
# ---------------------------------------------------------

COLORS = dict(MOCHA_COLOR)

MOD = "mod4"

BORDER = 2
MARGIN = 4
PADDING = 8

FONT = "Cascadia Code"
FONT_SIZE = 14

# ---------------------------------------------------------
# --- QTile Hooks
# ---------------------------------------------------------


@hook.subscribe.startup_once
def startup_once():
    subprocess.call([os.path.expanduser("~/.config/qtile/assets/scripts/startup.sh")])


# ---------------------------------------------------------
# --- QTile Definitions
# ---------------------------------------------------------


def qtile_auto_fullscreen():
    return False


def qtile_groups():
    return [Group(i, layout="max") for i in "1234567890"]


def qtile_key_binder():
    return simple_key_binder(MOD)


def qtile_widgets_default():
    return dict(
        background=COLORS["BACKGROUND"],
        font=FONT,
        fontsize=FONT_SIZE,
    )


def qtile_extension_defaults():
    return qtile_widgets_default()


def qtile_floating_layout():
    return layout.Floating(
        border_focus=COLORS["WINDOW_BORDER_FOCUS"],
        border_normal=COLORS["WINDOW_BORDER_NORMAL"],
        border_width=BORDER,
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(title="branchdialog"),
            Match(title="pinentry"),
            Match(title="splash"),
            Match(title="win0"),
            Match(wm_class="confirmreset"),
            Match(wm_class="makebranch"),
            Match(wm_class="maketag"),
            Match(wm_class="ssh-askpass"),
        ],
    )


def qtile_focus_on_window_activation():
    return "Focus"


def qtile_layouts():
    return [
        layout.Max(
            border_focus=COLORS["WINDOW_BORDER_FOCUS"],
            border_normal=COLORS["WINDOW_BORDER_NORMAL"],
        ),
        layout.Columns(
            border_focus=COLORS["WINDOW_BORDER_FOCUS"],
            border_focus_stack=COLORS["WINDOW_BORDER_FOCUS"],
            border_normal=COLORS["WINDOW_BORDER_NORMAL"],
            border_normal_stack=COLORS["WINDOW_BORDER_NORMAL"],
            border_on_single=True,
            margin_on_single=[MARGIN, MARGIN, MARGIN, MARGIN],
            border_width=BORDER,
            margin=MARGIN,
        ),
    ]


def qtile_widgets_bar():
    return [
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
        widget.Spacer(
            foreground=COLORS["TOP_BAR_BORDER"],
            length=PADDING,
        ),
        widget.AGroupBox(
            foreground=COLORS["FOREGROUND"],
            padding=0,
            margin_y=4,
            margin_x=0,
            borderwidth=0,
        ),
        widget.Spacer(
            foreground=COLORS["TOP_BAR_BORDER"],
            length=PADDING,
        ),
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
        widget.Prompt(
            foreground=COLORS["FOREGROUND"],
            padding=PADDING,
            cursor=True,
            cursor_color=COLORS["FOREGROUND"],
            prompt="",
            record_history=False,
            markup=False,
        ),
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
        widget.Spacer(
            foreground=COLORS["TOP_BAR_BORDER"],
        ),
        widget.WindowCount(
            foreground=COLORS["FOREGROUND"],
            padding=PADDING,
        ),
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
        widget.KeyboardLayout(
            foreground=COLORS["MAGENTA"],
            padding=PADDING,
            configured_keyboards=["us", "br"],
        ),
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
        widget.Volume(
            foreground=COLORS["YELLOW"],
            padding=PADDING,
        ),
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
        widget.Clock(
            foreground=COLORS["BLUE"],
            padding=PADDING,
            format="%Y-%m-%d %I:%M:%S %p",
        ),
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
        widget.QuickExit(
            foreground=COLORS["RED"],
            padding=PADDING,
            countdown_format="[ {} SECs ]",
            default_text="[  EXIT  ]",
        ),
        widget.Sep(
            foreground=COLORS["TOP_BAR_BORDER"],
            padding=PADDING,
            size_percent=100,
            linewidth=BORDER,
        ),
    ]


def qtile_screens():
    return [
        Screen(
            wallpaper="~/.config/qtile/assets/images/"
            + COLORS["BACKGROUND"][1:]
            + ".jpeg",
            wallpaper_mode="fill",
            top=bar.Bar(
                qtile_widgets_bar(),
                (32 - BORDER),
                border_color=COLORS["TOP_BAR_BORDER"],
                border_width=[0, 0, BORDER, 0],
            ),
        ),
    ]


def qtile_keys():
    return [
        Key([MOD, "shift"], "h", lazy.layout.shuffle_left()),
        Key([MOD, "shift"], "l", lazy.layout.shuffle_right()),
        Key([MOD, "shift"], "j", lazy.layout.shuffle_down()),
        Key([MOD, "shift"], "k", lazy.layout.shuffle_up()),
        Key([MOD], "h", lazy.layout.left()),
        Key([MOD], "l", lazy.layout.right()),
        Key([MOD], "j", lazy.layout.down()),
        Key([MOD], "k", lazy.layout.up()),
        Key([MOD, "control"], "n", lazy.layout.normalize()),
        Key([MOD, "control"], "h", lazy.layout.grow_left()),
        Key([MOD, "control"], "l", lazy.layout.grow_right()),
        Key([MOD, "control"], "j", lazy.layout.grow_down()),
        Key([MOD, "control"], "k", lazy.layout.grow_up()),
        Key([MOD, "control"], "return", lazy.layout.toggle_split()),
        Key([MOD, "control"], "m", lazy.layout.maximize()),
        Key([MOD, "control"], "i", lazy.layout.grow()),
        Key([MOD, "control"], "u", lazy.layout.shrink()),
        Key([MOD, "shift"], "return", lazy.layout.flip()),
        Key([MOD], "m", lazy.window.toggle_maximize()),
        Key([MOD], "f", lazy.window.toggle_fullscreen()),
        Key([MOD], "w", lazy.window.kill()),
        Key([MOD], "r", lazy.reload_config()),
        Key([MOD], "t", lazy.hide_show_bar("top")),
        Key([MOD], "return", lazy.spawn("kitty")),
        Key([MOD], "space", lazy.spawncmd()),
        Key([MOD], "tab", lazy.next_layout()),
        Key(
            [],
            "Print",
            lazy.spawn("scrot -q 100 ~/pictures/screenshots/%b%d_%H%M%S.png"),
        ),
    ]


# ---------------------------------------------------------
# --- QTile Variables
# ---------------------------------------------------------

auto_fullscreen = qtile_auto_fullscreen()
groups = qtile_groups()
dgroups_key_binder = qtile_key_binder()
widget_defaults = qtile_widgets_default()
extension_defaults = qtile_extension_defaults()
floating_layout = qtile_floating_layout()
focus_on_window_activation = qtile_focus_on_window_activation()
layouts = qtile_layouts()
screens = qtile_screens()
keys = qtile_keys()
