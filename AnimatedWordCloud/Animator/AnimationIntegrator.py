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
from AnimatedWordCloud.Utils import Config


def integrate_images(image_paths: list[str], config: Config) -> None:
    """
    Create images of each frame

    :param
    List[str] image_paths: List of image_paths created by AnimatedWordCloud.Animator.ImageCreator.create_images
    :param Config config: Config instance
    :return: None
    """

    gif_images = [Image.open(path) for path in image_paths]
    filepath = os.path.join(config.output_path, config.output_filename)
    gif_images[0].save(
        filepath,
        save_all=True,
        append_images=gif_images[1:],
        duration=config.duration_per_frame,
        loop=0,
    )

    return
