import os
import csv

csvpath = os.path.join('Resources/budget_data.csv')
with open(csvpath, newline='') as csvfile:
    pybank = csv.reader(csvfile, delimiter=",")  
    csv_header = next(pybank)
    
    total_Months = 0
    dates = []
    pNL = []
        
    for row in pybank:
        total_Months += 1
        dates.append(row[0])
        pNL.append(float(row[1]))

total_Profits = pNL[0]
avg_Change = 0
great_Inc = 0
great_Dec = 0

for i in range(1, total_Months):
    total_Profits += pNL[i]
    
    change = pNL[i] - pNL[i-1]
    avg_Change += change

    if change > great_Inc:
        great_Inc = change
        great_IncMonth = dates[i]
    elif change < great_Inc:
        great_Dec = change
        great_DecMonth = dates[i]

print("Financial Analysis")
print("----------------------------")
print(f"Months: {total_Months}")
print(f"Total Profits: ${(total_Profits):.2f}")
print(f"Average Change: ${(avg_Change/(total_Months - 1)):.2f}")
print(f"Greatest Increase in Profits: {great_IncMonth} (${great_Inc})")
print(f"Greatest Decrease in Profits: {great_DecMonth} (${great_Dec})")

with open("PyBank_Output.txt","w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Months: {total_Months}\n")
    txtfile.write(f"Total Profits: ${(total_Profits):.2f}\n")
    txtfile.write(f"Average Change: ${(avg_Change/(total_Months - 1)):.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {great_IncMonth} (${(great_Inc):.2f})\n")
    txtfile.write(f"Greatest Decrease in Profits: {great_DecMonth} (${(great_Dec):.2f})\n")


    




    


    

    