#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import csv

csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader,None) # skip the header
    
    row_count = 0 # set variable to 0
    
    cand={}            # create a dictionary to hold the candidate and no.
    
    for row in csvreader:
         row_count += 1                                   # count row number
         if row[2] not in cand:                          # Add candidate when row[2] is not found in dictionary
            cand[row[2]] = 0                               # and assign 0 to the new candidate added
         cand[row[2]] = cand[row[2]] + 1          # Add 1 to the counter for the corresponding candidate
    
    print(f"Election Results",
          f"\n----------------------------",
          f"\nTotal Votes: {row_count}",
          f"\n----------------------------")
    for row in cand:
           print(f"{row}: {format((cand[row]/row_count*100),'.3f')}% ({cand[row]})")
    print(f"----------------------------",
            f"\nWinner: {max(cand, key=cand.get)}",
            f"\n----------------------------")
    
    
    # Export result to text file
    txtpath = os.path.join('..','PyPoll', 'analysis', 'Text Output.txt')
    file1 = open(txtpath,"w") 
    file1.writelines(f"Election Results\n----------------------------\nTotal Votes: {row_count}\n----------------------------")
    for row in cand:
        file1.write(f"\n{row}: {format((cand[row]/row_count*100),'.3f')}% ({cand[row]})")
    file1.writelines(f"\n----------------------------\nWinner: {max(cand, key=cand.get)}\n----------------------------")    
    file1.close()

