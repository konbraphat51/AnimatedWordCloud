# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate allocation of each words in each static time
"""

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from AnimatedWordCloud import WordVector, TimelapseWordVector
from AnimatedWordCloud.Animator import AllocationInFrame, AllocationTimelapse

def allocate(word_vector: WordVector, 
             max_words: int, 
             max_word_size: float,
             image_width: int,
             image_height: int,
             font_path: str) -> AllocationInFrame:
    """
    Calculate allocation of each words in each static time

    :param WordVector word_vector: The word vector
    :param int max_words: Maximum number of words shown
    :param float max_word_size: Maximum size of the word
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """
    
    words = word_vector.get_ranking(0, max_words)
    
def estimate_text_size(word: str, font_size: int, font_path: str) -> (int, int):
    """
    Estimate text box size

    Highly depends on the drawing library

    :param str word: The word
    :param int font_size: The font size
    :param str font_path: The font path
    :return: Text box size (x, y)
    :rtype: (int, int)
    """
    
    #empty image
    image = np.zeros((font_size*2, font_size*(len(word)+1), 3), dtype=np.uint8)
    font = ImageFont.truetype(font_path, font_size)
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    
    #get size
    w, h = draw.textsize(word, font=font)
    
    return (w, h)
    
    
def allocate_all(timelapse: TimelapseWordVector) -> AllocationTimelapse:
    """
    Calculate allocation of each words in several each static time

    :param TimelapseWordVector timelapse: The word vector    
    :return: Allocation data of each frame
    :rtype: AllocationTimelapse
    """
    
    times = len(timelapse)

    allocation_timelapse = AllocationTimelapse()
    
    for cnt in range(times):
        allocation = allocate(timelapse[cnt].word_vector)
        allocation_timelapse.add(timelapse[cnt].time_name, allocation)
        
    return allocation_timelapse