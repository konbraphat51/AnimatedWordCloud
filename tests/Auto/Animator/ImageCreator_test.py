# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the ImageCreator classes
"""
import os
import glob
from AnimatedWordCloud.Animator.ImageCreator import create_images
from AnimatedWordCloud.Utils import (
    AllocationTimelapse,
    AllocationInFrame,
)
from AnimatedWordCloud.Utils import (
    Config,
    DEFAULT_OUTPUT_PATH,
)


def test_imagecreator():
    # test create_images function
    position_in_frames = AllocationTimelapse()
    allocation_in_frame = AllocationInFrame(from_static_allocation=True)
    allocation_in_frame.words = {"word": (30, (50, 50))}  # dictionary
    position_in_frames.add("2023_04_01", allocation_in_frame)
    create_images(position_in_frames, Config())
    test_path = os.path.join(DEFAULT_OUTPUT_PATH, "2023_04_01.png")
    assert os.path.isfile(test_path)
    os.remove(os.path.join(DEFAULT_OUTPUT_PATH, "2023_04_01.png"))
