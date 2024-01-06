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

DEFAULT_OUTPUT_PATH = os.path.join(LIBRARY_DIR, "output")
"""
Default output path of the generated images when none is specified.
"""
