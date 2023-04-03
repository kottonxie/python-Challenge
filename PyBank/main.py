import csv 
import os

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

csvpath = "Resources/budget_data.csv"

# To open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first and skip it
    csvheader = next(csvfile)
    # print(f"Header: {csvheader}")


    month = 0
    netTotal = 0
    pl = 0
    changePL = []
    greatestInc = float("-inf")
    greatestDec = float("inf")
    increase = ""
    decrease = ""

    for row in csvreader:

        # The total number of months included in the dataset
        month = month + 1
        # print(row[0])
        
        # The net total amount of "Profit/Losses" over the entire period
        netTotal = netTotal + int(row[1])

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        
        # To skip the first row
        if pl == 0:
            pl = int(row[1])
            continue

        # Adds list 
        changePL.append(int(row[1]) - pl)

        if (int(row[1]) - pl) > greatestInc:
            greatestInc = (int(row[1]) - pl)
            increase = row[0]

        if (int(row[1]) - pl) < greatestDec:
            greatestDec = (int(row[1]) - pl)
            decrease = row[0]

        # Saves the previous PL
        pl = int(row[1])

        # The greatest increase


    # Calulates the average of the difference in PL
    average = sum(changePL) / len(changePL)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month))
    print("Total: $" + str(netTotal))
    print("Average Change: $" + str(round(average, 2)))
    print(f"Greatest Increase in Profits: " + str(increase) + " ($" + str(greatestInc) + ")")
    print(f"Greatest Decrease in Profits: " + str(decrease) + " ($" + str(greatestDec) + ")")

    # Export as a txt file with information
    with open("output.txt", "a") as f:
        print("Financial Analysis", file=f)
        print("----------------------------", file=f)
        print("Total Months: " + str(month), file=f)
        print("Total: $" + str(netTotal), file=f)
        print("Average Change: $" + str(round(average, 2)), file=f)
        print(f"Greatest Increase in Profits: " + str(increase) + " ($" + str(greatestInc) + ")", file=f)
        print(f"Greatest Decrease in Profits: " + str(decrease) + " ($" + str(greatestDec) + ")", file=f)