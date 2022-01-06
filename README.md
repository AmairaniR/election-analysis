# Election Analysis

## Overview of the Election Audit 
This project audit the election results of a US Congressional District in Colorado by using various methods in Python (version 3.9.7) to extract the data from a the election results csv file and analyze it to determine the following: the total votes cast in the election, the names of each candidate, how many votes each candidate received and the percentage of the votes each candidate recieved, this data was used to determine the winner of the election. A secondary analysis was issued on the data in regards to the counties. The name of each county was determined, as well as how many voters voted in each county and the percentage, this was done in order to see which county had the largets voter turnout. 

## Election Audit Results 
-Total Votes: 369,711
-County Votes 
    -Jefferson: 10.5% 38,855
    -Denver: 82.8% 306,055
    -Arapahoe: 6.7% 24,801
-County with largest voter turnout: Denver
-Candidate votes 
    -Charles Casper Stockham: 23.0% (85,213)
    -Diana DeGette: 73.8% (272,892)
    -Raymon Anthony Doane: 3.1% (11,606)
-Winning Results
    -Winner: Diana DeGette
    -Winning Vote Count: 272,892
    -Winning Percentage: 73.8%

## Election Audit Summary/Proposal
Most of the script is already easily adaptable to any basic csv file with election results. Some modifications that would need to be made would be when extracting the candidate name (candidate_name = row[2]) and the county name (county_name = row[1]) from each row since the current method relies on referencing the index of a specific list and those names may not always be in the same place in each file.

Another possible modification to make this script more user friendly would be to have an input statement in the beginning of the script where the user would put in the csv file that needs to be read instead of manually coding it in themselves. 

