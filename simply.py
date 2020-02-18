# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:11:33 2020

@author: polakiew
"""

def simplyfy(x, threshholds = [24,60,60]):
    result = []
    for thresh in threshholds[::-1]:
        result.append(x % thresh)
        x //= thresh
    result.append(x)
    return result[::-1]
