import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')
my_report = open("Analysis/Election_Analysis.txt", "w")

total = 0
candidate_list = {}
win_votes = 0

for row in election_data:
    total += 1

    canditate = row["Candidate"]
    if canditate not in candidate_list.keys():
        candidate_list[candidate] = 0
    candidate_list[candidate] += 1


output = f'''
Election Results
-------------------------
Total Votes: {total}
-------------------------
'''

for candidate in candidate_list.keys():
    votes = can_list[can]

    output += f'{candidate}: {votes/total *100:.3f}% ({votes:,})\n'

    if votes > win_votes:
        win_votes = votes
        winner = candidate

output += f'------------------------- \nWinner: {winner}\n-------------------------'

print(output)
my_report.write(output)

#
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
    

#  with open('Analysis', "election_result.txt", 'w'):

#     # Write the rows
        # csvwriter.writerow(f"Financial Analysis")
        # csvwriter.writerow(f"----------------------------")
        # csvwriter.writerowf"Total Months: 86 {months}")
        # csvwriter.writerow(f"Total: $22564198 ${total_profit_loss}")

        # csvwriter.writerow(f"Average Change: $-8311.11 ${average_change}")

        # csvwriter.writerow(f"Greatest Increase in Profits: Aug-16 ($1862002) {inc[0]} (${inc[1]})")
        # csvwriter.writerow(f"Greatest Decrease in Profits: Feb-14 ($-1825558) {dec[0]} (${dec[1]})")

