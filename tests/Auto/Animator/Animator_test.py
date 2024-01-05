"""
Observes how animation words
"""

from AnimatedWordCloud import Config, animate
from tests.TestDataGetter import raw_timelapses_test

# testing data
raw_timelapse = raw_timelapses_test[0]

less_raw_timelapse = raw_timelapse[:2]

config = Config(max_words=50, max_font_size=20, min_font_size=10)


def test_animate():
    animate(less_raw_timelapse, config)
