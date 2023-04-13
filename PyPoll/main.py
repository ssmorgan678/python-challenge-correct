# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate".



# Modules
import os
import csv


# Set variables
candidate_column = 2
candidate_votes = {}
total_votes = 0


# Set path, open, and read in the CSV file
election_csv_path = os.path.join('Resources', 'election_data.csv')
with open(election_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)


# Loop through data for candidate info
    for row in csvreader:
        total_votes += 1
        current_name = row[candidate_column]
        if current_name in candidate_votes:
            candidate_votes[current_name] +=1
        else:
            candidate_votes[current_name] = 1



print("Election Results")
print("------------------------------")

# The total number of votes cast
print(f"Total Votes: {total_votes}")
print("------------------------------")


# The percentage of votes each candidate won
# The total number of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = votes/total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("------------------------------")


# The winner of the election based on popular vote.
print(f"Winner: {max(candidate_votes, key=candidate_votes.get)}")


# Export to text file
output_path = os.path.join("Analysis", "election_results.txt")

with open(output_path, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("------------------------------\n")

    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("------------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = votes/total_votes * 100
        (f"{candidate}: {percentage:.3f}% ({votes})")
        textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    textfile.write("------------------------------\n")
    
    textfile.write(f"Winner: {max(candidate_votes, key=candidate_votes.get)}\n")
    textfile.write("------------------------------\n")

