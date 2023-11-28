from AnimatedWordCloud.Animator.AnimationIntegrator import integrate_images
from typing import List
from PIL import Image

def test_integrateimages():
    image_paths: List[str] = ["SnapShot.png", "SnapShot.jpg"]
    filename: str = "output.gif"
    duration: int = 500
    assert integrate_images(image_paths, filename, duration) == None