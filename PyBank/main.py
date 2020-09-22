#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import csv

csvpath = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader,None)
       
    total = 0
    row_count = 0
    maxx = 0
    minn = 0
    for row in csvreader:
        total += int(row[1])
        row_count += 1
        if float(row[1]) > float(maxx):
            maxx = row[1]
            max_date = row[0]
        if float(row[1]) < float(minn):
            minn = row[1]
            min_date = row[0]
    
    print(f"Financial Analysis",
          f"\n----------------------------",
          f"\nTotal Months: {row_count}",
          f"\nTotal: ${total}",
          f"\nAverage  Change: ${round(total/row_count,2)}",
          f"\nGreatest Increase in Profits: {max_date} (${maxx})",
          f"\nGreatest Decrease in Profits: {min_date} (${minn})")
    
    txtpath = os.path.join('..','PyBank', 'analysis', 'Text Output.txt')
    file1 = open(txtpath,"w") 
    file1.writelines(f"Financial Analysis\n----------------------------\nTotal Months: {row_count}\nTotal: ${total}\nAverage  Change: ${round(total/row_count,2)}\nGreatest Increase in Profits: {max_date} (${maxx})\nGreatest Decrease in Profits: {min_date} (${minn})") 
    file1.close()

