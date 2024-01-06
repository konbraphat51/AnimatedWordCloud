# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Config class for passing parameters through the modules
"""

from __future__ import annotations
import random
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
    :param str transition_symbol: Symbol to be used for showing transition.
        It will be shown as "(former) [transition_symbol] (latter)".
    :param str starting_time_stamp: Time stamp of the starting time. (Before the first time stamp in the input data)
    :param int duration_per_interpolation_frame: Duration of each interpolation frame in milliseconds.
    :param int duration_per_static_frame: Duration of each static frame in milliseconds.
    :param int n_frames_for_interpolation: Number of frames in the animation.
    :param str interpolation_method: Method to interpolate the frames.
        There are "linear" only for now.
    :param bool drawing_time_stamp: Whether to draw time stamp on the image.
    :param str time_stamp_color: Color of the time stamp.
    :param int time_stamp_font_size: Font size of the time stamp.
        If None(default), it will be set to 75% of max_font_size
    :param tuple[int, int] time_stamp_position: Position of the time stamp.
        If None(default), it will be set to (image_width*0.75, image_height*0.75) which is right bottom.
    :param str intermediate_frames_id: Static images of each frame of itermediate product will be saved as "{intermediate_frames_id}_{frame_number}.png".
        If None(default), this will be set randomly.
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
        color_map: str = "Dark2",
        allocation_strategy: Literal["magnetic"] = "magnetic",
        image_division: int = 300,
        verbosity: Literal["silent", "minor", "debug"] = "silent",
        transition_symbol: str = " to ",
        starting_time_stamp: str = " ",
        duration_per_interpolation_frame: int = 50,
        duration_per_static_frame: int = 700,
        n_frames_for_interpolation: int = 20,
        interpolation_method: Literal["linear"] = "linear",
        drawing_time_stamp: bool = True,
        time_stamp_color: str = "black",
        time_stamp_font_size: int = None,
        time_stamp_position: tuple[int, int] = None,
        intermediate_frames_id: str = None,
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
        self.starting_time_stamp = starting_time_stamp
        self.duration_per_interpolation_frame = (
            duration_per_interpolation_frame
        )
        self.duration_per_static_frame = duration_per_static_frame
        self.n_frames_for_interpolation = n_frames_for_interpolation
        self.interpolation_method = interpolation_method
        self.drawing_time_stamp = drawing_time_stamp
        self.time_stamp_color = time_stamp_color

        self.time_stamp_font_size = self._compute_time_stamp_font_size(
            time_stamp_font_size
        )

        self.time_stamp_position = self._compute_time_stamp_position(
            time_stamp_position
        )

        self.intermediate_frames_id = self._compute_intermediate_frames_id(
            intermediate_frames_id
        )

    def _compute_time_stamp_font_size(
        self, time_stamp_font_size: int | None
    ) -> int:
        """
        Compute time_stamp_font_size from constructor argument.
        :param int time_stamp_font_size: Font size of the time stamp by the argument.
        :return: Font size of the time stamp.
        """
        if time_stamp_font_size is None:
            return int(self.max_font_size * 0.75)
        else:
            return time_stamp_font_size

    def _compute_time_stamp_position(
        self, time_stamp_position: tuple[int, int] | None
    ) -> tuple[int, int]:
        """
        Compute time_stamp_position from constructor argument.
        :param tuple[int, int] time_stamp_position: Position of the time stamp by the argument.
        :return: Position of the time stamp.
        """
        if time_stamp_position is None:
            return (
                self.image_width * 0.75,
                self.image_height * 0.75,
            )  # right bottom
        else:
            return time_stamp_position

    def _compute_intermediate_frames_id(
        self, intermediate_frames_id: str | None
    ) -> str:
        """
        returns intermediate_frames_id given from constructor
        set random value if intermediate_frames_id is None
        :param str|None intermediate_frames_id: intermediate_frames_id given
        :return: intermediate_frames_id computed
        :rtype: str
        """

        if intermediate_frames_id is None:
            # set randomly
            return str(random.randint(0, 1000000000))
        else:
            return intermediate_frames_id
