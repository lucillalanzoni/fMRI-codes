# ll1327 (readapted from J Mumford)- 13/10/17

'''
IMPORTANT! CHECK LINE 27 and 32 AND MAKE SURE IT MATCHED THE DIRECTORY WHERE THE TEMPLATE IS CONTAINED
-----------------------------
This script was readapted from Janette Mumford youtube video
https://www.youtube.com/watch?v=Js0tlNXxd9k

There is a template file called design_template_taskEVs.fsf in fsfdir
What the script does is to open the template file, replace all the wildcards with
the values for that participant, and generate each subjects design.fsf. 

The script will NOT run the analyses if line 76 is commented
If unsure about the fsf file and want to test it, don't run all of them in batch.
Safer to run one first and see what happens. There is a screenshot with a bash command 
to run the script in the cluster. /home/l/ll1327/Pictures/learnHOW

'''

# This script will generate each subjects design.fsf, but does not run it.
# Run it in the cluster

import glob
import os

# Set this to the directory in which all of the sub- directories live
studydir = '/scratch/groups/Projects/P1334/fMRI_analyses/1.firstLevel'


# Set this to the directory where you'll dump all the fsf files
# This is also the directory in which the template file lives
fsfdir = "%s/fsf/task/2.2" %(studydir)


# Get all the paths
# glob.glob allows you to retrieve files without having to specifying their name
# glob.glob works even when different subjs. don't have the same number of files in their folders

subdirsFunc = glob.glob("%s/[0-9][0-9]_R[0-9][0-9][0-9][0-9]/Functional/Run[0-9].nii.gz"%(studydir))
#subdirsFunc = ['1_R4065', '2_R3899']          # use this if wanting to generate fsf file for a few people only


# for each filepath found 
for dir in list(subdirsFunc):
  splitdir = dir.split('/')         # split by /. This will give you:
                                    # '', 'scratch', 'groups, 'Projects', etc.
    
  splitdir_sub = splitdir[7]        # subject number is in index 6 (start counting from 0, '' is 0)
  subnum = splitdir_sub             # if not sure you can test that in the console using splitdir[7]
       
                                    
  splitdir_run = splitdir[9]        # subject number is in index 9 (count from 0)
  runnum=splitdir_run[:4]           # we retain only Run1 (discard the file extension, which is the last 4 characters)
  print(subnum)
  

  # creates a dictionary that specifies what to replace the wildcards with
  replacements = {'SUBNUM':subnum, 'RUNNUM':runnum}
  
  
  # now open the template file for reading
  with open("%s/design_template_taskEVs.fsf"%(fsfdir)) as infile:
      
    # and open an output file for writing
    with open("%s/design_%s_%s.fsf"%(fsfdir, subnum, runnum), 'w') as outfile:
        
        # loop through the rows of the template file
        for line in infile:
            
          # take the key (src = source) and value (target) in the dictionary "replacements"
          for src, target in replacements.items():
              
            # for each row replace src (wildcards) with the desired value 
            line = line.replace(src, target)
            
          outfile.write(line)
                   
# CAREFUL HERE! If this line is uncommented, the script will automatically send
# all the fsf files to the clusterFeat. Make sure you have tested one fsf file
# before sending them in batch
         
  os.system("clusterFeat %s/design_%s_%s.fsf"%(fsfdir, subnum, runnum))
