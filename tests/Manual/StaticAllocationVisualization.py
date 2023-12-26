"""
Observes how Allocation words
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    allocate_all,
)
from AnimatedWordCloud.Animator.ImageCreator import create_images
from AnimatedWordCloud.Utils import Config
from tests.TestDataGetter import timelapses_test

timelapse = timelapses_test[0]

config = Config(max_words=50, max_font_size=20, min_font_size=10)

allocation_timelapse = allocate_all(timelapse, config)

create_images(allocation_timelapse, config)
