import csv

# open file in dictionary reader mode
data = csv.DictReader(open('Resources/election_data.csv'))

# open a new text file to receive the output
my_report = open("Analysis/Election_Analysis.txt", "w")

# set up variables
total = 0
candidate_list = {}
win_votes = 0

# for loop to get data from each row in the file
for row in data:
    # increment the total votes
    total += 1

    # candidate's name from current row
    candidate = row["Candidate"]  

    # get new candidate name with 0 votes
    if candidate not in candidate_list.keys():
        candidate_list[candidate] = 0
    candidate_list[candidate] += 1
   
# set up for the output
output = f'''

Election Results
-------------------------
Total Votes: {total:,}
-------------------------
'''

# for loop to get votes per candidate
for candidate in candidate_list.keys():
    votes = candidate_list[candidate]

    # calculate percentage of votes per candidate and store in variable for output
    output += f'{candidate}: {votes/total *100:.3f}% ({votes:,})\n'

    # check if subsequent candidate has more votes than the previous
    if votes > win_votes:
        win_votes = votes
        winner = candidate

# add winner to output variable
output += f'------------------------- \nWinner: {winner}\n-------------------------'

# print to console
print(output)
# output to text file
my_report.write(output)