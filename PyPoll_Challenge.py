
from ast import If
import csv
import os

file_to_load = os.path.join( "Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

county_options = []

county_votes= {}



winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_county_count = 0


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        total_votes = total_votes + 1

        candidate_name = row[2]

        county_name = row[1]

     
        
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        if county_name not in county_options:

            county_options.append(county_name)

            county_votes[county_name] = 0

      
            county_votes[county_name] += 1

        else:
            county_votes[county_name] += 1


with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for county in county_votes.keys():
      
        vote_county = county_votes.get(county)

       
        vote_percentage_county = float(vote_county) / float(total_votes) * 100

       
        county_results = (
            f"{county}: {vote_percentage_county:.1f}% ({vote_county:,})\n"
        )
    
        print(county_results)

        txt_file.write(county_results)
        
       
        
        if vote_county > winning_county_count:
            winning_county = county
            winning_county_count = vote_county
        
   
    winning_county_summary = (
                f"-------------------------\n"
                    f"Largest County Turnout Winner: {winning_county}\n" 
                    f"-------------------------\n")
    
    print(winning_county_summary)


  
    txt_file.write(winning_county_summary)

  
    for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

     
        print(candidate_results)
       
        txt_file.write(candidate_results)

      
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

   
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
