#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import csv

csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader,None)
    
    row_count = 0
    
    cand={}
    
    for row in csvreader:
         row_count += 1
         if row[2] not in cand:
            cand[row[2]] = 0
         cand[row[2]] = cand[row[2]] + 1

    print(f"Election Results",
          f"\n----------------------------",
          f"\nTotal Votes: {row_count}",
          f"\n----------------------------")
    for row in cand:
           print(f"{row}: {format((cand[row]/row_count*100),'.3f')}% ({cand[row]})")
    print(f"----------------------------",
            f"\nWinner: {max(cand, key=cand.get)}",
            f"\n----------------------------")
    
    txtpath = os.path.join('..','PyPoll', 'analysis', 'Text Output.txt')
    file1 = open(txtpath,"w") 
    file1.writelines(f"Election Results\n----------------------------\nTotal Votes: {row_count}\n----------------------------")
    for row in cand:
        file1.write(f"\n{row}: {format((cand[row]/row_count*100),'.3f')}% ({cand[row]})")
    file1.writelines(f"\n----------------------------\nWinner: {max(cand, key=cand.get)}\n----------------------------")    
    file1.close()


# In[ ]:




