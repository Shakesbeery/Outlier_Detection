# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:09:21 2014

@author: David Beery
"""
import numpy as np
import pandas as pd

class Feature:
    def __init__(self, info_list):
        self.data = info_list
        self.avg = 0.0
        self.std_dev = 0.0
        self.three_sigma = 0.0
        self.bounds = {'top': 0, 'bottom': 0}
        self.length = [len(str(x)) for x in info_list]
        try:
            self.value = [int(x) for x in info_list]
        except ValueError:
            pass
        
    def sd(self, data_type):
        values = getattr(self, data_type)
        self.std_dev = np.std(values)
        self.three_sigma = self.std_dev*3
    
    def mean(self, data_type):
        values = getattr(self, data_type)
        self.avg = np.mean(values)
        
    def outlier(self, data_type):
        self.mean(data_type)
        self.sd(data_type)
        self.bounds['bottom'] = self.avg - self.three_sigma
        self.bounds['top'] = self.avg + self.three_sigma
        for i, item in enumerate(self.value):
            if item > self.bounds['top']:
                print self.data[i], "has a {0} greater than the upper limit of {1}...".format(data_type, self.bounds['top'])
            elif item < self.bounds['bottom']:
                print self.data[i], "has a {0} lower than the lower limit of {1}...".format(data_type, self.bounds['bottom'])
        print "No other outliers detected in data set!"

def marathonData(loc):
    df = pd.read_csv(loc)
    return list(df["Time in Seconds"])
    