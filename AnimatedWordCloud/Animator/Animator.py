# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Heart of animation flow
Get the input and returns the output, 
    calling each modules
"""

from __future__ import annotations
from typing import Iterable
from AnimatedWordCloud.Utils import Config, TimelapseWordVector
from AnimatedWordCloud.Animator.AllocationCalculator import allocate
from AnimatedWordCloud.Animator.ImageCreator import create_images
from AnimatedWordCloud.Animator.AnimationIntegrator import integrate_images


def animate(
    word_vector_timelapse: Iterable[tuple[str, dict[str, float]]],
    config: Config = None,
    output_filename: str = "output.gif",
) -> str:
    """
    Create an animation of word cloud,
        from the timelapse data of words vectors

    This function will call each modules in the right order,
        and return the animation path

    :param Iterable[tuple[str, dict[str, float]]] word_vector_timelapse:
    Timelapse data of word vectors.
    The data structure is a list of tuples,
        which includes "name of the time(str)" and "word vector(Dict[str, float])"
    :param Config config: Configuration of the animation. If None, default config will be used.
    :param str output_filename: Filename of the animation file.
    :return: The path of the animation file.
    :rtype: str
    """

    # use default config if not specified
    if config is None:
        config = Config()

    # convert data to TimelapseWordVector
    timelapse_word_vector = TimelapseWordVector.convert_from_dicts_list(
        word_vector_timelapse
    )

    # Calculate allocation
    allocation_timelapse = allocate(timelapse_word_vector, config)

    # to images
    image_paths = create_images(allocation_timelapse, config)

    # to one animation file
    animation_path = integrate_images(
        image_paths, allocation_timelapse, config, filename=output_filename
    )

    if config.verbosity == "minor" or config.verbosity == "debug":
        _success_message()

    return animation_path


def _success_message(animation_path: str) -> None:
    """
    print success message.

    :param str animation_path: animation saved path
    :return: None
    :rtype: None
    """
    success_message = (
        f"your animation was successfully saved in {animation_path}"
    )
    string_frame_over = (
        "-" * (len(success_message) // 2)
        + "Success!"
        + "-" * (len(success_message) // 2)
    )
    string_frame_under = "-" * len(success_message + "Success!")
    success_message = " " * 4 + success_message + " " * 4
    print(string_frame_over)
    print(success_message)
    print(string_frame_under)
