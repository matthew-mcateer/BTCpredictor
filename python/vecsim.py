# -*- coding: utf-8 -*-
'''
find the similarity between two vectors "x" and "y"
'''
import math
import numpy as np

def vecsim(x, y):
    
    assert len(x) == len(y), "these vectors are different lengths!"
    assert x.size =! 0, "need a larger vector"
    
    num = np.sum((x - np.mean(x)).*(y - np.mean(y)))
    den = len(x) * np.std(x) * np.std(y)
    
    if (den == 0):
       similarity = num     #to account for if either vector has std = 0
       else:
       s = (num / den)
    
    return similarity