#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:33:52 2017
DESCRIPTION HERE
This script takes the csv files in the behav folder for each participant 
specified in brackets, and reads through, and produces output text files
containing the information we need for FEAT

IMPORTANT: 
    1.Make sure the script lives in the same directory as the participants folders
    2.Make sure the directory is the correct one

Improve: add a few lines that create the directory for a new version if this doesn't exist

@author: ll1327
"""

import csv
import os
import glob

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
modelType = input ('Is this cue or task?')
version = input ('What version are you running?')

# List of participants on which we want to perform the analyses

par = glob.glob('[0-9][0-9]_R[0-9][0-9][0-9][0-9]')       # grabs all participants in the folder 
par.sort()

for i in range(len(par)):
    directory = '/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel/%s/Evs/%s/%s' %(par[i], modelType, version) 

    if not os.path.exists(directory):
        os.makedirs(directory)
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

        
        # now loops through the list of dictionaries 'trials' and stores the info in txt files
        for entry in trials:
            
            if entry['Cue Condition'] == 'combined' and entry['CORR'] == '1':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout1)
                #fout1.write('%s 4 1\n' %entry['Task_start'])
            elif entry['Cue Condition'] == 'combined' and entry['CORR'] == '0':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','0'), file = fout1)
            
            if entry['Cue Condition'] == 'scrambled'and entry['CORR'] == '1': 
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout2)
            elif entry['Cue Condition'] == 'scrambled'and entry['CORR'] == '0':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','0'), file = fout2)
                
            if entry['Cue Condition'] == 'singleE' and entry['CORR'] == '1': 
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout3)
            elif entry['Cue Condition'] == 'singleE' and entry['CORR'] == '0':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','0'), file = fout3)

            if entry['Cue Condition'] == 'singleL'and entry['CORR'] == '1':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout4)
            elif entry['Cue Condition'] == 'singleL'and entry['CORR'] == '0':
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','0'), file = fout4)
                
            if entry['Cue Condition'] == 'nonSem': 
                output = print('{0} {1} {2}'.format(entry['Task_start'],'4','1'), file = fout5)
        

        fout1.close()
        fout2.close()
        fout3.close()
        fout4.close()
        fout5.close()


        csvfile.close()