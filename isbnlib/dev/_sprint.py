# -*- coding: utf-8 -*-
"""isbnlib sprint file."""
# flake8: noqa

import os
import sys

WINDOWS = os.name == 'nt'
PY2 = sys.version < '3'
EOL = '\r\n' if WINDOWS and not PY2 else '\n'


def set_codepage(cp=65001):
    import win32console
    win32console.SetConsoleOutputCP(cp)
    win32console.SetConsoleCP(cp)


def set_cmdfont(fontname="Lucida Console"):
    import ctypes

    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 11
    font.dwFontSize.Y = 18
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = fontname

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))


if WINDOWS:
    # cp65001 == utf8
    set_codepage(65001)
    set_cmdfont('Lucida Console')


def sprint(content, filep=None, mode='w'):
    """Smart print function.

    So that redirection works and Win console works with utf-8.
    """
    s = content + EOL
    buf = s.encode("utf-8")
    if filep:
        stdout = sys.stdout
        sys.stdout = open(filep, mode)
    sys.stdout.write(buf)
    if filep:
        sys.stdout = stdout
