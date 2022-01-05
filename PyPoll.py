#Add dependencies
import csv

#Assign a variable to load a file from a path 
file_to_load = 'resources/election_results.csv'
#Assign a variable to save a file from a path 
file_to_save = 'analysis/election_analysis.txt'

#initalize total votes variable 
total_votes = 0

#declare new list for candiates
candidate_options = []

#declare dictionary for candidate votes 
candidate_votes = {}

#winning variables tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file 
with open(file_to_load) as election_data:
    
    #To do: read and analyze data here
    #read the file object with the reader function 
    file_reader = csv.reader(election_data)

    #read the header row 
    headers = next(file_reader)

    #Print each row in the CSV file 
    for row in file_reader:
        #add to total vote count 
        total_votes += 1
        #print candidate name from each row 
        candidate_name = row[2]
        #If candidate does not match any existing candidate 
        if candidate_name not in candidate_options:
            #add it to list of candidates
            candidate_options.append(candidate_name)
            #begin tracking candidate votes counts 
            candidate_votes[candidate_name] = 0
        #increment candidate votes 
        candidate_votes[candidate_name] += 1

#Save final results to text file 
with open(file_to_save, "w") as txt_file:
    #Print final vote count to terminal 
    election_results = (
        f'\n'
        f'Election Results\n'
        f'-----------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-----------------------\n')
    print(election_results, end="")
    #Save final vote count to text file 
    txt_file.write(election_results)
    #Iterate through candidate list 
    for candidate_name in candidate_votes: 
        #retrieve vote count of candidate 
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes 
        vote_percentage = float(votes) / float(total_votes) * 100 
        #to do: print out each candidates's name, vote count, and percentage of votes to the terminal and txt file
        candidate_results = (f'{candidate_name}: {votes}, {vote_percentage:.1f}%\n')
        print(candidate_results)
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate 
        #Determine if the votes is greater than the winning count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true set the following...
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    #To do: print out winning candidate, vote count, and percentage to terminal and text file
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
         

 
