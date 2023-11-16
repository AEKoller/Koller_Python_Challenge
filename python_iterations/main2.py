#So, I completed the pypoll part of the assignment the first time around uising a "stupid" method that didn't use dictionaries. Once we had gone over dictionaries in class, 
#I realized that I could use disctionaries, and I went back and redid the script to utilize dictionaries. I've included the my old script because I am happy that I managed  
#to do it my way first, but I also wanted to provide the "right" way to do it based off our previous exercises.
import os
import csv


election_data = os.path.join('pypoll', 'Resources','election_data.csv')

def election_analysis(election_data):
    total_votes = 0
    candidate_votes = {'Charles Casper Stockham': 0, 'Diana DeGette': 0, 'Raymon Anthony Doane': 0}
    #charles_votes = 0
    #charles_percent = None
    #diana_votes = 0 
    #diana_percent = None
    #raymon_votes = 0 
    #raymon_percent = None
    winner = None
    max_votes = 0

    with open(election_data, 'r') as csvfile:
        csvreader2 = csv.reader(csvfile, delimiter=',')

        next(csvreader2)

        for row in csvreader2:
            
            total_votes += 1
            candidate_name = str(row[2])
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            #if str(row[2]) == 'Charles Casper Stockham':
                #charles_votes += 1
            #if str(row[2]) == 'Diana DeGette':
                #diana_votes += 1
            #if str(row[2]) == 'Raymon Anthony Doane':
                #raymon_votes += 1
        #charles_percent = round(charles_votes/total_votes*100,3)
        #diana_percent = round(diana_votes/total_votes*100,3)
        #raymon_percent = round(raymon_votes/total_votes*100,3)

        #candidates.append(charles_votes, diana_votes, raymon_votes)
        #for candidate in candidates:
            #winner = 
    for candidate, votes in candidate_votes.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate
        
    return total_votes, winner, candidate_votes
total_votes, winner, candidate_votes =election_analysis(election_data)
    #return total_votes, charles_votes, diana_votes, raymon_votes, charles_percent, diana_percent, raymon_percent
#total_votes, charles_votes,diana_votes, raymon_votes, charles_percent, diana_percent, raymon_percent= election_analysis(election_data)
print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("-------------------------")
print("")
for candidate, votes in candidate_votes.items():
    percent = round(votes / total_votes * 100, 3)
    print(f"{candidate}: {percent}% ({votes})")
print("")
print("-------------------------")
print(f"Winner: {winner}")
print("")

#print("Total Votes: ",total_votes)
#print("")
#print("-------------------------")
#print("")
#print("Charles Casper Stockham: ", charles_percent,"%", "(",charles_votes,")")
#print("")
#print("Diana DeGette: ", diana_percent,"%", "(", diana_votes, ")")
#print("")
#print("Raymon Anthony Doane: ", raymon_percent,"%", "(", raymon_votes, ")")
#print("")
#print("-------------------------")
#print("")