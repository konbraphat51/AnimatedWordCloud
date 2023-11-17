# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the TimelapsedWordVector classes
"""


from AnimatedWordCloud.Animator.TimelapseWordVector import (
    WordVector,
    TimeFrame,
    TimelapseWordVector,
)


# test WordVector


def test_wordvector():
    # test add
    instance = WordVector()

    instance.add("test", 1)
    instance.add("test2", 4)
    instance.add("test3", 3)
    instance.add("test4", 2)

    assert instance._word_heap == [
        (-4, "test2"),
        (-3, "test3"),
        (-2, "test4"),
        (-1, "test"),
    ]
    assert instance._word_dictionary == {
        "test": 1,
        "test2": 4,
        "test3": 3,
        "test4": 2,
    }

    # test add_multiple
    instance = WordVector()

    instance.add_multiple(
        [("test", 1), ("test2", 4), ("test3", 3), ("test4", 2)]
    )

    assert instance._word_heap == [
        (-4, "test2"),
        (-3, "test3"),
        (-2, "test4"),
        (-1, "test"),
    ]
    assert instance._word_dictionary == {
        "test": 1,
        "test2": 4,
        "test3": 3,
        "test4": 2,
    }

    # test get ranking
    assert instance.get_ranking(0, 2) == [("test2", 4), ("test3", 3)]
    assert instance.get_ranking(1, 3) == [("test3", 3), ("test4", 2)]
    assert instance.get_ranking(1, -1) == [
        ("test3", 3),
        ("test4", 2),
        ("test", 1),
    ]

    # test get_weight
    assert instance.get_weight("test") == 1

    # test convert_from_dict
    instance = WordVector.convert_from_dict(
        {"test": 1, "test2": 4, "test3": 3, "test4": 2}
    )

    assert instance._word_heap == [
        (-4, "test2"),
        (-3, "test3"),
        (-2, "test4"),
        (-1, "test"),
    ]
    assert instance._word_dictionary == {
        "test": 1,
        "test2": 4,
        "test3": 3,
        "test4": 2,
    }


def test_timeframe():
    # demo word vector
    test_dict = {"test": 1, "test2": 4, "test3": 3, "test4": 2}
    word_vector = WordVector.convert_from_dict(test_dict)

    # test constructor
    instance = TimeFrame("test_time", word_vector)

    assert instance.time_name == "test_time"
    assert instance.word_vector.get_ranking(0, -1) == [
        ("test2", 4),
        ("test3", 3),
        ("test4", 2),
        ("test", 1),
    ]

    # test convert_from_dict
    assert TimeFrame.convert_from_dict(
        "test_time", test_dict
    ).word_vector.get_ranking(0, -1) == [
        ("test2", 4),
        ("test3", 3),
        ("test4", 2),
        ("test", 1),
    ]

    assert (
        TimeFrame.convert_from_dict("test_time", test_dict).time_name
        == "test_time"
    )

    # test convert_from_tup_dict
    assert TimeFrame.convert_from_tup_dict(
        ["test_time", test_dict]
    ).word_vector.get_ranking(0, -1) == [
        ("test2", 4),
        ("test3", 3),
        ("test4", 2),
        ("test", 1),
    ]


def test_timelapsewordvector():
    # demo word vector
    test_dict0 = {"test": 1, "test2": 4, "test3": 3, "test4": 2}
    test_dict1 = {"test": 4, "test2": 1, "test3": -2, "test4": 10}
    word_vector0 = WordVector.convert_from_dict(test_dict0)
    word_vector1 = WordVector.convert_from_dict(test_dict1)

    time_frame0 = TimeFrame("test_time", word_vector0)
    time_frame1 = TimeFrame("test_time", word_vector1)

    # test add_time_frame, __getitem__
    instance = TimelapseWordVector()
    instance.add_time_frame(time_frame0)
    instance.add_time_frame(time_frame1)

    assert instance[0].word_vector.get_ranking(0, -1) == [
        ("test2", 4),
        ("test3", 3),
        ("test4", 2),
        ("test", 1),
    ]

    assert instance[0].time_name == "test_time"

    assert instance[1].word_vector.get_ranking(0, -1) == [
        ("test4", 10),
        ("test", 4),
        ("test2", 1),
        ("test3", -2),
    ]

    # test __len__
    assert len(instance) == 2

    # test convert_from_dicts_list
    dicts_list = [("time0", test_dict0), ("test_dict1", test_dict1)]

    assert TimelapseWordVector.convert_from_dicts_list(dicts_list)[
        0
    ].word_vector.get_ranking(0, -1) == [
        ("test2", 4),
        ("test3", 3),
        ("test4", 2),
        ("test", 1),
    ]
