#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:33:52 2017

This script takes the csv files in the behavioural folder for each participant 
in the main directory, and reads through, and produces output text files
containing the information we need for the EVs in FEAT

IMPORTANT: the script must live in the same directory as the paryicipants folders 
(if not, glob.glob will not find anything with that structure specified in line 31)

To improve: add a few lines that create the directory for a new version if this doesn't exist

@author: ll1327
"""

import csv
import os
import glob

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# In my experiment I had two main models: one for when participants saw the cue pictures, one for the following semantic decision task
modelType = input ('Is this cue or task?')

# My fMRI analyses have been numbered 1.0, 1.1, 1.2, 2.0, 2.1 (etc). This allows to grab exactly the folder that I need
version = input ('What version are you running?')
#-------------------------------------------------

# glob grabs all participants in the folder 
par = glob.glob('[0-9][0-9]_R[0-9][0-9][0-9][0-9]')       
 
# for each item in the list of participant, list the path to the folder that contains the behavioural data
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
        fout1 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_combined_task.txt' %(par[i], modelType, version, run),'w')
        fout2 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_scrambled_task.txt' %(par[i],modelType, version, run),'w')        
        fout3 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleE_task.txt' %(par[i], modelType, version,run),'w')
        fout4 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleL_task.txt' %(par[i], modelType, version,run),'w')
        fout5 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_nonSem_task.txt' %(par[i],modelType, version, run),'w')

#        fout6 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_combined_task.txt' %(par[i], modelType, version, run),'w')
#        fout7 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_scrambled_task.txt' %(par[i],modelType, version, run),'w')        
#        fout8 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleE_task.txt' %(par[i], modelType, version,run),'w')
#        fout9 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleL_task.txt' %(par[i], modelType, version,run),'w')
#        fout10 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_nonSem_task.txt' %(par[i],modelType, version, run),'w')        

        
        # now loops through the list of dictionaries 'trials' and stores the info in txt files
        for entry in trials:
            
            if entry['Cue Condition'] == 'combined':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout1)
#                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout6)
            
            if entry['Cue Condition'] == 'scrambled': 
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout2)
#                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout7)
                
            if entry['Cue Condition'] == 'singleE': 
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout3)
#                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout8)

            if entry['Cue Condition'] == 'singleL':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout4)
#                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout9)
                
            if entry['Cue Condition'] == 'nonSem': 
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout5)
#                output = print('{0} {1} {2}'.format(entry['Cue_start'],'1','1'), file = fout10)  
        

        fout1.close()
        fout2.close()
        fout3.close()
        fout4.close()
        fout5.close()
        
#        fout6.close()
#        fout7.close()
#        fout8.close()
#        fout9.close()
#        fout10.close()

        csvfile.close()
