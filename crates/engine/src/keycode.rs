pub type Keycode = u16;

pub const KEY_BUFFER_SIZE: usize = 512;

pub const KEY_NONE: Keycode = 0;

pub const KEY_A: Keycode = 4;
pub const KEY_B: Keycode = 5;
pub const KEY_C: Keycode = 6;
pub const KEY_D: Keycode = 7;
pub const KEY_E: Keycode = 8;
pub const KEY_F: Keycode = 9;
pub const KEY_G: Keycode = 10;
pub const KEY_H: Keycode = 11;
pub const KEY_I: Keycode = 12;
pub const KEY_J: Keycode = 13;
pub const KEY_K: Keycode = 14;
pub const KEY_L: Keycode = 15;
pub const KEY_M: Keycode = 16;
pub const KEY_N: Keycode = 17;
pub const KEY_O: Keycode = 18;
pub const KEY_P: Keycode = 19;
pub const KEY_Q: Keycode = 20;
pub const KEY_R: Keycode = 21;
pub const KEY_S: Keycode = 22;
pub const KEY_T: Keycode = 23;
pub const KEY_U: Keycode = 24;
pub const KEY_V: Keycode = 25;
pub const KEY_W: Keycode = 26;
pub const KEY_X: Keycode = 27;
pub const KEY_Y: Keycode = 28;
pub const KEY_Z: Keycode = 29;
pub const KEY_1: Keycode = 30;
pub const KEY_2: Keycode = 31;
pub const KEY_3: Keycode = 32;
pub const KEY_4: Keycode = 33;
pub const KEY_5: Keycode = 34;
pub const KEY_6: Keycode = 35;
pub const KEY_7: Keycode = 36;
pub const KEY_8: Keycode = 37;
pub const KEY_9: Keycode = 38;
pub const KEY_0: Keycode = 39;
pub const KEY_RETURN: Keycode = 40;
pub const KEY_ESCAPE: Keycode = 41;
pub const KEY_BACKSPACE: Keycode = 42;
pub const KEY_TAB: Keycode = 43;
pub const KEY_SPACE: Keycode = 44;
pub const KEY_MINUS: Keycode = 45;
pub const KEY_EQUALS: Keycode = 46;
pub const KEY_LEFTBRACKET: Keycode = 47;
pub const KEY_RIGHTBRACKET: Keycode = 48;
pub const KEY_BACKSLASH: Keycode = 49;
pub const KEY_NONUSHASH: Keycode = 50;
pub const KEY_SEMICOLON: Keycode = 51;
pub const KEY_APOSTROPHE: Keycode = 52;
pub const KEY_GRAVE: Keycode = 53;
pub const KEY_COMMA: Keycode = 54;
pub const KEY_PERIOD: Keycode = 55;
pub const KEY_SLASH: Keycode = 56;
pub const KEY_CAPSLOCK: Keycode = 57;
pub const KEY_F1: Keycode = 58;
pub const KEY_F2: Keycode = 59;
pub const KEY_F3: Keycode = 60;
pub const KEY_F4: Keycode = 61;
pub const KEY_F5: Keycode = 62;
pub const KEY_F6: Keycode = 63;
pub const KEY_F7: Keycode = 64;
pub const KEY_F8: Keycode = 65;
pub const KEY_F9: Keycode = 66;
pub const KEY_F10: Keycode = 67;
pub const KEY_F11: Keycode = 68;
pub const KEY_F12: Keycode = 69;
pub const KEY_PRINTSCREEN: Keycode = 70;
pub const KEY_SCROLLLOCK: Keycode = 71;
pub const KEY_PAUSE: Keycode = 72;
pub const KEY_INSERT: Keycode = 73;
pub const KEY_HOME: Keycode = 74;
pub const KEY_PAGEUP: Keycode = 75;
pub const KEY_DELETE: Keycode = 76;
pub const KEY_END: Keycode = 77;
pub const KEY_PAGEDOWN: Keycode = 78;
pub const KEY_RIGHT: Keycode = 79;
pub const KEY_LEFT: Keycode = 80;
pub const KEY_DOWN: Keycode = 81;
pub const KEY_UP: Keycode = 82;
pub const KEY_NUMLOCKCLEAR: Keycode = 83;
pub const KEY_KP_DIVIDE: Keycode = 84;
pub const KEY_KP_MULTIPLY: Keycode = 85;
pub const KEY_KP_MINUS: Keycode = 86;
pub const KEY_KP_PLUS: Keycode = 87;
pub const KEY_KP_ENTER: Keycode = 88;
pub const KEY_KP_1: Keycode = 89;
pub const KEY_KP_2: Keycode = 90;
pub const KEY_KP_3: Keycode = 91;
pub const KEY_KP_4: Keycode = 92;
pub const KEY_KP_5: Keycode = 93;
pub const KEY_KP_6: Keycode = 94;
pub const KEY_KP_7: Keycode = 95;
pub const KEY_KP_8: Keycode = 96;
pub const KEY_KP_9: Keycode = 97;
pub const KEY_KP_0: Keycode = 98;
pub const KEY_KP_PERIOD: Keycode = 99;
pub const KEY_NONUSBACKSLASH: Keycode = 100;
pub const KEY_APPLICATION: Keycode = 101;
pub const KEY_POWER: Keycode = 102;
pub const KEY_KP_EQUALS: Keycode = 103;
pub const KEY_F13: Keycode = 104;
pub const KEY_F14: Keycode = 105;
pub const KEY_F15: Keycode = 106;
pub const KEY_F16: Keycode = 107;
pub const KEY_F17: Keycode = 108;
pub const KEY_F18: Keycode = 109;
pub const KEY_F19: Keycode = 110;
pub const KEY_F20: Keycode = 111;
pub const KEY_F21: Keycode = 112;
pub const KEY_F22: Keycode = 113;
pub const KEY_F23: Keycode = 114;
pub const KEY_F24: Keycode = 115;
pub const KEY_EXECUTE: Keycode = 116;
pub const KEY_HELP: Keycode = 117;
pub const KEY_MENU: Keycode = 118;
pub const KEY_SELECT: Keycode = 119;
pub const KEY_STOP: Keycode = 120;
pub const KEY_AGAIN: Keycode = 121;
pub const KEY_UNDO: Keycode = 122;
pub const KEY_CUT: Keycode = 123;
pub const KEY_COPY: Keycode = 124;
pub const KEY_PASTE: Keycode = 125;
pub const KEY_FIND: Keycode = 126;
pub const KEY_MUTE: Keycode = 127;
pub const KEY_VOLUMEUP: Keycode = 128;
pub const KEY_VOLUMEDOWN: Keycode = 129;
pub const KEY_KP_COMMA: Keycode = 133;
pub const KEY_KP_EQUALSAS400: Keycode = 134;
pub const KEY_INTERNATIONAL1: Keycode = 135;
pub const KEY_INTERNATIONAL2: Keycode = 136;
pub const KEY_INTERNATIONAL3: Keycode = 137;
pub const KEY_INTERNATIONAL4: Keycode = 138;
pub const KEY_INTERNATIONAL5: Keycode = 139;
pub const KEY_INTERNATIONAL6: Keycode = 140;
pub const KEY_INTERNATIONAL7: Keycode = 141;
pub const KEY_INTERNATIONAL8: Keycode = 142;
pub const KEY_INTERNATIONAL9: Keycode = 143;
pub const KEY_LANG1: Keycode = 144;
pub const KEY_LANG2: Keycode = 145;
pub const KEY_LANG3: Keycode = 146;
pub const KEY_LANG4: Keycode = 147;
pub const KEY_LANG5: Keycode = 148;
pub const KEY_LANG6: Keycode = 149;
pub const KEY_LANG7: Keycode = 150;
pub const KEY_LANG8: Keycode = 151;
pub const KEY_LANG9: Keycode = 152;
pub const KEY_ALTERASE: Keycode = 153;
pub const KEY_SYSREQ: Keycode = 154;
pub const KEY_CANCEL: Keycode = 155;
pub const KEY_CLEAR: Keycode = 156;
pub const KEY_PRIOR: Keycode = 157;
pub const KEY_RETURN2: Keycode = 158;
pub const KEY_SEPARATOR: Keycode = 159;
pub const KEY_OUT: Keycode = 160;
pub const KEY_OPER: Keycode = 161;
pub const KEY_CLEARAGAIN: Keycode = 162;
pub const KEY_CRSEL: Keycode = 163;
pub const KEY_EXSEL: Keycode = 164;
pub const KEY_KP_00: Keycode = 176;
pub const KEY_KP_000: Keycode = 177;
pub const KEY_THOUSANDSSEPARATOR: Keycode = 178;
pub const KEY_DECIMALSEPARATOR: Keycode = 179;
pub const KEY_CURRENCYUNIT: Keycode = 180;
pub const KEY_CURRENCYSUBUNIT: Keycode = 181;
pub const KEY_KP_LEFTPAREN: Keycode = 182;
pub const KEY_KP_RIGHTPAREN: Keycode = 183;
pub const KEY_KP_LEFTBRACE: Keycode = 184;
pub const KEY_KP_RIGHTBRACE: Keycode = 185;
pub const KEY_KP_TAB: Keycode = 186;
pub const KEY_KP_BACKSPACE: Keycode = 187;
pub const KEY_KP_A: Keycode = 188;
pub const KEY_KP_B: Keycode = 189;
pub const KEY_KP_C: Keycode = 190;
pub const KEY_KP_D: Keycode = 191;
pub const KEY_KP_E: Keycode = 192;
pub const KEY_KP_F: Keycode = 193;
pub const KEY_KP_XOR: Keycode = 194;
pub const KEY_KP_POWER: Keycode = 195;
pub const KEY_KP_PERCENT: Keycode = 196;
pub const KEY_KP_LESS: Keycode = 197;
pub const KEY_KP_GREATER: Keycode = 198;
pub const KEY_KP_AMPERSAND: Keycode = 199;
pub const KEY_KP_DBLAMPERSAND: Keycode = 200;
pub const KEY_KP_VERTICALBAR: Keycode = 201;
pub const KEY_KP_DBLVERTICALBAR: Keycode = 202;
pub const KEY_KP_COLON: Keycode = 203;
pub const KEY_KP_HASH: Keycode = 204;
pub const KEY_KP_SPACE: Keycode = 205;
pub const KEY_KP_AT: Keycode = 206;
pub const KEY_KP_EXCLAM: Keycode = 207;
pub const KEY_KP_MEMSTORE: Keycode = 208;
pub const KEY_KP_MEMRECALL: Keycode = 209;
pub const KEY_KP_MEMCLEAR: Keycode = 210;
pub const KEY_KP_MEMADD: Keycode = 211;
pub const KEY_KP_MEMSUBTRACT: Keycode = 212;
pub const KEY_KP_MEMMULTIPLY: Keycode = 213;
pub const KEY_KP_MEMDIVIDE: Keycode = 214;
pub const KEY_KP_PLUSMINUS: Keycode = 215;
pub const KEY_KP_CLEAR: Keycode = 216;
pub const KEY_KP_CLEARENTRY: Keycode = 217;
pub const KEY_KP_BINARY: Keycode = 218;
pub const KEY_KP_OCTAL: Keycode = 219;
pub const KEY_KP_DECIMAL: Keycode = 220;
pub const KEY_KP_HEXADECIMAL: Keycode = 221;
pub const KEY_LCTRL: Keycode = 224;
pub const KEY_LSHIFT: Keycode = 225;
pub const KEY_LALT: Keycode = 226;
pub const KEY_LGUI: Keycode = 227;
pub const KEY_RCTRL: Keycode = 228;
pub const KEY_RSHIFT: Keycode = 229;
pub const KEY_RALT: Keycode = 230;
pub const KEY_RGUI: Keycode = 231;
pub const KEY_MODE: Keycode = 257;
pub const KEY_AUDIONEXT: Keycode = 258;
pub const KEY_AUDIOPREV: Keycode = 259;
pub const KEY_AUDIOSTOP: Keycode = 260;
pub const KEY_AUDIOPLAY: Keycode = 261;
pub const KEY_AUDIOMUTE: Keycode = 262;
pub const KEY_MEDIASELECT: Keycode = 263;
pub const KEY_WWW: Keycode = 264;
pub const KEY_MAIL: Keycode = 265;
pub const KEY_CALCULATOR: Keycode = 266;
pub const KEY_COMPUTER: Keycode = 267;
pub const KEY_AC_SEARCH: Keycode = 268;
pub const KEY_AC_HOME: Keycode = 269;
pub const KEY_AC_BACK: Keycode = 270;
pub const KEY_AC_FORWARD: Keycode = 271;
pub const KEY_AC_STOP: Keycode = 272;
pub const KEY_AC_REFRESH: Keycode = 273;
pub const KEY_AC_BOOKMARKS: Keycode = 274;
pub const KEY_BRIGHTNESSDOWN: Keycode = 275;
pub const KEY_BRIGHTNESSUP: Keycode = 276;
pub const KEY_DISPLAYSWITCH: Keycode = 277;
pub const KEY_KBDILLUMTOGGLE: Keycode = 278;
pub const KEY_KBDILLUMDOWN: Keycode = 279;
pub const KEY_KBDILLUMUP: Keycode = 280;
pub const KEY_EJECT: Keycode = 281;
pub const KEY_SLEEP: Keycode = 282;
pub const KEY_APP1: Keycode = 283;
pub const KEY_APP2: Keycode = 284;
pub const KEY_AUDIOREWIND: Keycode = 285;
pub const KEY_AUDIOFASTFORWARD: Keycode = 286;

pub const KEY_MIN_VALUE: Keycode = KEY_A;
pub const KEY_MAX_VALUE: Keycode = KEY_AUDIOFASTFORWARD;

pub const KEY_SHIFT: Keycode = 290;
pub const KEY_CONTROL: Keycode = 291;
pub const KEY_ALT: Keycode = 292;
pub const KEY_SUPER: Keycode = 293;

pub const MOUSE_BUTTON_LEFT: Keycode = 295;
pub const MOUSE_BUTTON_MIDDLE: Keycode = 296;
pub const MOUSE_BUTTON_RIGHT: Keycode = 297;

pub const CONTROLLER1_BUTTON_A: Keycode = 300;
pub const CONTROLLER1_BUTTON_B: Keycode = 301;
pub const CONTROLLER1_BUTTON_X: Keycode = 302;
pub const CONTROLLER1_BUTTON_Y: Keycode = 303;
pub const CONTROLLER1_BUTTON_BACK: Keycode = 304;
pub const CONTROLLER1_BUTTON_START: Keycode = 306;
pub const CONTROLLER1_BUTTON_LEFTSHOULDER: Keycode = 309;
pub const CONTROLLER1_BUTTON_RIGHTSHOULDER: Keycode = 310;
pub const CONTROLLER1_BUTTON_DPAD_UP: Keycode = 311;
pub const CONTROLLER1_BUTTON_DPAD_DOWN: Keycode = 312;
pub const CONTROLLER1_BUTTON_DPAD_LEFT: Keycode = 313;
pub const CONTROLLER1_BUTTON_DPAD_RIGHT: Keycode = 314;

pub const CONTROLLER2_BUTTON_A: Keycode = 400;
pub const CONTROLLER2_BUTTON_B: Keycode = 401;
pub const CONTROLLER2_BUTTON_X: Keycode = 402;
pub const CONTROLLER2_BUTTON_Y: Keycode = 403;
pub const CONTROLLER2_BUTTON_BACK: Keycode = 404;
pub const CONTROLLER2_BUTTON_START: Keycode = 406;
pub const CONTROLLER2_BUTTON_LEFTSHOULDER: Keycode = 409;
pub const CONTROLLER2_BUTTON_RIGHTSHOULDER: Keycode = 410;
pub const CONTROLLER2_BUTTON_DPAD_UP: Keycode = 411;
pub const CONTROLLER2_BUTTON_DPAD_DOWN: Keycode = 412;
pub const CONTROLLER2_BUTTON_DPAD_LEFT: Keycode = 413;
pub const CONTROLLER2_BUTTON_DPAD_RIGHT: Keycode = 414;
