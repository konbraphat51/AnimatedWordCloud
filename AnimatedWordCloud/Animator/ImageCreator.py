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
import hashlib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from AnimatedWordCloud.Utils import (
    ensure_directory_exists,
    Config,
    AllocationTimelapse,
    AllocationInFrame,
)


class colormap_color_func(object):
    # https://github.com/amueller/word_cloud/blob/main/wordcloud/wordcloud.py#L91
    """Color func created from matplotlib colormap.

    :param colormap : string or matplotlib colormap
        Colormap to sample from
    """

    def __init__(self, color_map="dark2"):
        self.color_map = plt.get_cmap(name=color_map)

    def __call__(
        self, word: str, font_size, position, random_state=None, **kwargs
    ):
        # MD5ハッシュを計算
        md5_hash = hashlib.md5(word.encode()).hexdigest()
        # 16進数を10進数に変換
        decimal_value = int(md5_hash, 16)
        # 10進数を0から1の範囲に正規化
        normalized_value = decimal_value / (16**32 - 1)
        r, g, b, _ = np.maximum(
            0, 255 * np.array(self.color_map(normalized_value))
        )
        return "rgb({:.0f}, {:.0f}, {:.0f})".format(r, g, b)


def create_image(
    allocation_in_frame: AllocationInFrame,
    time_name: str,
    config: Config,
    color_func=None,
) -> str:
    """
    Create image of a frame

    :param AllocationInFrame allocation_in_frame: Position/size data of a video frame.
    :param str time_name: Name of the frame
    :param Tuple[float, float] image_size: Tuple of float values (width, height) representing the size of the image.
    :param str font_path: Path to the font file.
    :param str background_color:  Background color of the image, default is "white".
    :param str color_map:  Colormap to be used for the image, default is "magma".
    :param str color_func:  Custom function for color mapping, default is None.
    :return: The path of the image.
    :rtype: str
    """
    if color_func is None:
        color_func = colormap_color_func(config.color_map)

    image = Image.new(
        "RGB",
        (config.image_width, config.image_height),
        config.background_color,
    )
    draw = ImageDraw.Draw(image)
    allocation_in_frame_word_dict = allocation_in_frame.words

    for word, position in allocation_in_frame_word_dict.items():
        font_size = position[0]
        (x, y) = position[1]
        font = ImageFont.truetype(config.font_path, font_size)
        draw.text(
            (x, y),
            word,
            fill=color_func(word=word, font_size=font_size, position=(x, y)),
            font=font,
        )
    # save the image
    save_path = os.path.join(config.output_path, f"{time_name}.png")
    image.save(save_path)  # TODO: changing the file path

    return save_path


def create_images(
    position_in_frames: AllocationTimelapse,
    config: Config,
    color_func=None,
) -> list[str]:
    """
    Create images of each frame

    :param AllocationTimelapse position_in_frames: List of position/size data of each video frame.
    :param Config config: Config instance
    :param object color_func:  Custom function for color mapping, default is None.
    :return: The path of the images. The order of the list is the same as the order of the input.
    :rtype: list[str]
    """

    ensure_directory_exists(config.output_path)

    image_paths = []

    for time_name, allocation_in_frame in position_in_frames.timelapse:
        save_path = create_image(
            allocation_in_frame=allocation_in_frame,
            time_name=time_name,
            config=config,
            color_func=color_func,
        )

        image_paths.append(save_path)

    return image_paths
