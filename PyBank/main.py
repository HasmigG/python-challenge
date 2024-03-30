import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

months = 0
total_profit_loss = 0
previous_profit_loss = False
total_change = 0

changes_list = []
inc = ["",0]
dec = ["",0]

with open(budget_data) as data:
    reader = csv.reader(data)

    # Read the header row
    # header = next(reader)
    next(reader)
   
    for row in reader:
        months = months + 1
        
        # Total
        profit_loss = int(row[1])
        total_profit_loss += profit_loss

        if previous_profit_loss: #if it's anything that isn't false
                
            # # Average change from EXPERT
            change = profit_loss - previous_profit_loss
            changes_list.append(change)
            
             # Greatest Increase
            if change > inc[1]:
                inc[0] = row[0]
                inc[1] = change

            # Greatest Decrease
            if change < dec[1]:
                dec[0] = row[0]
                dec[1] = change

        previous_profit_loss = profit_loss

    

                # # Average change from TUTOR    
                # change =  profit_loss - previous_profit_loss
                # if previous_profit_loss == 0:
                #     change = 0

                # total_change += change

                # previous_profit_loss = profit_loss
    

    average_change = sum(changes_list) / len(changes_list)
    print(f"Testing: {sum(changes_list)}")


# Print out the state's name and their graduation rates
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: 86 {months}")
print(f"Total: $22564198 ${total_profit_loss}")
# print(f"Average Change: $-8311.11 ${average_change}")
print(f"Average Change: $-8311.11 ${average_change()}")
print(f"Greatest Increase in Profits: Aug-16 ($1862002) {inc[0]} (${inc[1]})")
print(f"Greatest Decrease in Profits: Feb-14 ($-1825558) {dec[0]} (${dec[1]})")

 
#  with open('Analysis', "financial_analysis.txt", 'w'):

#     # Write the rows
        # csvwriter.writerow(f"Financial Analysis")
        # csvwriter.writerow(f"----------------------------")
        # csvwriter.writerowf"Total Months: 86 {months}")
        # csvwriter.writerow(f"Total: $22564198 ${total_profit_loss}")

        # csvwriter.writerow(f"Average Change: $-8311.11 ${average_change}")

        # csvwriter.writerow(f"Greatest Increase in Profits: Aug-16 ($1862002) {inc[0]} (${inc[1]})")
        # csvwriter.writerow(f"Greatest Decrease in Profits: Feb-14 ($-1825558) {dec[0]} (${dec[1]})")


