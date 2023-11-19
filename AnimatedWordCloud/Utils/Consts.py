# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Consts for AnimatedWordCloud functions
"""


from pathlib import Path
import os


LIBRARY_DIR = Path(__file__).parent.parent
"""
Directory of the library currently exists.
Shows "AnimatedWordCloud" directory.
"""

DEFAULT_ENG_FONT_PATH = os.path.join(
    LIBRARY_DIR,
    "Assets",
    "Fonts",
    "NotoSansMono-VariableFont_wdth,wght.ttf",
)
"""
path of default Eng font file exists
"""

TRANSITION_SYMBOL = "->"
"""
Symbol showed in image that indicates the transition of the time.

ex. shown as "2021/01/01 -> 2021/01/02"
"""
