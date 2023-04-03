import csv 
import os

csvpath = "Resources/election_data.csv"

# To open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first and skip it
    csvheader = next(csvfile)

    # Defined variables
    totalVotes = 0
    candidateList = {}
    candidate = ""
    candidateNum = []
    candidateVotes = 0

    for row in csvreader:

        # The total number of votes
        totalVotes = totalVotes + 1

        # The total number of votes each candidate won and candidates
        candidateList[str(row[2])] = 1 + candidateList.get(str(row[2]), 0)

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalVotes))

    print("-------------------------")
    # The percentage of votes each candidate won
    for candidate in candidateList.keys():
        print(candidate + ": " + str(round(100 * (candidateList[candidate]/totalVotes), 3)) + "%" + " (" + (str(candidateList[candidate])) + ")")
    print("-------------------------")
    # The winner of the election based on popular vote
    currentMax = float("-inf")
    winner = ""
    for candidate in candidateList:
        if candidateList[candidate] > currentMax:
            currentMax = candidateList[candidate]
            winner = candidate
    print("Winner: " + str(winner))
    print("-------------------------")


# Export as a txt file with information
with open("output.txt", "a") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print("Total Votes: " + str(totalVotes), file=f)

    print("-------------------------", file=f)
    # The percentage of votes each candidate won
    for candidate in candidateList.keys():
        print(candidate + ": " + str(round(100 * (candidateList[candidate]/totalVotes), 3)) + "%" + " (" + (str(candidateList[candidate])) + ")", file=f)
    print("-------------------------", file=f)
    # The winner of the election based on popular vote
    currentMax = float("-inf")
    winner = ""
    for candidate in candidateList:
        if candidateList[candidate] > currentMax:
            currentMax = candidateList[candidate]
            winner = candidate
    print("Winner: " + str(winner), file=f)
    print("-------------------------", file=f)