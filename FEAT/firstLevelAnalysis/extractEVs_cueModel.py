#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:33:52 2017
DESCRIPTION HERE
This script takes the csv files in the behav folder for each participant 
specified in brackets, and reads through, and produces output text files
containing the information we need for FEAT


@author: ll1327
"""

import csv
import os
import glob

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# List of participants on which we want to perform the analyses

par = glob.glob('[0-9][0-9]_R[0-9][0-9][0-9][0-9]')       # grabs all participants in the main directory

for i in range(len(par)):
    behpath = os.listdir('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Behav' %par[i])
    for k in range(len(behpath)):
        filename = '/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Behav/%s' %(par[i], behpath[k])
        run = filename.split('/')[-1].split('_')[2]
        
        # open a csv file that has the name that we inputted
        trials = []
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)    # reads through
            #print(reader.fieldnames)            
            for row in reader:
                #print(row)
                trials.append(row)
                
            
        # opens the following text files that will be used to store the even timing
#        fout1 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/task/Run%s_combined_task.txt' %(par[i], run),'w')
#        fout2 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/task/Run%s_scrambled_task.txt' %(par[i],run),'w')
#        fout3 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/task/Run%s_singleE_task.txt' %(par[i],run),'w')
#        fout4 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/task/Run%s_singleL_task.txt' %(par[i],run),'w')
#        fout5 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/task/Run%s_nonSem_task.txt' %(par[i],run),'w')
#        fout6 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/task/Run%s_null_task.txt' %(par[i],run),'w')
        fout7 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/cue/Run%s_combined_pics.txt' %(par[i], run),'w')
        fout8 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/cue/Run%s_scrambled_pics.txt' %(par[i],run),'w')
        fout9 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/cue/Run%s_singleE_pics.txt' %(par[i],run),'w')
        fout10 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/cue/Run%s_singleL_pics.txt' %(par[i],run),'w')
#        fout11 = open('/scratch/groups/Projects/P1334/1stLevel/%s/Evs/cue/Run%s_nonSem_pics.txt' %(par[i],run),'w')
        
        
        # now loops through the list of dictionaries 'trials' and stores the info in txt files
        for entry in trials:
            
            if entry['Cue Condition'] == 'combined':
#                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout1)
                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout7)
            
            if entry['Cue Condition'] == 'scrambled' or entry['Cue Condition'] == 'nonSem': 
#                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout2)
                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout8)
                
            if entry['Cue Condition'] == 'singleE': 
#                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout3)
                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout9)
                
            if entry['Cue Condition'] == 'singleL': 
#                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout4)
                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout10)
            
#            if entry['Cue Condition'] == 'nonSem': 
#                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout5)
#                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout11)  
        
#            if entry['Cue Condition'] == 'null': 
#                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout6)
        
#        fout1.close()
#        fout2.close()
#        fout3.close()
#        fout4.close()
#        fout5.close()
#        fout6.close()
        fout7.close()
        fout8.close()
        fout9.close()
        fout10.close()
#        fout11.close()
        csvfile.close()
