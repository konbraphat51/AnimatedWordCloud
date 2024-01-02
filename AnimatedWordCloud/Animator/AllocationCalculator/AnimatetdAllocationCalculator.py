from __future__ import annotations
import numpy as np
from AnimatedWordCloud.Utils import (
    AllocationTimelapse,
    AllocationInFrame,
    Config,
)


# For reviewers, I think that AllocationInFrame and AllocationTimelapse should be added to some methods. 


def get_setdiff(
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
    """
    np.setdiff1(x, y)'s returns an array x excluding the elements contained in array y.
    """
    from_words_to_be_added_key = np.setdiff1d(to_words, from_words)
    to_words_to_be_added_key = np.setdiff1d(from_words, to_words)
    return from_words_to_be_added_key, to_words_to_be_added_key


def add_key_in_allocation_frame(
    from_allocation_frame: AllocationInFrame,
    to_allocation_frame: AllocationInFrame,
    from_words_to_be_added_key: list[str],
    to_words_to_be_added_key: list[str],
) -> tuple[AllocationInFrame, AllocationInFrame]:
    """
    :param  AllocationInFrame from_allocation_frame, to_allocation_frame: start frame and end frame
    :param list[str] from_words_to_be_added_key, to_words_to_be_added_key: the keys to be added
    :return: AllocationInFrame from_allocation_frame, to_allocation_frame: start and end frame added to the necessary keys
    """
    for to_be_added_key in from_words_to_be_added_key:
        # add key in from_allocation_frame
        (font_size, (left_top)) = to_allocation_frame[to_be_added_key]
        from_allocation_frame.add(to_be_added_key, font_size, left_top)

    for to_be_added_key in to_words_to_be_added_key:
        # add key in to_allocation_frame
        (font_size, (left_top)) = from_allocation_frame[to_be_added_key]
        to_allocation_frame.add(to_be_added_key, font_size, left_top)

    return from_allocation_frame, to_allocation_frame


def calc_frame_value(
    from_value: float, to_value: float, index: int, n_frames: int
):
    """
    calculate interpolation's value
    """
    # Linear only for now
    value = from_value + index / (n_frames + 1) * (to_value - from_value)
    return value


def calc_added_frame(
    from_allocation_frame: AllocationInFrame,
    to_allocation_frame: AllocationInFrame,
    key: str,
    n_frames: int,
    index: int,
) -> tuple[float, float, float]:
    """
    calculate interpolation's value. font_size, x_pos, y_pos
    """
    # Linear only for now
    from_font_size = from_allocation_frame[key][0]
    to_font_size = to_allocation_frame[key][0]
    from_x_pos = from_allocation_frame[key][1][0]
    to_x_pos = to_allocation_frame[key][1][0]
    from_y_pos = from_allocation_frame[key][1][1]
    to_y_pos = to_allocation_frame[key][1][1]
    frame_font_size = calc_frame_value(
        from_font_size, to_font_size, index, n_frames
    )
    frame_x_pos = calc_frame_value(from_x_pos, to_x_pos, index, n_frames)
    frame_y_pos = calc_frame_value(from_y_pos, to_y_pos, index, n_frames)
    return frame_font_size, frame_x_pos, frame_y_pos


def get_interpolated_frames(
    from_allocation_frame: AllocationInFrame,
    to_allocation_frame: AllocationInFrame,
    from_day: str,
    to_day: str,
    config: Config,
) -> AllocationTimelapse:
    """
    get_interpolated_frames Algorithm:
    1. Align word counts in from_allocation_frame and to_allocation_frame
    2. Calculate interpolated frames using each of these methods for example, linear

    :param AllocationInFrame from_allocation_frame, to_allocation_frame: start frame and end frame
    :param Config config:
    :return AllocationTimelapse:
    """
    # Linear only for now
    n_frames = config.n_frames
    from_words_to_be_added_key, to_words_to_be_added_key = get_setdiff(
        from_allocation_frame, to_allocation_frame
    )
    from_allocation_frame, to_allocation_frame = add_key_in_allocation_frame(
        from_allocation_frame,
        to_allocation_frame,
        from_words_to_be_added_key,
        to_words_to_be_added_key,
    )
    to_be_added_frames: list[dict[str, tuple[float, tuple[float, float]]]] = [
        {} for _ in range(n_frames)
    ]  # not [{}] * n_frames
    # dict[str, tuple[float, tuple[float, float]]]: word -> (font size, left-top position)
    all_keys = list(from_allocation_frame.words.keys())
    for key in all_keys:
        for index in range(1, n_frames + 1):
            """
            from_value + index / (n_frames + 1) * (to_value - from_value)
            """
            # index: 1, 2, ..., n_frames, so 1 - indexed
            frame_font_size, frame_x_pos, frame_y_pos = calc_added_frame(
                from_allocation_frame,
                to_allocation_frame,
                key,
                n_frames,
                index,
            )
            to_be_added_frames[index - 1][key] = (
                frame_font_size,
                (frame_x_pos, frame_y_pos),
            )
    # Generate interpolated_frames
    interpolated_frames: AllocationTimelapse = AllocationTimelapse()
    for index, to_be_added_frame in enumerate(to_be_added_frames):
        to_be_added_allocation_frame = AllocationInFrame()
        to_be_added_allocation_frame.words = to_be_added_frame
        transition_day = from_day + config.transition_symbol + to_day
        interpolated_frames.add(transition_day, to_be_added_allocation_frame)
    return interpolated_frames


def animated_allocate(
    allocation_timelapse: AllocationTimelapse, config: Config
) -> AllocationTimelapse:
    """
    :param AllocationTimelapse allocation_timelapse: static allocations already calculated (AllocationTimelapse)
    :param Config config:
    :return: AllocationTimelapse which interpolation allocation for animation inserted (AllocationTimelapse)
    :rtype: AllocationTimelapse
    """

    # Branching by interpolation_method
    n_timestamps = len(
        allocation_timelapse.timelapse
    )  # get the number of timestamps
    animated_allocated_timelapse_data: list[tuple(str, AllocationInFrame)] = []
    if config.interpolation_method == "linear":
        """
        Interpolate between timestamps. the positions of words are changed by linear.
        """
        for index in range(n_timestamps - 1):
            from_allocation_frame = allocation_timelapse.get_frame(index)
            to_allocation_frame = allocation_timelapse.get_frame(index + 1)
            from_day = allocation_timelapse.timelapse[index][0]
            to_day = allocation_timelapse.timelapse[index + 1][0]
            interpolated_frames: AllocationTimelapse = get_interpolated_frames(
                from_allocation_frame,
                to_allocation_frame,
                from_day,
                to_day,
                config,
            )

            animated_allocated_timelapse_data = (
                animated_allocated_timelapse_data
                + [allocation_timelapse.timelapse[index]]
                + interpolated_frames.timelapse
            )
        animated_allocated_timelapse_data = (
            animated_allocated_timelapse_data
            + [allocation_timelapse.timelapse[index + 1]]
        )
        animated_allocated_timelapse = AllocationTimelapse()
        animated_allocated_timelapse.timelapse = (
            animated_allocated_timelapse_data
        )
        return animated_allocated_timelapse
    else:
        raise NotImplementedError()
