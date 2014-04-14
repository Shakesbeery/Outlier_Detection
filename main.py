# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:06:10 2014

@author: David Beery
"""
__version__ = '1.0'

from features import feature, marathonData

def main():
    info = marathonData("D:\\Users\\David Beery\\Google Drive\\full.csv")
    test = feature(info)
    test.outlier('values')

if __name__ == '__main__':
    main()