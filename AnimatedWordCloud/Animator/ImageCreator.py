# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Create images of each frame
"""


from __future__ import annotations
import os
from random import Random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from AnimatedWordCloud.Utils import (
    AllocationTimelapse,
)
from AnimatedWordCloud.Utils.Consts import DEFAULT_OUTPUT_PATH
from AnimatedWordCloud.Utils.FileManager import ensure_directory_exists


class colormap_color_func(object):
    # https://github.com/amueller/word_cloud/blob/main/wordcloud/wordcloud.py#L91
    """Color func created from matplotlib colormap.

    :param colormap : string or matplotlib colormap
        Colormap to sample from
    """

    def __init__(self, color_map="magma"):
        self.color_map = plt.cm.get_cmap(color_map)

    def __call__(self, word, font_size, position, random_state=None, **kwargs):
        if random_state is None:
            random_state = Random()
        r, g, b, _ = np.maximum(
            0, 255 * np.array(self.color_map(random_state.uniform(0, 1)))
        )
        return "rgb({:.0f}, {:.0f}, {:.0f})".format(r, g, b)


def create_images(
    position_in_frames: AllocationTimelapse,
    image_size: tuple[float, float],
    font_path: str,
    background_color: str = "white",
    color_map: str = "magma",
    color_func=None,
) -> list[str]:
    """
    Create images of each frame

    :param AllocationTimelapse position_in_frames: List of position/size data of each video frame.
    :param Tuple[float, float] image_size: Tuple of float values (width, height) representing the size of the image.
    :param font_path: Path to the font file.
    :param background_color:  Background color of the image, default is "white".
    :param color_map:  Colormap to be used for the image, default is "magma".
    :param color_func:  Custom function for color mapping, default is None.
    :return: The path of the images. The order of the list is the same as the order of the input.
    :rtype: List[str]
    """

    ensure_directory_exists(DEFAULT_OUTPUT_PATH)

    image_paths = []

    if color_func is None:
        color_func = colormap_color_func(color_map)

    for time_name, allocation_in_frame in position_in_frames.timelapse:
        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)
        allocation_in_frame_word_dict = allocation_in_frame.words

        for word, position in allocation_in_frame_word_dict.items():
            font_size = position[0]
            (x, y) = position[1]
            font = ImageFont.truetype(font_path, font_size)
            draw.text(
                (x, y),
                word,
                fill=color_func(
                    word=word, font_size=font_size, position=(x, y)
                ),
                font=font,
            )
        # save the image
        save_path = os.path.join(DEFAULT_OUTPUT_PATH, f"{time_name}.png")
        image.save(save_path)  # TODO: changing the file path
        image_paths.append(save_path)
    return image_paths
