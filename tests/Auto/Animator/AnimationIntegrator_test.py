from AnimatedWordCloud.Animator.AnimationIntegrator import integrate_images
from typing import List
from pathlib import Path
import os

DIR = Path(__file__).parent
def test_integrateimages():
    image_path0 = os.path.join(DIR, "tests0.png")
    image_path1 = os.path.join(DIR, "tests1.png")
    image_paths: List[str] = [image_path0, image_path1]  # temporary path
    print(image_path1)
    filename: str = "output.gif"
    duration: int = 500
    assert integrate_images(image_paths, filename, duration) == None