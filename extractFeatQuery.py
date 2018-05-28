#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:34:20 2018
@author: ll1327

Want a script that takes the content of the text files outputted after feat query and copies them in csv file

"""

import glob
#------------------------------------------------------------------------------
cope = input ("Which cope?")
cluster = input ("Which cluster?")

#------------------------------------------------------------------------------

studydir = "/scratch/groups/Projects/P1334/fMRI_analyses/2.intermediate"
outdir = "/scratch/groups/Projects/P1334/fMRI_analyses/4.ROI/task/2.2/Results"


subdirsFunc = glob.glob("%s/[0-9][0-9]_R[0-9][0-9][0-9][0-9]"%(studydir)) 

with open("%s/featQ_cope%s_clust%s.txt" %(outdir, cope, cluster), 'w') as outfile: 
    # for each filepath found 
    for dir in list(subdirsFunc):
        splitdir = dir.split('/')         # split by /. This will give you:
                                    # '', 'scratch', 'groups, 'Projects', 'P1334', '1stLevel', '26_R3529' (for example)
    
        splitdir_sub = splitdir[7]        # subject number is in index 7 (start counting from 0, '' is 0)
        subnum = splitdir_sub             # if not sure you can test that in the console using splitdir[6]
       
                                    
        print(subnum)
  

  
        with open("%s/%s/Results/task/2.2/intermediate.gfeat/cope%s.feat/featquery_clust%s/report.txt"%(studydir, subnum,cope, cluster)) as infile:
            for line in infile:
                 outfile.write(line)
                 print(line)
    
          
          

   
    
    
    

    
  