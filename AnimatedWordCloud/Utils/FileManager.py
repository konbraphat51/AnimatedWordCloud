# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Modules for controling file managements
"""

import os


def ensure_directory_exists(directory_path: str) -> None:
    """
    Verify that the directory exists. If it does not exist, create another directory.

    :param
    - str directory_path
    :rtype: None
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return
