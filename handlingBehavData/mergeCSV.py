# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:33:41 2017
This script takes all csv files that are located in a folder at the path 
specified by basedir, and mnerges them into a single output file - also it adds 
a column with the participant number - How to improve: make it write the header

@author: ll1327
"""

from glob import glob
import os

# path for the csv files in all the participants folders
basedir = '/scratch/groups/Projects/P1334/1stLevel/[0-9][0-9]_R[0-9][0-9][0-9][0-9]/Behav/*.csv'


ppt_dirs = glob(basedir)

# output directory
out = '/scratch/groups/Projects/P1334/1stLevel/BehavResults/allData.csv'

with open(out, 'w') as singleFile:
    for csvFile in ppt_dirs:
        num = os.path.basename(csvFile).split('_')[0]   # takes the last bit of 
                                                        # the path which contains 
                                                        # ppt num and time etc), 
                                                        # then select only number
        for i, line in enumerate(open(csvFile, 'r')):
            if i == 0: # removes the first row (first row has index zero)
                pass
            else:
                singleFile.write(num + ',' + line)  # produces the new logfile 
                                                    # and adds a line for ppt n
