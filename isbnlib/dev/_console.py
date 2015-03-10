# -*- coding: utf-8 -*-
"""isbnlib console & uprint file.

This is a 'just good enough' fix for UTF-8 printing and redirection.
On Windows, some characters (cyrillic, chinese, ...) are missing
in console, however if you redirect to a file they will shown!
Its OK on Linux and OSX.
"""
# flake8: noqa

import os
import sys


WINDOWS = os.name == 'nt'
PY2 = sys.version < '3'
PY3 = not PY2
EOL = '\r\n' if WINDOWS else '\n'


def set_msconsolefont(fontname="Lucida Console"):
    """stackoverflow.com/questions/3592673/change-console-font-in-windows.

    At least in Windows 8, the kernel changes the console code page
    to cp65001 (Windows's UTF-8) too. But in case you need, you have
    a function to do that below.
    """
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


def set_mscp65001():
    """Change Windows console to cp65001 (UTF-8)."""
    try:
        if sys.stdout.encoding == 'cp65001':
            return
    except:
        pass
    try:
        # change code page
        # use pywin32 if installed
        import win32console
        win32console.SetConsoleOutputCP(65001)
        win32console.SetConsoleCP(65001)
    except:
        # fallback
        import subprocess
        subprocess.call("chcp 65001 > %TMP%\\xxx", shell = True)


def uprint(content, filep=None, mode='w'):
    """Unicode print function.

    Works with redirection too.
    """
    s = content + EOL
    buf = s.encode("utf-8")
    if filep:
        stdout = sys.stdout
        sys.stdout = open(filep, mode)
    if PY3:
        sys.stdout.buffer.write(buf)
    if PY2:
        sys.stdout.write(buf)
    if filep:
        sys.stdout = stdout
    return True
