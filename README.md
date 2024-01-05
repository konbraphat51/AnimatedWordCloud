# AnimatedWordCloud ver 1.0.0

**UNDER CONSTRUCTION**

<a href="https://codeclimate.com/github/konbraphat51/AnimatedWordCloud/maintainability"><img src="https://api.codeclimate.com/v1/badges/7a03252f77e7af46dc0f/maintainability" /></a>
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/20a71da0d9d841a2af236f6362a08ae7)](https://app.codacy.com/gh/konbraphat51/AnimatedWordCloud/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![unit-test](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml/badge.svg?branch=main)](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml)[![codecov](https://codecov.io/gh/konbraphat51/AnimatedWordCloud/graph/badge.svg?token=4OOX0GSJDJ)](https://codecov.io/gh/konbraphat51/AnimatedWordCloud)

AnimatedWordCloud animates the timelapse of your words vector.

## Examples!

Using [Elon Musk's tweets](https://data.world/adamhelsinger/elon-musk-tweets-until-4-6-17).  
(C) Elon Musk

[GIF HERE]

## How to use?

### Requirements

Python (3.8 <= version <= 3.12)

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

timelapse = # adding time lapse data

#give the config to second parameter
animate(timelapse, config)
```

##### Parameters of `Config`

All has default value, so just edit what you need

| parameter name             | type            | meaning                                                                                                                                        |
| -------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| font_path                  | str             | Path to the font file.                                                                                                                         |
| output_path                | str             | Parh of the output directory                                                                                                                   |
| max_words                  | int             | max number of the words in the screen                                                                                                          |
| max_font_size              | int             | Maximum font size of the word                                                                                                                  |
| min_font_size              | int             | Minimum font size of the word                                                                                                                  |
| image_width                | int             | Width of the image                                                                                                                             |
| image_height               | int             | Height of the image                                                                                                                            |
| background_color           | str             | Background color. <br>This is based on [Pillow.Image.new()](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new)        |
| color_map                  | str             | color map used for coloring words<br>This is based on [matplotlib colormap](https://matplotlib.org/stable/users/explain/colors/colormaps.html) |
| allocation_strategy        | str(literal)    | allocation algorithm method. This will change the allocation of the words in the output. <br> There is "magnetic" now.                         |
| image_division             | int             | precision of allocation calculation. Higher the preciser, but calculation slower                                                               |
| verbosity                  | str(literal)    | logging.<br>silent: nothing<br>minor: bars to know the progress<br>debug: all progress. noisy                                                  |
| transition_symbol          | str             | written in the image                                                                                                                           |
| duration_per_frame         | int             | milliseconds per frame                                                                                                                         |
| n_frames_for_interpolation | int             | how many frames will be generated for interpolation between each frames                                                                        |
| interpolation_method       | str(literal)    | The method of making movement<br>There is "linear" now                                                                                         |
| drawing_time_stamp         | bool            | Whether to draw time stamp on the image                                                                                                        |
| time_stamp_color           | str             | Color of the time stamp. This is based on [`Pillow ImageColor`](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html#color-names) |
| time_stamp_font_size       | int             | Font size of the time stamp.<br>If None(default), it will be set to 75% of max_font_size                                                       |
| time_stamp_position        | tuple[int, int] | Position of the time stamp.<br>If None(default), it will be set to (image_width*0.75, image_height*0.75) which is right bottom.                |

## Want to contribute?

Look at [CONTRIBUTING.md](CONTRIBUTING.md) first.

### Maintainers

- [Konbraphat51](https://github.com/konbraphat51): Head Author  
  [![Konbraphat51 icon](https://github.com/konbraphat51.png)](https://github.com/konbraphat51)

- [SuperHotDogCat](https://github.com/SuperHotDogCat): Author  
  [![SuperHotDogCat](https://github.com/SuperHotDogCat.png)](https://github.com/SuperHotDogCat)

## Want to support?

**⭐Give this project a star⭐**  
This is our first OSS project, ⭐**star**⭐ would make us very happy⭐⭐⭐
