# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Create images of each frame
"""

from typing import List
from AnimatedWordCloud.Utils import AllocationTimelapse


def create_images(position_in_frames: AllocationTimelapse) -> List[str]:
    """
    Create images of each frame

    :param Iterable[PositionInFrame] position_in_frames: List of position/size data of each video frame.
    :return: The path of the images. The order of the list is the same as the order of the input.
    :rtype: List[str]
    """

    return [""]
