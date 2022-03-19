import pandas as pd

import csv

import os
# -------------
# import datetime as dt

# now = dt.datetime.now()
# print("The time right now is ", now)

# ----------------

# csv_file = "Resources/election_results1.csv"

# df_elections = pd.read_csv(file_to_load)
# # print(df_elections.head())

# print(dir(csv))


# ---------------

# election_data = open(file_to_load, 'r')

# Open the election results and read the file

# Direct path to file --------

# file_to_load = "election_results.csv"

# with open(file_to_load) as election_data:
    # To do: perform analysis.
    #  print(election_data)

#  --------

# Indirect path to file  with os --------


# file_to_load = os.path.join( "election_results.csv")

file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# 1. Initialize a total vote counter.
total_votes = 0

candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
 
    headers = next(file_reader)
      # print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
        
        # Add the candidate name to the candidate list.
            # candidate_options.append(candidate_name)
            
        # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        

# Total number of votes  = 369711
    
        
# 3. Print the total votes. 
print(total_votes) 
# Total number of votes each candidate received
print(candidate_votes)







        
  



