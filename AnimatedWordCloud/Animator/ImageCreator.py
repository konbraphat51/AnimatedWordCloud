# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Create images of each frame
"""

from typing import List
from collections.abc import Iterable, Tuple
from AnimatedWordCloud.Animator import PositionInFrame, AllocationTimelapse
from PIL import Image, ImageDraw, ImageFont

def create_images(position_in_frames: AllocationTimelapse, image_size: Tuple[float, float], font_path: str, background_color: str = "white") -> List[str]:
    """
    Create images of each frame

    :param AllocationTimelapse position_in_frames: List of position/size data of each video frame.
    :return: The path of the images. The order of the list is the same as the order of the input.
    :rtype: List[str]
    """
    image_paths = []
    for time_name, allocation_in_frame in AllocationTimelapse.timelapse:
        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)
        for word, (font_size, (x, y)) in allocation_in_frame.words.items():
            font = ImageFont.truetype(font_path, font_size)
            draw.text((x, y), word, fill="black", font=font) #TODO:  Allow specifying the text color dynamically.
        # save the image
        image.save(f"{time_name}.png") #TODO: changing the file path
        image_paths.append(f"{time_name}.png")
    return image_paths
