# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:06:10 2014

@author: David Beery
"""
__version__ = '1.1'

from features import Feature, marathonData

def main():
    #List of english words:
    #http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt
    info = marathonData(".\\full.csv")
    test = Feature(info)
    test.outlier('value')

if __name__ == '__main__':
    main()