#In this Challenge, you are tasked with creating a Python script to analyze the financial 
# records of your company. You will be given a financial dataset called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses"

#Import required modules
import os
import csv


#Initial variables
profit_change = []
date = []
prev_profit = 0
profit_loss = 0

#Set path and read in csv file
budget_csv_path = os.path.join('Resources','budget_data.csv')
with open (budget_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #Loop through the data and append/address variables
    for row in csvreader:
        profit_loss += int(row[1])
        change = int(row[1]) - prev_profit
        prev_profit = int(row[-1])
        profit_change.append(change)
        date.append(row[0])
        
       
    #Create variable to find the average change in "Profit/Losses"  
    avg_change = sum(profit_change[1:]) / len(date[1:])  
   

    #Create variables to find the greatest increase and the greatest decrease in profits
    max_increase = max(profit_change)
    increase = profit_change.index(max_increase)
    maxi_month = date[increase]

    max_decrease = min(profit_change)
    decrease = profit_change.index(max_decrease)
    maxd_month = date[decrease]

    
    #Print financial analysis results
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {len(date)}")
    print(f"Total: ${profit_loss}")
    print(f"Average Change: ${avg_change: .2f}")
    print(f"Greatest Increase in Profits: {maxi_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {maxd_month} (${max_decrease})")

#Set output path and export results to text file
output_path = os.path.join("Analysis", "financial_analysis.txt")

with open(output_path, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------------------\n")
    textfile.write(f"Total Months: {len(date)}\n")
    textfile.write(f"Total: ${profit_loss}\n")
    textfile.write(f"Average Change: ${avg_change: .2f}\n")
    textfile.write(f"Greatest Increase in Profits: {maxi_month} (${max_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {maxd_month} (${max_decrease})\n")
    