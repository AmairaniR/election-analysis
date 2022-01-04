#Add dependencies
import csv

#Assign a variable to load a file from a path 
file_to_load = 'resources/election_results.csv'
#Assign a variable to save a file from a path 
file_to_save = 'analysis/election_analysis.txt'

#Open the election results and read the file 
with open(file_to_load) as election_data:
    
    #To do: read and analyze data here
    #read the file object with the reader function 
        file_reader = csv.reader(election_data)

    #read and print the header row 
        headers = next(file_reader)
        print(headers)    