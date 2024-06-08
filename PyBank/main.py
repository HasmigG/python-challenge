import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')
my_report = open('Analysis/Budget_Analysis.txt','w')

months = 0
total = 0
previous_revenue = 0
total_change = 0
increase = ["",0]
decrease = ["",0]

with open(budget_data, 'r') as file:
    csvreader = csv.reader(file)
    csv_header = next(csvreader)

    for row in csvreader:
        months += 1
            
        # Total
        profit_loss = int(row[1])
        total += profit_loss

        # Average Change
        change = profit_loss - previous_revenue
        if previous_revenue == 0:
            change = 0
        
        total_change += change

        previous_revenue = profit_loss

        # Greatest Increase
        if change > increase[1]:
            increase[0] = row[0]
            increase[1] = change

        # Greatest Decrease
        if change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = change

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_change/(months-1):,.2f}
Greatest Increase in Profits: {increase[0]} (${increase[1]:,})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]:,})
'''

print (output)
my_report.write(output)
my_report.close()