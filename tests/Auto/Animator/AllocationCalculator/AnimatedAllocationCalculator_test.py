from __future__ import annotations
import numpy as np
from AnimatedWordCloud.Utils import (
    AllocationTimelapse,
    AllocationInFrame,
    Config,
)
from AnimatedWordCloud.Animator.AllocationCalculator.AnimatetdAllocationCalculator import (
    _get_setdiff,
    _add_key_in_allocation_frame,
    _calc_added_frame,
    _get_interpolated_frames,
    animated_allocate,
)


def get_setdiff_test():
    allocationframe1 = AllocationInFrame()
    allocationframe2 = AllocationInFrame()
    allocationframe1.add("apple", 10, (10, 10))
    allocationframe1.add("banana", 10, (10, 10))
    allocationframe1.add("grape", 10, (10, 10))
    allocationframe2.add("apple", 10, (10, 10))
    allocationframe2.add("banana", 10, (10, 10))
    allocationframe2.add("orange", 10, (10, 10))
    from_words_to_be_added_key, to_words_to_be_added_key = _get_setdiff(
        allocationframe1, allocationframe2
    )
    assert from_words_to_be_added_key == ["orange"]
    assert to_words_to_be_added_key == ["grape"]


def add_key_in_allocation_frame_test():
    allocationframe1 = AllocationInFrame()
    allocationframe2 = AllocationInFrame()
    allocationframe1.add("apple", 10, (10, 10))
    allocationframe1.add("banana", 10, (10, 10))
    allocationframe1.add("grape", 10, (10, 10))
    allocationframe2.add("apple", 10, (10, 10))
    allocationframe2.add("banana", 10, (10, 10))
    allocationframe2.add("orange", 10, (10, 10))
    from_words_to_be_added_key, to_words_to_be_added_key = _get_setdiff(
        allocationframe1, allocationframe2
    )
    from_allocation_frame, to_allocation_frame = _add_key_in_allocation_frame(
        allocationframe1,
        allocationframe2,
        from_words_to_be_added_key,
        to_words_to_be_added_key,
    )
    assert from_allocation_frame.words == {
        "apple": (10, (10, 10)),
        "banana": (10, (10, 10)),
        "grape": (10, (10, 10)),
        "orange": (10, (10, 10)),
    }
    assert to_allocation_frame.words == {
        "apple": (10, (10, 10)),
        "banana": (10, (10, 10)),
        "orange": (10, (10, 10)),
        "grape": (10, (10, 10)),
    }


def calc_added_value_test():
    allocationframe1 = AllocationInFrame()
    allocationframe2 = AllocationInFrame()
    allocationframe1.add("apple", 10, (10, 10))
    allocationframe1.add("banana", 10, (10, 10))
    allocationframe1.add("grape", 10, (10, 10))
    allocationframe2.add("apple", 20, (20, 30))
    allocationframe2.add("banana", 10, (10, 10))
    allocationframe2.add("orange", 10, (10, 10))
    from_words_to_be_added_key, to_words_to_be_added_key = _get_setdiff(
        allocationframe1, allocationframe2
    )
    from_allocation_frame, to_allocation_frame = _add_key_in_allocation_frame(
        allocationframe1,
        allocationframe2,
        from_words_to_be_added_key,
        to_words_to_be_added_key,
    )
    config = Config()
    key = "apple"
    index = 1
    assert index >= 1
    n_frames = 1
    frame_font_size, frame_x_pos, frame_y_pos = _calc_added_frame(
        from_allocation_frame, to_allocation_frame, key, index, config
    )
    assert frame_font_size == 15
    assert frame_x_pos == 15
    assert frame_y_pos == 20
    key = "banana"
    index = 1
    config.n_frames = 20
    frame_font_size, frame_x_pos, frame_y_pos = _calc_added_frame(
        from_allocation_frame,
        to_allocation_frame,
        key,
        index,
        config,
    )
    assert frame_font_size == 10
    assert frame_x_pos == 10
    assert frame_y_pos == 10


def get_interpolated_frames_test():
    config = Config()
    config.n_frames = 1
    from_day = "2024-1-1"
    to_day = "2024-1-2"
    allocationframe1 = AllocationInFrame()
    allocationframe2 = AllocationInFrame()
    allocationframe1.add("apple", 10, (10, 10))
    allocationframe1.add("banana", 10, (10, 10))
    allocationframe1.add("grape", 10, (10, 10))
    allocationframe2.add("apple", 20, (20, 30))
    allocationframe2.add("banana", 10, (10, 10))
    allocationframe2.add("orange", 10, (10, 10))
    from_words_to_be_added_key, to_words_to_be_added_key = _get_setdiff(
        allocationframe1, allocationframe2
    )
    from_allocation_frame, to_allocation_frame = _add_key_in_allocation_frame(
        allocationframe1,
        allocationframe2,
        from_words_to_be_added_key,
        to_words_to_be_added_key,
    )

    interpolated_frames = _get_interpolated_frames(
        from_allocation_frame, to_allocation_frame, from_day, to_day, config
    )
    assert interpolated_frames.timelapse[0][0] == "2024-1-1_to_2024-1-2"
    assert interpolated_frames.timelapse[0][1].words == {
        "apple": (15, (15, 20)),
        "banana": (10, (10, 10)),
        "grape": (10, (10, 10)),
        "orange": (10, (10, 10)),
    }
    config.n_frames = 2
    interpolated_frames = _get_interpolated_frames(
        from_allocation_frame, to_allocation_frame, from_day, to_day, config
    )
    assert len(interpolated_frames.timelapse) == 2
    print(interpolated_frames.timelapse[0][1].words)
    print(interpolated_frames.timelapse[1][1].words)


def animated_allocate_test():
    static_timelapse = AllocationTimelapse()
    from_day = "2024-1-1"
    to_day = "2024-1-2"
    allocationframe1 = AllocationInFrame()
    allocationframe2 = AllocationInFrame()
    allocationframe1.add("apple", 10, (10, 10))
    allocationframe1.add("banana", 10, (10, 10))
    allocationframe1.add("grape", 10, (10, 10))
    allocationframe2.add("apple", 20, (20, 30))
    allocationframe2.add("banana", 10, (10, 10))
    allocationframe2.add("orange", 10, (10, 10))
    static_timelapse.add(from_day, allocationframe1)
    static_timelapse.add(to_day, allocationframe2)
    config = Config()
    config.n_frames = 1
    config.interpolation_method = "linear"
    animated_timelapse: AllocationTimelapse = animated_allocate(
        static_timelapse, config
    )
    assert len(animated_timelapse.timelapse) == 3
    config.n_frames = 3
    animated_timelapse: AllocationTimelapse = animated_allocate(
        static_timelapse, config
    )
    assert len(animated_timelapse.timelapse) == 5
