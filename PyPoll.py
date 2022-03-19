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
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # for row in file_reader:
    #     print(row)
     # Print the header row.
    headers = next(file_reader)
    print(headers)



# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# Write some data to the file.
# outfile.write("Hello World")
    # txt_file.write("Hello World")
    
    # txt_file.write("Arapahoe")
    # txt_file.write("Denver")
    # txt_file.write("Jefferson")
    
    # txt_file.write("Arapahoe, Denver, Jefferson")
    
    #  txt_file.write("Arapahoe\nDenver\nJefferson")
# Close the file
# outfile.close()