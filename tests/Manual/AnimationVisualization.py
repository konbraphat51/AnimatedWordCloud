"""
Observes how animation words
"""

from AnimatedWordCloud import Config, animate
from tests.TestDataGetter import timelapses_test

# testing data
timelapse = timelapses_test[0]

config = Config(
    max_words=50, max_font_size=20, min_font_size=10, verbosity="debug"
)

animate(timelapse, config)
