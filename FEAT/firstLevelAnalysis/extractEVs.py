#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:33:52 2017

This script takes the csv files in the behavioural folder for each participant 
in the main directory, and reads through, and produces output text files
containing the information we need for the EVs in FEAT - produces CONSTANT EPOCH

First column is the start of the decision (when the words appear), second column 
is the duration of the decision (4 sec), third column is a weight. I gave the weight 1 to everything, regardless of accuracy 

IMPORTANT: 
1.the script must live in the same directory as the paryicipants folders 
(if not, glob.glob will not find anything with that structure specified in "par")
2. Uncomment the lines about the cue model if wanting to run on cue model
3. The script works only on a macrostructure of this kind: 
   1. main directory contains a folder for each participant
   2. each participant's folder has the following name [0-9][0-9]_R[0-9][0-9][0-9][0-9] (e.g. 20_R2437)
   3. update "par" and "behpath" if used outside of P1334

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
        
        
        trials = []                             # creates an empty list that will be filled with rows from the csv file
        with open(filename) as csvfile:         # open a csv file that has the name that we inputted
            reader = csv.DictReader(csvfile)    # reads through - temporary repository of the content of the csv
            #print(reader.fieldnames)           # for sanity check that the reader is doing its job        
            
            for row in reader:
                #print(row)
                trials.append(row)              # each item in "reader" will be added to the list "trials"

            
        # opens the following text files (for writing) they will be used to store the event timing
        fout1 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_combined_task.txt' %(par[i], modelType, version, run),'w')
        fout2 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_scrambled_task.txt' %(par[i],modelType, version, run),'w')        
        fout3 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleE_task.txt' %(par[i], modelType, version,run),'w')
        fout4 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleL_task.txt' %(par[i], modelType, version,run),'w')
        fout5 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_nonSem_task.txt' %(par[i],modelType, version, run),'w')

#        fout6 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_combined_cue.txt' %(par[i], modelType, version, run),'w')
#        fout7 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_scrambled_cue.txt' %(par[i],modelType, version, run),'w')        
#        fout8 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleE_cue.txt' %(par[i], modelType, version,run),'w')
#        fout9 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_singleL_cue.txt' %(par[i], modelType, version,run),'w')
#        fout10 = open('/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s/Run%s_nonSem_cue.txt' %(par[i],modelType, version, run),'w')        

        
        # now loops through the list of dictionaries 'trials' and stores the relevant info in the txt files
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
