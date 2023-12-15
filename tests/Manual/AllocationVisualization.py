"""
Observes how Allocation words
"""

import pathlib
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    allocate_all,
)
from AnimatedWordCloud.Animator.ImageCreator import create_images
from AnimatedWordCloud.Utils.Consts import (
    DEFAULT_ENG_FONT_PATH,
    DEFAULT_OUTPUT_PATH,
)
from tests.TestDataGetter import timelapses_test

timelapse = timelapses_test[0]

allocation_timelapse = allocate_all(
    timelapse, 50, 30, 10, 800, 600, DEFAULT_ENG_FONT_PATH, "magnetic", 100
)

create_images(
    allocation_timelapse,
    (800, 600),
    DEFAULT_ENG_FONT_PATH,
    "white",
)
