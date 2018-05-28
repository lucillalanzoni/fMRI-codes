#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:56:19 2018

@author: ll1327
"""

import os

# Set this to the directory in which all of the sub- directories live
studydir = '/scratch/groups/Projects/P1334/fMRI_analyses/3.group'


# Set this to the directory where you'll dump all the fsf files
# This is also the directory in which the template file lives
fsfdir = "%s/fsf/task/2.2.1" %(studydir)

for i in os.listdir(fsfdir):
  print(i)
  os.system("clusterFeat %s/%s"%(fsfdir,i))