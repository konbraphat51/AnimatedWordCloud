# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Create images of each frame
"""
from typing import List
from collections.abc import Tuple
from AnimatedWordCloud.Animator import AllocationTimelapse
from PIL import Image, ImageDraw, ImageFont
from random import Random
import numpy as np
import os
from ..Utils.Consts import TMP_OUTPUT_PATH


class colormap_color_func(object):
    # https://github.com/amueller/word_cloud/blob/main/wordcloud/wordcloud.py#L91
    """Color func created from matplotlib colormap.

    Parameters
    ----------
    colormap : string or matplotlib colormap
        Colormap to sample from

    Example
    -------
    >>> WordCloud(color_func=colormap_color_func("magma"))

    """

    def __init__(self, color_map="magma"):
        import matplotlib.pyplot as plt

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
    image_size: Tuple[float, float],
    font_path: str,
    background_color: str = "white",
    color_map: str = "magma",
    color_func: function = None,
) -> List[str]:
    """
    Create images of each frame

    :param
    - AllocationTimelapse position_in_frames: List of position/size data of each video frame.
    - Tuple[float, float] image_size: Tuple of float values (width, height) representing the size of the image.
    - str font_path: Path to the font file.
    - str background_color:  Background color of the image, default is "white".
    - str color_map:  Colormap to be used for the image, default is "magma".
    - str color_func:  Custom function for color mapping, default is None.
    :return: The path of the images. The order of the list is the same as the order of the input.
    :rtype: List[str]
    """
    if not os.path.exists(TMP_OUTPUT_PATH):
        os.makedirs(TMP_OUTPUT_PATH)
    image_paths = []
    color_func = color_func or colormap_color_func(color_map)
    for time_name, allocation_in_frame in position_in_frames.timelapse:
        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)
        for word, (font_size, (x, y)) in allocation_in_frame.words.items():
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
        save_path = os.path.join(TMP_OUTPUT_PATH, f"{time_name}.png")
        image.save(save_path)  # TODO: changing the file path
        image_paths.append(save_path)
    return image_paths
