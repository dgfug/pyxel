# flake8: noqa
from typing import Callable, List, Optional, Tuple, Union

#
# constants
#
PYXEL_VERSION: str

RESOURCE_FILE_EXTENSION: str
RESOURCE_ARCHIVE_DIRNAME: str

COLOR_COUNT: int
IMAGE_COUNT: int
IMAGE_SIZE: int
TILEMAP_COUNT: int
TILEMAP_SIZE: int
TILE_SIZE: int

COLOR_BLACK: int
COLOR_NAVY: int
COLOR_PURPLE: int
COLOR_GREEN: int
COLOR_BROWN: int
COLOR_DARK_BLUE: int
COLOR_LIGHT_BLUE: int
COLOR_WHITE: int
COLOR_RED: int
COLOR_ORANGE: int
COLOR_YELLOW: int
COLOR_LIME: int
COLOR_CYAN: int
COLOR_GRAY: int
COLOR_PINK: int
COLOR_PEACH: int

FONT_WIDTH: int
FONT_HEIGHT: int

CHANNEL_COUNT: int
SOUND_COUNT: int
MUSIC_COUNT: int

TONE_TRIANGLE: int
TONE_SQUARE: int
TONE_PULSE: int
TONE_NOISE: int

EFFECT_NONE: int
EFFECT_SLIDE: int
EFFECT_VIBRATO: int
EFFECT_FADEOUT: int

#
# key
#
KEY_NONE: int

KEY_A: int
KEY_B: int
KEY_C: int
KEY_D: int
KEY_E: int
KEY_F: int
KEY_G: int
KEY_H: int
KEY_I: int
KEY_J: int
KEY_K: int
KEY_L: int
KEY_M: int
KEY_N: int
KEY_O: int
KEY_P: int
KEY_Q: int
KEY_R: int
KEY_S: int
KEY_T: int
KEY_U: int
KEY_V: int
KEY_W: int
KEY_X: int
KEY_Y: int
KEY_Z: int
KEY_1: int
KEY_2: int
KEY_3: int
KEY_4: int
KEY_5: int
KEY_6: int
KEY_7: int
KEY_8: int
KEY_9: int
KEY_0: int
KEY_RETURN: int
KEY_ESCAPE: int
KEY_BACKSPACE: int
KEY_TAB: int
KEY_SPACE: int
KEY_MINUS: int
KEY_EQUALS: int
KEY_LEFTBRACKET: int
KEY_RIGHTBRACKET: int
KEY_BACKSLASH: int
KEY_NONUSHASH: int
KEY_SEMICOLON: int
KEY_APOSTROPHE: int
KEY_GRAVE: int
KEY_COMMA: int
KEY_PERIOD: int
KEY_SLASH: int
KEY_CAPSLOCK: int
KEY_F1: int
KEY_F2: int
KEY_F3: int
KEY_F4: int
KEY_F5: int
KEY_F6: int
KEY_F7: int
KEY_F8: int
KEY_F9: int
KEY_F10: int
KEY_F11: int
KEY_F12: int
KEY_PRINTSCREEN: int
KEY_SCROLLLOCK: int
KEY_PAUSE: int
KEY_INSERT: int
KEY_HOME: int
KEY_PAGEUP: int
KEY_DELETE: int
KEY_END: int
KEY_PAGEDOWN: int
KEY_RIGHT: int
KEY_LEFT: int
KEY_DOWN: int
KEY_UP: int
KEY_NUMLOCKCLEAR: int
KEY_KP_DIVIDE: int
KEY_KP_MULTIPLY: int
KEY_KP_MINUS: int
KEY_KP_PLUS: int
KEY_KP_ENTER: int
KEY_KP_1: int
KEY_KP_2: int
KEY_KP_3: int
KEY_KP_4: int
KEY_KP_5: int
KEY_KP_6: int
KEY_KP_7: int
KEY_KP_8: int
KEY_KP_9: int
KEY_KP_0: int
KEY_KP_PERIOD: int
KEY_NONUSBACKSLASH: int
KEY_APPLICATION: int
KEY_POWER: int
KEY_KP_EQUALS: int
KEY_F13: int
KEY_F14: int
KEY_F15: int
KEY_F16: int
KEY_F17: int
KEY_F18: int
KEY_F19: int
KEY_F20: int
KEY_F21: int
KEY_F22: int
KEY_F23: int
KEY_F24: int
KEY_EXECUTE: int
KEY_HELP: int
KEY_MENU: int
KEY_SELECT: int
KEY_STOP: int
KEY_AGAIN: int
KEY_UNDO: int
KEY_CUT: int
KEY_COPY: int
KEY_PASTE: int
KEY_FIND: int
KEY_MUTE: int
KEY_VOLUMEUP: int
KEY_VOLUMEDOWN: int
KEY_KP_COMMA: int
KEY_KP_EQUALSAS400: int
KEY_INTERNATIONAL1: int
KEY_INTERNATIONAL2: int
KEY_INTERNATIONAL3: int
KEY_INTERNATIONAL4: int
KEY_INTERNATIONAL5: int
KEY_INTERNATIONAL6: int
KEY_INTERNATIONAL7: int
KEY_INTERNATIONAL8: int
KEY_INTERNATIONAL9: int
KEY_LANG1: int
KEY_LANG2: int
KEY_LANG3: int
KEY_LANG4: int
KEY_LANG5: int
KEY_LANG6: int
KEY_LANG7: int
KEY_LANG8: int
KEY_LANG9: int
KEY_ALTERASE: int
KEY_SYSREQ: int
KEY_CANCEL: int
KEY_CLEAR: int
KEY_PRIOR: int
KEY_RETURN2: int
KEY_SEPARATOR: int
KEY_OUT: int
KEY_OPER: int
KEY_CLEARAGAIN: int
KEY_CRSEL: int
KEY_EXSEL: int
KEY_KP_00: int
KEY_KP_000: int
KEY_THOUSANDSSEPARATOR: int
KEY_DECIMALSEPARATOR: int
KEY_CURRENCYUNIT: int
KEY_CURRENCYSUBUNIT: int
KEY_KP_LEFTPAREN: int
KEY_KP_RIGHTPAREN: int
KEY_KP_LEFTBRACE: int
KEY_KP_RIGHTBRACE: int
KEY_KP_TAB: int
KEY_KP_BACKSPACE: int
KEY_KP_A: int
KEY_KP_B: int
KEY_KP_C: int
KEY_KP_D: int
KEY_KP_E: int
KEY_KP_F: int
KEY_KP_XOR: int
KEY_KP_POWER: int
KEY_KP_PERCENT: int
KEY_KP_LESS: int
KEY_KP_GREATER: int
KEY_KP_AMPERSAND: int
KEY_KP_DBLAMPERSAND: int
KEY_KP_VERTICALBAR: int
KEY_KP_DBLVERTICALBAR: int
KEY_KP_COLON: int
KEY_KP_HASH: int
KEY_KP_SPACE: int
KEY_KP_AT: int
KEY_KP_EXCLAM: int
KEY_KP_MEMSTORE: int
KEY_KP_MEMRECALL: int
KEY_KP_MEMCLEAR: int
KEY_KP_MEMADD: int
KEY_KP_MEMSUBTRACT: int
KEY_KP_MEMMULTIPLY: int
KEY_KP_MEMDIVIDE: int
KEY_KP_PLUSMINUS: int
KEY_KP_CLEAR: int
KEY_KP_CLEARENTRY: int
KEY_KP_BINARY: int
KEY_KP_OCTAL: int
KEY_KP_DECIMAL: int
KEY_KP_HEXADECIMAL: int
KEY_LCTRL: int
KEY_LSHIFT: int
KEY_LALT: int
KEY_LGUI: int
KEY_RCTRL: int
KEY_RSHIFT: int
KEY_RALT: int
KEY_RGUI: int
KEY_MODE: int
KEY_AUDIONEXT: int
KEY_AUDIOPREV: int
KEY_AUDIOSTOP: int
KEY_AUDIOPLAY: int
KEY_AUDIOMUTE: int
KEY_MEDIASELECT: int
KEY_WWW: int
KEY_MAIL: int
KEY_CALCULATOR: int
KEY_COMPUTER: int
KEY_AC_SEARCH: int
KEY_AC_HOME: int
KEY_AC_BACK: int
KEY_AC_FORWARD: int
KEY_AC_STOP: int
KEY_AC_REFRESH: int
KEY_AC_BOOKMARKS: int
KEY_BRIGHTNESSDOWN: int
KEY_BRIGHTNESSUP: int
KEY_DISPLAYSWITCH: int
KEY_KBDILLUMTOGGLE: int
KEY_KBDILLUMDOWN: int
KEY_KBDILLUMUP: int
KEY_EJECT: int
KEY_SLEEP: int
KEY_APP1: int
KEY_APP2: int
KEY_AUDIOREWIND: int
KEY_AUDIOFASTFORWARD: int

KEY_SHIFT: int
KEY_CTRL: int
KEY_ALT: int
KEY_GUI: int

MOUSE_POS_X: int
MOUSE_POS_Y: int
MOUSE_WHEEL_X: int
MOUSE_WHEEL_Y: int

MOUSE_BUTTON_LEFT: int
MOUSE_BUTTON_MIDDLE: int
MOUSE_BUTTON_RIGHT: int
MOUSE_BUTTON_X1: int
MOUSE_BUTTON_X2: int
MOUSE_BUTTON_UNKOWN: int

GAMEPAD1_AXIS_LEFTX: int
GAMEPAD1_AXIS_LEFTY: int
GAMEPAD1_AXIS_RIGHTX: int
GAMEPAD1_AXIS_RIGHTY: int
GAMEPAD1_AXIS_TRIGGERLEFT: int
GAMEPAD1_AXIS_TRIGGERRIGHT: int

GAMEPAD1_BUTTON_A: int
GAMEPAD1_BUTTON_B: int
GAMEPAD1_BUTTON_X: int
GAMEPAD1_BUTTON_Y: int
GAMEPAD1_BUTTON_BACK: int
GAMEPAD1_BUTTON_GUIDE: int
GAMEPAD1_BUTTON_START: int
GAMEPAD1_BUTTON_LEFTSTICK: int
GAMEPAD1_BUTTON_RIGHTSTICK: int
GAMEPAD1_BUTTON_LEFTSHOULDER: int
GAMEPAD1_BUTTON_RIGHTSHOULDER: int
GAMEPAD1_BUTTON_DPAD_UP: int
GAMEPAD1_BUTTON_DPAD_DOWN: int
GAMEPAD1_BUTTON_DPAD_LEFT: int
GAMEPAD1_BUTTON_DPAD_RIGHT: int

GAMEPAD2_AXIS_LEFTX: int
GAMEPAD2_AXIS_LEFTY: int
GAMEPAD2_AXIS_RIGHTX: int
GAMEPAD2_AXIS_RIGHTY: int
GAMEPAD2_AXIS_TRIGGERLEFT: int
GAMEPAD2_AXIS_TRIGGERRIGHT: int

GAMEPAD2_BUTTON_A: int
GAMEPAD2_BUTTON_B: int
GAMEPAD2_BUTTON_X: int
GAMEPAD2_BUTTON_Y: int
GAMEPAD2_BUTTON_BACK: int
GAMEPAD2_BUTTON_GUIDE: int
GAMEPAD2_BUTTON_START: int
GAMEPAD2_BUTTON_LEFTSTICK: int
GAMEPAD2_BUTTON_RIGHTSTICK: int
GAMEPAD2_BUTTON_LEFTSHOULDER: int
GAMEPAD2_BUTTON_RIGHTSHOULDER: int
GAMEPAD2_BUTTON_DPAD_UP: int
GAMEPAD2_BUTTON_DPAD_DOWN: int
GAMEPAD2_BUTTON_DPAD_LEFT: int
GAMEPAD2_BUTTON_DPAD_RIGHT: int

#
# System
#
width: int
height: int
frame_count: int

def init(
    width: int,
    height: int,
    title: Optional[str],
    scale: Optional[int],
    fps: Optional[int],
    quit_key: Optional[int],
    capture_sec: Optional[int],
): ...
def title(title: str) -> None: ...
def icon(data: List[str], scale: int) -> None: ...
def fullscreen() -> None: ...
def run(update: Callable[[], None], draw: Callable[[], None]) -> None: ...
def show() -> None: ...
def flip() -> None: ...
def quit() -> None: ...

#
# Resource
#
mouse_x: int
mouse_y: int
mouse_wheel : int
text_input : str
drop_files: List[str]

def load(
    filename: str,
    image: Optional[bool],
    tilemap: Optional[bool],
    sound: Optional[bool],
    music: Optional[bool],
) -> None: ...
def save(
    filename: str,
    image: Optional[bool],
    tilemap: Optional[bool],
    sound: Optional[bool],
    music: Optional[bool],
) -> None: ...
def screenshot() -> None: ...
def reset_capture() -> None: ...
def screencast() -> None: ...

#
# Input
#
def mouse(visible: bool) -> None: ...
def btn(key: int) -> bool: ...
def btnp(key: int, hold: Optional[int], repeat: Optional[int]) -> bool: ...
def btnr(key: int) -> bool: ...
def btnv(key: int) -> int: ...

#
# Graphics
#
class Image: ...
class Tilemap: ...

colors: List[int]
screen: Image
cursor: Image
font: Image

def image(img: int) -> Image: ...
def tilemap(tm: int) -> Tilemap: ...
def clip(
    x: Optional[int],
    y: Optional[int],
    w: Optional[int],
    h: Optional[int],
) -> None: ...
def pal(col1: Optional[int], col2: Optional[int]) -> None: ...
def cls(col: int) -> None: ...
def pget(x: int, y: int) -> int: ...
def pset(x: int, y: int, col: int) -> None: ...
def line(x1: int, y1: int, x2: int, y2: int, col: int) -> None: ...
def rect(x: int, y: int, w: int, h: int, col: int) -> None: ...
def rectb(x: int, y: int, w: int, h: int, col: int) -> None: ...
def circ(x: int, y: int, r: int, col: int) -> None: ...
def circb(x: int, y: int, r: int, col: int) -> None: ...
def tri(
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    x3: int,
    y3: int,
    col: int,
) -> None: ...
def trib(
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    x3: int,
    y3: int,
    col: int,
) -> None: ...
def blt(
    x: int,
    y: int,
    img: int,
    image_x: int,
    image_y: int,
    w: int,
    h: int,
    color_key: Optional[int],
) -> None: ...
def bltm(
    x: int,
    y: int,
    tm: int,
    u: int,
    v: int,
    w: int,
    h: int,
    colkey: Optional[int],
) -> None: ...
def text(x: int, y: int, string: str, col: int) -> None: ...

#
# Audio
#
class Channel: ...
class Sound: ...
class Music: ...

def channel(ch: int) -> Channel: ...
def sound(snd: int) -> Sound: ...
def music(msc: int) -> Music: ...
def play_pos(ch: int) -> Optional[Tuple[int, int]]: ...
def play(ch: int, snd: Union[List[int] | int], loop: Optional[bool]) -> None: ...
def playm(msc: int, loop: Optional[bool]) -> None: ...
def stop(ch: Optional[int]) -> None: ...

#
# Image class
#
class Image:
    width: int
    height: int
    def __init__(self, width: int, height: int) -> None: ...
    def height(self) -> int: ...
    def set(self, x: int, y: int, data_str: List[str]) -> None: ...
    def load(self, x: int, y: int, filename: str) -> None: ...
    def save(self, filename: str, scale: int) -> None: ...
    def clip(
        self, x: Optional[int], y: Optional[int], w: Optional[int], h: Optional[int]
    ) -> None: ...
    def cls(self, col: int) -> None: ...
    def pget(self, x: int, y: int) -> int: ...
    def pset(self, x: int, y: int, col: int) -> None: ...
    def line(self, x1: int, y1: int, x2: int, y2: int, col: int) -> None: ...
    def rect(self, x: int, y: int, w: int, h: int, col: int) -> None: ...
    def rectb(self, x: int, y: int, w: int, h: int, col: int) -> None: ...
    def circ(self, x: int, y: int, r: int, col: int) -> None: ...
    def circb(self, x: int, y: int, r: int, col: int) -> None: ...
    def tri(
        self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, col: int
    ) -> None: ...
    def trib(
        self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, col: int
    ) -> None: ...
    def fill(self, x: int, y: int, col: int) -> None: ...
    def blt(
        self,
        x: int,
        y: int,
        img: Image,
        u: int,
        v: int,
        w: int,
        h: int,
        colkey: Optional[int],
    ) -> None: ...
    def bltm(
        self,
        x: int,
        y: int,
        tm: Tilemap,
        u: int,
        v: int,
        w: int,
        h: int,
        colkey: Optional[int],
    ) -> None: ...
    def text(self, x: int, y: int, s: str, col: int, font: Image) -> None: ...

#
# Tilemap class
#
class Tilemap:
    width: int
    height: int
    iamge: Union[Image | int]
    def __init__(self, width: int, height: int, img: Union[Image | int]) -> None: ...
    def set(self, x: int, y: int, data_str: List[str]) -> None: ...
    def clip(
        self,
        x: Optional[int],
        y: Optional[int],
        w: Optional[int],
        h: Optional[int],
    ) -> None: ...
    def cls(self, tile: Tuple[int, int]) -> None: ...
    def pget(self, x: int, y: int) -> Tuple[int, int]: ...
    def pset(self, x: int, y: int, tile: Tuple[int, int]) -> None: ...
    def line(
        self, x1: int, y1: int, x2: int, y2: int, tile: Tuple[int, int]
    ) -> None: ...
    def rect(self, x: int, y: int, w: int, h: int, tile: Tuple[int, int]) -> None: ...
    def rectb(self, x: int, y: int, w: int, h: int, tile: Tuple[int, int]) -> None: ...
    def circ(self, x: int, y: int, r: int, tile: Tuple[int, int]) -> None: ...
    def circb(self, x: int, y: int, r: int, tile: Tuple[int, int]) -> None: ...
    def tri(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        x3: int,
        y3: int,
        tile: Tuple[int, int],
    ) -> None: ...
    def trib(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        x3: int,
        y3: int,
        tile: Tuple[int, int],
    ) -> None: ...
    def fill(self, x: int, y: int, tile: Tuple[int, int]) -> None: ...
    def blt(
        self,
        x: int,
        y: int,
        tm: Tilemap,
        u: int,
        v: int,
        w: int,
        h: int,
        tilekey: Optional[Tuple[int, int]],
    ) -> None: ...

#
# Channel class
#
class Channel:
    volume: int
    def __init__(self) -> None: ...
    def play_pos(self) -> Optional[Tuple[int, int]]: ...
    def play(self, snd: Union[List[Sound] | Sound], loop: Optional[bool]) -> None: ...
    def stop(self) -> None: ...

#
# Sound class
#
class Sound:
    notes: List[int]
    tones: List[int]
    volumes: List[int]
    effects: List[int]
    speed: int
    def __init__(self) -> None: ...
    def set(
        self,
        note_str: str,
        tone_str: str,
        volume_str: str,
        effect_str: str,
        speed: int,
    ) -> None: ...
    def set_note(self, note_str: str) -> None: ...
    def set_tone(self, tone_str: str) -> None: ...
    def set_volume(self, volume_str: str) -> None: ...
    def set_effect(self, effect_str: str) -> None: ...

#
# Music class
#
class Music:
    seqs: List[List[int]]
    def __init__(self) -> None: ...
    def set(self, seqs: List[List[int]]) -> None: ...
