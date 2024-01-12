import csv
data = csv.reader(open('Resources/budget_data.csv'))
my_report = open('Analysis/Budget_Analysis.txt','w')

next(data)

months = 0
total = 0
pre_rev = 0
total_ch = 0
inc = ['',0]
dec = ['',0]

for row in data:
    months += 1 # months = months + 1

    # Total
    rev = int(row[1])
    total += rev
    
    # Average Change
    ch = rev - pre_rev
    if pre_rev == 0:
        ch = 0
    
    total_ch += ch

    pre_rev = rev

    # Greatest Increase
    if ch > inc[1]:
        inc[0] = row[0]
        inc[1] = ch

    # Greatest Decrease
    if ch < dec[1]:
        dec[0] = row[0]
        dec[1] = ch



output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)