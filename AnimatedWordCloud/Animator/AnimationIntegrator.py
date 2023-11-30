# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Integrates the images into a single video (gif)
"""

from __future__ import annotations
from PIL import Image


def integrate_images(
    image_paths: list[str],
    filename: str,
    duration_per_frame: int = 500,
) -> None:
    """
    Create images of each frame

    :param
    List[str] image_paths: List of image_paths created by AnimatedWordCloud.Animator.ImageCreator.create_images.
    str filename: output filename.
    int duration: display time for each frame
    :return: None
    """

    gif_images = [Image.open(path) for path in image_paths]

    gif_images[0].save(
        filename,
        save_all=True,
        append_images=gif_images[1:],
        duration=duration_per_frame,
        loop=0,
    )

    return
