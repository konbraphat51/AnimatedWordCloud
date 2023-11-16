# -*- coding: utf-8 -*-
# Copyright (C) 2016-2023 PyThaiNLP Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Setup script for PyThaiNLP.

https://github.com/PyThaiNLP/pythainlp
"""
from setuptools import find_packages, setup

readme = """
(readme here)
"""

requirements = []

setup(
    name="AnimatedWordCloud",
    version="0.1.0",
    description="Animate a word cloud",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="konbraphat51, superhotdogcat",
    author_email="",
    url="https://github.com/konbraphat51/AnimatedWordCloud/tree/main",
    packages=find_packages(exclude=["tests", "tests.*"]),
    test_suite="tests",
    python_requires=">=3.7",
    package_data={
        "AnimatedWordCloud/Assets": [
            "Fonts/NotoSansMono-VariableFont_wdth,wght.ttf"
        ]
    },
    include_package_data=True,
    install_requires=requirements,
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
    project_urls={},
)

# TODO: Check extras and decide whether or not additional data, like model files, should be downloaded
