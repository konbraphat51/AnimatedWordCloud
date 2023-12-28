import os
import glob
import subprocess
from pathlib import Path
from AnimatedWordCloud.Utils.Data import (
    AllocationTimelapse,
    AllocationInFrame,
)
from AnimatedWordCloud.Utils.Consts import (
    DEFAULT_ENG_FONT_PATH,
)
from AnimatedWordCloud.Animator.AnimationIntegrator import integrate_images
from AnimatedWordCloud.Animator.ImageCreator import create_images
from AnimatedWordCloud.Utils import Config

DIR = Path(__file__).parent


def test_integrateimages():
    config = Config(output_path="output.gif")
    image_path0 = os.path.join(DIR, "tests0.png")
    image_path1 = os.path.join(DIR, "tests1.png")
    image_paths: list[str] = [image_path0, image_path1]  # temporary path
    assert integrate_images(image_paths, config) == None


def test_imagecreator_and_integrateimages():
    # test create_images function
    config = Config(output_path="output.gif")
    position_in_frames = AllocationTimelapse()
    allocation_in_frame = AllocationInFrame()
    allocation_in_frame.words = {"word": (30, (50, 50))}  # dictionary
    position_in_frames.add("2023_04_01", allocation_in_frame)
    image_paths = create_images(
        position_in_frames,
        config,
    )
    assert integrate_images(image_paths, config) == None
