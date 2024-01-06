# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate interpolated allocations between timestamps
"""

from __future__ import annotations
import numpy as np
from AnimatedWordCloud.Utils import (
    AllocationTimelapse,
    AllocationInFrame,
    Config,
)


def animated_allocate(
    allocation_timelapse: AllocationTimelapse, config: Config
) -> AllocationTimelapse:
    """
    :param AllocationTimelapse allocation_timelapse: static allocations already calculated (AllocationTimelapse)
    :param Config config:
    :return: AllocationTimelapse which interpolation allocation for animation inserted (AllocationTimelapse)
    :rtype: AllocationTimelapse
    """

    # final output
    timelapse_output: AllocationTimelapse = AllocationTimelapse()

    # Branching by interpolation_method
    n_timestamps = len(
        allocation_timelapse.timelapse
    )  # get the number of timestamps

    # Interpolate between timestamps. the positions of words are changed by linear.
    for index in range(n_timestamps - 1):
        # get static frame data
        from_allocation_frame = allocation_timelapse.get_frame(index)
        to_allocation_frame = allocation_timelapse.get_frame(index + 1)
        time_name_from = allocation_timelapse.timelapse[index][0]
        time_name_to = allocation_timelapse.timelapse[index + 1][0]

        # interpolate between two frames
        interpolated_frames: list[
            AllocationInFrame
        ] = _get_interpolated_frames(
            from_allocation_frame,
            to_allocation_frame,
            config,
        )

        # add static frame first
        timelapse_output.add(time_name_from, from_allocation_frame)

        # add interpolated frames
        time_name = time_name_from + config.transition_symbol + time_name_to
        for interpolated_frame in interpolated_frames:
            timelapse_output.add(time_name, interpolated_frame)

    # add last static frame
    timelapse_output.add(time_name_to, to_allocation_frame)

    return timelapse_output


def _get_setdiff(
    from_allocation_frame: AllocationInFrame,
    to_allocation_frame: AllocationInFrame,
) -> tuple[list[str], list[str]]:
    """
    Extract the keys to be added

    :param AllocationInFrame from_allocation_frame, to_allocation_frame: start frame and end frame
    :return: the keys to be added
    """
    from_words: list[str] = list(from_allocation_frame.words.keys())
    to_words: list[str] = list(to_allocation_frame.words.keys())

    # np.setdiff1(x, y)'s returns an array x excluding the elements contained in array y.
    from_words_to_be_added_key = np.setdiff1d(to_words, from_words)
    to_words_to_be_added_key = np.setdiff1d(from_words, to_words)
    return from_words_to_be_added_key, to_words_to_be_added_key


def _add_key_in_allocation_frame(
    from_allocation_frame: AllocationInFrame,
    to_allocation_frame: AllocationInFrame,
    from_words_to_be_added_key: list[str],
    to_words_to_be_added_key: list[str],
) -> tuple[AllocationInFrame, AllocationInFrame]:
    """
    :param  AllocationInFrame from_allocation_frame, to_allocation_frame: start frame and end frame
    :param list[str] from_words_to_be_added_key, to_words_to_be_added_key: the keys to be added
    :return: AllocationInFrame from_allocation_frame, to_allocation_frame: start and end frame added to the necessary keys
    :rtype: tuple[AllocationInFrame, AllocationInFrame]
    """
    for to_be_added_key in from_words_to_be_added_key:
        # add key in from_allocation_frame
        (font_size, left_top) = to_allocation_frame[to_be_added_key]
        from_allocation_frame.add(to_be_added_key, font_size, left_top)

    for to_be_added_key in to_words_to_be_added_key:
        # add key in to_allocation_frame
        (font_size, left_top) = from_allocation_frame[to_be_added_key]
        to_allocation_frame.add(to_be_added_key, font_size, left_top)

    return from_allocation_frame, to_allocation_frame


def _calc_frame_value(
    from_value: float, to_value: float, index: int, config: Config
) -> float:
    """
    :param float from_value, to_value: font_size, x_position, or y_position
    :param int index: interpolation frame index
    :param Config config used for n_frames_for_interpolation and interpolation_method
    :return: calculated interpolation's value
    :rtype: float

    Linear only for now
    Add non-Linear interpolation processes in the future.
    """
    if config.interpolation_method == "linear":
        value = _calc_linear(from_value, to_value, index, config)
    else:
        raise NotImplementedError()
    return value


def _calc_linear(
    from_value: float, to_value: float, index: int, config: Config
):
    """
    :param float from_value, to_value: font_size, x_position, or y_position
    :param int index: interpolation frame index
    :param Config config used for n_frames_for_interpolation
    :return: calculated linear interpolation's value
    :rtype: float

    Linear only for now
    Add non-Linear interpolation processes in the future.
    """
    value = from_value + index / (config.n_frames_for_interpolation + 1) * (
        to_value - from_value
    )
    return value


def _calc_added_frame(
    from_allocation_frame: AllocationInFrame,
    to_allocation_frame: AllocationInFrame,
    key: str,
    index: int,
    config: Config,
) -> tuple[float, float, float]:
    """
    :param float from_allocation_frame, to_allocation_frame: start frame and end frame
    :param str key: a focused word. It's interpolation font size and positions are calculated.
    :param int index: interpolation frame index
    :param Config config: used for the argument of _calc_frame_value
    :return: calculated interpolation's values (frame_font_size, frame_x_pos, frame_y_pos)
    :rtype: tuple[float, float, float]
    """
    from_font_size = from_allocation_frame[key][0]
    to_font_size = to_allocation_frame[key][0]
    from_x_pos = from_allocation_frame[key][1][0]
    to_x_pos = to_allocation_frame[key][1][0]
    from_y_pos = from_allocation_frame[key][1][1]
    to_y_pos = to_allocation_frame[key][1][1]
    frame_font_size = _calc_frame_value(
        from_font_size, to_font_size, index, config
    )
    frame_x_pos = _calc_frame_value(from_x_pos, to_x_pos, index, config)
    frame_y_pos = _calc_frame_value(from_y_pos, to_y_pos, index, config)
    return frame_font_size, frame_x_pos, frame_y_pos


def _get_interpolated_frames(
    from_allocation_frame: AllocationInFrame,
    to_allocation_frame: AllocationInFrame,
    config: Config,
) -> list[AllocationInFrame]:
    """
    get_interpolated_frames Algorithm:
    1. Align word counts in from_allocation_frame and to_allocation_frame
    2. Calculate interpolated frames using each of these methods for example, linear

    :param AllocationInFrame from_allocation_frame, to_allocation_frame: start frame and end frame
    :param Config config:
    :return: interpolated frames
    :rtype: list[AllocationInFrame]
    """
    # Linear only for now
    n_frames_for_interpolation = config.n_frames_for_interpolation
    from_words_to_be_added_key, to_words_to_be_added_key = _get_setdiff(
        from_allocation_frame, to_allocation_frame
    )
    from_allocation_frame, to_allocation_frame = _add_key_in_allocation_frame(
        from_allocation_frame,
        to_allocation_frame,
        from_words_to_be_added_key,
        to_words_to_be_added_key,
    )
    to_be_added_frames: list[dict[str, tuple[float, tuple[float, float]]]] = [
        {} for _ in range(n_frames_for_interpolation)
    ]  # not [{}] * n_frames_for_interpolation
    # dict[str, tuple[float, tuple[float, float]]]: word -> (font size, left-top position)
    all_keys = list(from_allocation_frame.words.keys())
    for key in all_keys:
        for index in range(1, n_frames_for_interpolation + 1):
            # from_value + index / (n_frames_for_interpolation + 1) * (to_value - from_value)
            # index: 1, 2, ..., n_frames_for_interpolation, so 1 - indexed
            frame_font_size, frame_x_pos, frame_y_pos = _calc_added_frame(
                from_allocation_frame, to_allocation_frame, key, index, config
            )
            to_be_added_frames[index - 1][key] = (
                frame_font_size,
                (frame_x_pos, frame_y_pos),
            )

    # Generate interpolated_frames as AllocationInFrame
    output = []
    for index, to_be_added_frame in enumerate(to_be_added_frames):
        to_be_added_allocation_frame = AllocationInFrame(
            from_static_allocation=False
        )
        to_be_added_allocation_frame.words = to_be_added_frame
        output.append(to_be_added_allocation_frame)

    return output
