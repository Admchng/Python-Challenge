# Import dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Output", "pypoll_data.txt")

# Declares the variables
candidate_votes = {}
vote_percentage = {}
total_votes = 0
WinnerCount = 0
Winner = ""

# Open and read files
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    # Loop each row and count and votes
    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

# Calculate percentage of votes for each candidate
for candidate in candidate_votes:
    vote_percentage[candidate] = candidate_votes[candidate] / total_votes

# Calculate the winner based on most votes
for candidate in candidate_votes:
    if candidate_votes[candidate] > WinnerCount:
        WinnerCount = candidate_votes[candidate]
        Winner = candidate

# Create a text file with the output
with open(file_to_output, "w") as textfile:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    textfile.write(election_results)

    # Print each candidate's voter count and percentage in the terminal.
    for candidate in candidate_votes:
        candidate_results = (
            f"{candidate}: {vote_percentage[candidate]*100:.1f}% ({candidate_votes[candidate]:,})\n")
        print(candidate_results)
        textfile.write(candidate_results)

    # Print the winner in the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {Winner}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    textfile.write(winning_candidate_summary)

# Read the output file
with open(file_to_output, "r") as analysis:
    contents = analysis.read()
print(contents)
