# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:09:21 2014

@author: David Beery
"""
import numpy as np

class feature:
    def __init__(self, info_list):
        self.data = info_list
        self.length = [len(str(x)) for x in info_list]
        try:
            self.values = [float(x) for x in info_list]
        except ValueError:
            pass
        
    def SD(self, data_type):
        values = getattr(self, data_type)
        return np.std(values)
    
    def mean(self, data_type):
        values = getattr(self, data_type)
        return np.mean(values)
        
    def outlier(self):
        pass
            