
# coding: utf-8

# In[ ]:


# Homework #3 PyPoll

#You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
#Each dataset is composed of three columns: Voter ID, County, and Candidate.
# Import the os module
# This will allow us to create file paths across operating systems

import os
import csv

#Load election_data_1
csvpath1 = os.path.join("election_data_1.csv")

# Lists to store data
voter_id = []
county = []
candidate = []
nrows = 0

with open(csvpath1, 'r') as csvfile1:
    
    csvreader1 = csv.reader(csvfile1, delimiter=',')

    next(csvreader1, None)
    
    for row in csvreader1:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        nrows = nrows + 1


# In[ ]:


#Load election_data_2

csvpath2 = os.path.join("election_data_2.csv")

with open(csvpath2, 'r') as csvfile2:
    
    csvreader2 = csv.reader(csvfile2, delimiter=',')

    next(csvreader2, None)
    
    for row in csvreader2:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        nrows = nrows + 1


# In[ ]:


#Identify candidates
candidate_name = list(set(candidate))
print(candidate_name)


# In[ ]:


#The total number of votes each candidate won.
total_dict = {x:candidate.count(x) for x in candidate}
total_list = list(total_dict.values())
print(total_list)


# In[ ]:


#Identify Winner
winner_count = max(total_list)
winner_index = total_list.index(winner_count)
winner_name = candidate_name[winner_index]
print(winner_name)


# In[ ]:


#The percentage of votes each candidate won.
percent_dict = {x:(candidate.count(x)/nrows) for x in candidate}
percent_list = list(percent_dict.values())
print(percent_list)


# In[ ]:


# Zip lists together
summary = zip(candidate_name, total_list, percent_list)
summary_list = list(summary)
print(summary_list)


# In[ ]:


#Putting it all together

print('Election Results')
print("---------------------")
print('Total votes:', nrows)
print("---------------------")

for item in summary_list:
    print(item)

print("---------------------")
print('Winner: ', winner_name)
print("---------------------")




# In[ ]:


# Set variable for output file
output_file = os.path.join("pypoll_final3.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    
    # Write the header row
    writer.writerow(["Candidate", "Count", "Percent"])
    
    # Write in zipped rows
    writer.writerows(summary_list)

