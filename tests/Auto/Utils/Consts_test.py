# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing Consts module
"""

from pathlib import Path
from AnimatedWordCloud.Utils.Consts import (
    LIBRARY_DIR,
    DEFAULT_ENG_FONT_PATH,
)


def test_globals():
    assert LIBRARY_DIR.exists()
    assert Path(DEFAULT_ENG_FONT_PATH).exists()
