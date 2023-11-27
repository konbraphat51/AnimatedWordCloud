# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Integrates the images into a single video (gif)
"""

from typing import List
import cv2


def integrate_images(
    image_paths: List[str],
    filename: str,
) -> None:
    """
    Create images of each frame

    :param
    List[str] image_paths: List of image_paths created by AnimatedWordCloud.Animator.ImageCreator.create_images.
    str filename: output filename.
    :return: None
    """

    images = [cv2.imread(path) for path in image_paths]
    height, width, layers = images[0].shape

    gif = cv2.VideoWriter(
        filename,
        cv2.VideoWriter_fourcc(*"GIF"),
        1,
        (width, height),
    )

    for image in images:
        gif.write(image)
    cv2.destroyAllWindows()
    gif.release()

    return