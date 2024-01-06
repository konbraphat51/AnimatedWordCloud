# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Integrates the images into a single video (gif)
"""

from __future__ import annotations
import os
from PIL import Image
from AnimatedWordCloud.Utils import Config, AllocationTimelapse


def integrate_images(
    image_paths: list[str],
    allocation_timelapse: AllocationTimelapse,
    config: Config,
    filename: str = "output.gif",
) -> str:
    """
    Create images of each frame

    :param
    List[str] image_paths: List of image_paths created by AnimatedWordCloud.Animator.ImageCreator.create_images
    :param AllocationTimelapse allocation_timelapse: AllocationTimelapse instance
    :param Config config: Config instance
    :return: The path of the output animation file
    :rtype: str
    """

    # input
    gif_images = [Image.open(path) for path in image_paths]

    # output
    filepath_output = os.path.join(config.output_path, filename)

    # compute the duration of each frame
    durations = []
    for _, allocation_in_frame in allocation_timelapse.timelapse:
        if allocation_in_frame.from_static_allocation:
            durations.append(config.duration_per_static_frame)
        else:
            durations.append(config.duration_per_interpolation_frame)

    # save gif
    gif_images[0].save(
        filepath_output,
        save_all=True,
        append_images=gif_images[1:],
        duration=durations,
        loop=0,
    )

    return filepath_output
