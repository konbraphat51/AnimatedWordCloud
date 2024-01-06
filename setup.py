# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Setup script
"""
from setuptools import find_packages, setup
from pathlib import Path

# get README.md
readme = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")


def requirements_from_file(file_name):
    return open(file_name).read().splitlines()


setup(
    name="AnimatedWordCloudTimelapse",
    version="1.0.4",
    description="Animate a timelapse of word cloud",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="konbraphat51, superhotdogcat",
    author_email="konbraphat51@gmail.com, siromisochan@gmail.com",
    url="https://github.com/konbraphat51/AnimatedWordCloud/tree/main",
    packages=find_packages(exclude=["tests", "Docs"]),
    test_suite="tests",
    python_requires=">=3.8",
    package_data={"AnimatedWordCloud": ["Assets/**"]},
    include_package_data=True,
    install_requires=requirements_from_file("requirements.txt"),
    license="MIT License",
    zip_safe=False,
    keywords=[
        "NLP",
        "World Cloud",
        "Animation",
        "Natural Language Processing",
        "video",
        "Visualization",
        "Data Science",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia :: Video",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
    ],
    entry_points={
        # "console_scripts": [
        # ],
    },
    project_urls={
        "GitHub Repository": "https://github.com/konbraphat51/AnimatedWordCloud"
    },
)
