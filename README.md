# AnimatedWordCloud ver 1.0.0

**UNDER CONSTRUCTION**

<a href="https://codeclimate.com/github/konbraphat51/AnimatedWordCloud/maintainability"><img src="https://api.codeclimate.com/v1/badges/7a03252f77e7af46dc0f/maintainability" /></a>
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/20a71da0d9d841a2af236f6362a08ae7)](https://app.codacy.com/gh/konbraphat51/AnimatedWordCloud/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![unit-test](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml/badge.svg?branch=main)](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml)[![codecov](https://codecov.io/gh/konbraphat51/AnimatedWordCloud/graph/badge.svg?token=4OOX0GSJDJ)](https://codecov.io/gh/konbraphat51/AnimatedWordCloud)

AnimatedWordCloud animates the timelapse of your words vector.

## How to use?

### install

(scheduled)

```
pip install AnimatedWordCloud
```

### coding

#### Using default configuration

```python
from AnimatedWordCloud import animate

# data must be list[("time name", dict[str, float])]
timelapse_wordvector = [
    (
        "time_0",
        {
            "hanshin":0.334,
            "chiba":0.226
        }
    ),
    (
        "time_1",
        {
            "hanshin":0.874,
            "fujinami":0.609
        }
    ),
    (
        "time_2",
        {
            "fujinami":0.9,
            "major":0.4
        }
    )
]

# animate!
# the animation gif path is in this variable!
path = animate(timelapse_wordvector)
```

#### Editing configuration

```python
from AnimatedWordCloud import animate, Config

config = Config(
    what_you_want_to_edit = editing_value
)

#give the config to second parameter
animate(timelapse, config)
```
