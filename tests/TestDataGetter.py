# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Get data from test_data submodule
"""

from __future__ import annotations
import json
from AnimatedWordCloud.Animator.TimelapseWordVector import TimelapseWordVector


def get_test_timelapses_raw() -> list[list[tuple[str, dict[str, float]]]]:
    """
    Get the raw data of word vectors from test_data submodule

    :return: The list of raw data of word vector timelapses
    :rtype: List[Tuple[str, Dict[str, float]]]
    """

    output = []

    # from Elon Musk's tweets
    with open(
        "tests/test_data/ElonMusk/wordvector_timelapse_elon.json", "r"
    ) as f:
        output.append(json.load(f))

    return output


raw_timelapses_test = get_test_timelapses_raw()
"""
The raw data of word vector timelapses got from test_data submodule
:rtype: List[List[Tuple[str, Dict[str, float]]]]
"""

timelapses_test = []
"""
The inner class data of word vector timelapses got from test_data submodule
:rtype: List[TimelapseWordVector]
"""
for raw_timelapse in raw_timelapses_test:
    timelapse = TimelapseWordVector.convert_from_dicts_list(raw_timelapse)
    timelapses_test.append(timelapse)
