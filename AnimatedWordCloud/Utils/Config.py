# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Config class for passing parameters through the modules
"""

from typing import Literal
from AnimatedWordCloud.Utils.Consts import (
    DEFAULT_ENG_FONT_PATH,
    DEFAULT_OUTPUT_PATH,
)


class Config:
    """
    Config class for AnimatedWordCloud

    :param str font_path: Path to the font file.
        If None, default English font will be used.
    :param str output_path: Path to the output directory.
        If None, default output directory in this library will be used.
        Warning: This directory won't be deleted automatically.
            So, becareful of your storage.
    :param int max_words: Maximum number of words shown in each frame.
    :param int max_font_size: Maximum font size of the word.
    :param int min_font_size: Minimum font size of the word.
    :param int image_width: Width of the image.
    :param int image_height: Height of the image.
    :param str background_color: Background color of the image, default is "white".
    :param str color_map: Colormap to be used for the image, default is "magma".
    :param str allocation_stategy: Strategy to allocate words.
        There are "magnetic" only for now.
    :param int image_division: The number of division of the image.
        This is available for magnetic strategy only.
    :param str verbosity: Verbosity of the log.
        "silent" for no log, "minor" for only important logs, "debug" for all logs.
    """

    def __init__(
        self,
        font_path: str = None,
        output_path: str = None,
        max_words: int = 100,
        max_font_size: int = 50,
        min_font_size: int = 10,
        image_width=800,
        image_height=600,
        background_color: str = "white",
        color_map: str = "magma",
        allocation_strategy: Literal["magnetic"] = "magnetic",
        image_division: int = 300,
        verbosity: Literal["silent", "minor", "debug"] = "silent",
        transition_symbol: str = "_to_",
        duration_per_frame: int = 500,
        n_frames: int = 1,
        interpolation_method: str = "linear",
    ) -> None:
        # explanation written above

        # handle nones
        if font_path is None:
            font_path = DEFAULT_ENG_FONT_PATH
        if output_path is None:
            output_path = DEFAULT_OUTPUT_PATH
        self.font_path = font_path
        self.output_path = output_path
        self.max_words = max_words
        self.max_font_size = max_font_size
        self.min_font_size = min_font_size
        self.image_width = image_width
        self.image_height = image_height
        self.background_color = background_color
        self.color_map = color_map
        self.allocation_strategy = allocation_strategy
        self.image_division = image_division
        self.verbosity = verbosity
        self.transition_symbol = transition_symbol
        self.duration_per_frame = duration_per_frame
        self.n_frames = n_frames
        self.interpolation_method = interpolation_method
