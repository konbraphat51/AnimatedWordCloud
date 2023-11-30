import os
import glob
import subprocess
from pathlib import Path
from AnimatedWordCloud.Animator.ImageCreator import create_images
from AnimatedWordCloud.Animator.AllocationCalculator.AllocationData import (
    AllocationTimelapse,
    AllocationInFrame,
)
from AnimatedWordCloud.Utils.Consts import (
    DEFAULT_ENG_FONT_PATH,
)
from AnimatedWordCloud.Animator.AnimationIntegrator import integrate_images

DIR = Path(__file__).parent
def test_integrateimages():
    image_path0 = os.path.join(DIR, "tests0.png")
    image_path1 = os.path.join(DIR, "tests1.png")
    image_paths: list[str] = [image_path0, image_path1]  # temporary path
    filename: str = "output.gif"
    duration_per_frame: int = 500
    assert integrate_images(image_paths, filename, duration_per_frame) == None

def test_imagecreator_and_integrateimages():
    # test create_images function
    position_in_frames = AllocationTimelapse()
    allocation_in_frame = AllocationInFrame()
    allocation_in_frame.words = {"word": (30, (50, 50))}  # dictionary
    position_in_frames.add("2023_04_01", allocation_in_frame)
    image_paths = create_images(
        position_in_frames,
        image_size=(100, 100),
        font_path=DEFAULT_ENG_FONT_PATH,
    )
    filename: str = "output.gif"
    duration_per_frame: int = 500
    assert integrate_images(image_paths, filename, duration_per_frame) == None
