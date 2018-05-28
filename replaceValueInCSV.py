#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:54:24 2018

This script needs to live in the directory where all the participants folders are

Opens the csv files in the specified directory, if the response is None
which means that no response has been given, replaces a 3 with a 4
Script wrote to fix the csv files from a mistake in the experiment script 
(which instead of storing a 4 for trials that have not been answered, it stores a 3)

@author: ll1327
"""
import pandas as pd
import glob
import os

par = glob.glob('[0-9][0-9]_R[0-9][0-9][0-9][0-9]')       # grabs all participants in the main directory

for i in range(len(par)):
    behpath = os.listdir('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Behav' %par[i])
    for k in range(len(behpath)):
        filename = '/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Behav/%s' %(par[i], behpath[k])
        
        df = pd.read_csv(filename)
        #df.head(3) #prints 3 heading rows


        #Now if you want to change the value in the 'RT' column in the 1st row, run:
        #df.set_value(1, "RT", 4)

        #If you want to change all the values where a certain condition is met
        df.loc[df["KeyPress"]== "None", "RT"] = 4

        #Finally, to save the values:
        df.to_csv(filename, index=False)
