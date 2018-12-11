import os
import csv

print("Financial Analysis")
print("------------------------")

bankCSV = os.path.join('Pybank_data.csv')

Months = []
Total_revenue = []
Monthly_Rev = []

with open(bankCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
     #The total number of months included in the dataset
        month = row[0]
        
        Months.append(month)

        TotalMonths = len(Months)

    #The total net amount of "Profit/Losses" over the entire period

        Revenue = int(row[1])
        
        Total_revenue.append(Revenue)

    for i in range(Total_revenue):

       Monthly_Rev.append(Total_revenue[i+1]-Total_revenue[i])


       Monthly_change = (sum(Monthly_Rev)/len(Monthly_Rev))

min == i <

print(f"Total Months:  {str(TotalMonths)}")
print(f"Total : ${sum(Total_revenue)}")
#print(f"Total Monthly change:  ${round(sum(Monthly_Rev)/len(Monthly_Rev),2)}")








#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period