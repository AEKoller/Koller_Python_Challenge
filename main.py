import os
import csv

budget_data = os.path.join(os.path.dirname(__file__),'Pybank','Resources','budget_data.csv')
output_file_budget = os.path.join(os.path.dirname(__file__),'Pybank', 'Analysis', 'budget_results.txt')
election_data = os.path.join(os.path.dirname(__file__),'Pypoll', 'Resources','election_data.csv')
output_file_election = os.path.join(os.path.dirname(__file__),'Pypoll', 'Analysis', 'election_results.txt')


#budget_data analysis

#Calculating the total number of months included in the dataset
#The months are located within the first column within the data set. They are structured such that each row contains the first three letters
#of the month followed by the year. Becasue the data is structured the way that it is, a count function can be used
def budget_analysis(budget_data):
    num_of_months = 0
    prof_loss = 0
    monthly_change = []
    previous_month_profit_loss = None
    greatest_increase = 0
    greatest_decrease = 0
    with open (budget_data, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #this is needed to skip the header row
        next(csvreader)

        


        for row in csvreader:
            #becasue each row represents a new month, all we need to do is create a counter that adds to the sum total.
            #what this is essentially doing is adding +1 for every tow parsed within the data set
            num_of_months += 1
            current_date = row[0]
            #profit losses and gains are specific data, and therefore require a specific reference. In this part of the 
            #function, we are adding every integer to the variable 'prof_loss' from each cell in column 2 that is parsed
            prof_loss += int(row[1]) 
            #Now I need to create a function that calculates the the change from one month to the next. This requires that I
            #subtract the cell that comes after the current cell BY the current cell
            #First, I'll create a variable that identifies the integer that is in the current row, column 2, as the 
            #current integer 
            current_month_profit_loss = int(row[1])
            #Let me explain what is happening in the next lines. We've just initialized current_month_profit and 
            #established that it is the integer within column B(or 1) and in the current row being parsed.
            #previous_month_profit_loss was initialized in row 16 as None, meaning that it does not equal anything. if 
            #previous_month_profit_loss is still equal to nothing when it reaches the if statement below, then it skips to
            #after the if statement, where the value of previous_month_profit_loss beceomes equal to current_month_profit_loss
            #this puts us back to the top of the for loop, where the next row is parsed. When we finally get back down to
            #the if statement, previous_month_profit_loss is no longer none, but still the value assigned to it in the previous
            #loop. Becasue previous_month_profit_loss is no longer None, we go into the if statement. Here, we initialize change, 
            #and set it to the sum of current_month_profit_loss - previous_month_profit_loss. This then gets appended to a list
            #which we will use later to calculate the average. Lastly, we're changing the date value that is associated with with
            #increase and decrease so that we can reference that later in the .txt output
            if previous_month_profit_loss is not None:
                change = current_month_profit_loss - previous_month_profit_loss
                monthly_change.append(change)
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = current_date
                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = current_date
                
            previous_month_profit_loss = current_month_profit_loss
            
    average_change = sum(monthly_change)/ len(monthly_change)
    #Now I need to find the greatest increase and decrease, and I will do that by parsing through the list we created that contains the 
    #changes: monthly_change
    #greatest_increase = 0
    #greatest_decrease = 0
    #for change in monthly_change:
        # #if change > greatest_increase:
        #     greatest_increase = change
        # if change < greatest_decrease:
        #     greatest_decrease = change
        
    return num_of_months, prof_loss, average_change, monthly_change, greatest_increase, greatest_increase_date,greatest_decrease, greatest_decrease_date


#So, I completed the pypoll part of the assignment the first time around uising a "stupid" method that didn't use dictionaries. Once we had gone over dictionaries in class, 
#I realized that I could use disctionaries, and I went back and redid the script to utilize dictionaries. I've included the my old script because I am happy that I managed  
#to do it my way first, but I also wanted to provide the "right" way to do it based off our previous exercises.
def election_analysis(election_data):
    total_votes = 0
    candidate_votes = {'Charles Casper Stockham': 0, 'Diana DeGette': 0, 'Raymon Anthony Doane': 0}
    candidate_results = None
    #OLD STUPID CODE
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
            #OLD STUPID CODE
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
    
    
    return total_votes, winner, candidate_votes, candidate, votes


#output_financial = (
    #f"Financial Analysis\n"
    #f"----------------------------\n"
    #f"Total Months: {total_months}\n"
    #f"Total: ${total_net}\n"
    #f"Average Change: ${net_monthly_avg:.2f}\n"
    #f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    #f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#output_election == (
    #f"Financial Analysis\n"
    #f"----------------------------\n"
    #f"Total Months: {total_months}\n"
    #f"Total: ${total_net}\n"
    #f"Average Change: ${net_monthly_avg:.2f}\n"
    #f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    #f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


    #with open(file_to_output, "w") as txt_file:
    #txt_file.write(output)


num_of_months, prof_loss, average_change, monthly_change, greatest_increase, greatest_increase_date,greatest_decrease, greatest_decrease_date = budget_analysis(budget_data)

output_financial = None
output_financial = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total months: {num_of_months}\n"
    f"Total: ${prof_loss}\n"
    f"Average change: ${round(average_change,2)}\n"
    f"Greatest increase in profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(output_financial)
with open(output_file_budget, 'w') as file:
    file.write(output_financial)
print(greatest_decrease_date)
print(greatest_increase_date)
print(greatest_increase)
print(greatest_decrease)

# OLD STUPID CODE
# print("Financial Analysis\n")
# print("----------------------------\n")
# print(f"Total months: {total_months}\n")
# print(f"Total: ${total_prof_loss}\n")
# print(f"Average change: ${round(average_change,2)}\n")
# print(f"Greatest increase in profits: {greatest_increase_date} (${greatest_increase})\n")
# print(f"Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease})\n")


# OLD STUPID CODE
# with open(output_file_budget, 'w') as file:
#     file.write("Financial Analysis\n")
#     file.write("\n")
#     file.write("----------------------------\n")
#     file.write("\n")
#     file.write(f"Total months: {total_months}\n")
#     file.write("\n")
#     file.write(f"Total: {total_prof_loss}\n")
#     file.write("\n")
#     file.write(f"Average change: {average_change}\n")
#     file.write("\n")
#     file.write(f"Greatest increase in profits: ({greatest_increase_date}) {greatest_increase}\n")
#     file.write("\n")
#     file.write(f"Greatest decrease in profits: ({greatest_decrease_date}) {greatest_decrease}\n")


 #OLDER STUPIDER CODE
 #return total_votes, charles_votes, diana_votes, raymon_votes, charles_percent, diana_percent, raymon_percent
#total_votes, charles_votes,diana_votes, raymon_votes, charles_percent, diana_percent, raymon_percent= election_analysis(election_data)

total_votes, winner, candidate_votes, candidate, votes =election_analysis(election_data)
output_election = None
output_election = (
    "Election Results\n"
    "\n"
    "-------------------------\n"
    "\n"
    f"Total Votes: {total_votes}\n"
    "\n"
    "-------------------------\n"
    "\n"
)
for candidate, votes in candidate_votes.items():
        cand_percent = round(votes / total_votes * 100, 3)
        output_election += f"{candidate}: {cand_percent}% ({votes})\n"

output_election += (
    "\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n")

print(output_election)
with open(output_file_election, 'w') as file:
    file.write(output_election)

# OLD STUPID CODE
# with open(output_file_election, 'w') as file:
#     file.write("Election Results\n")
#     file.write("\n")
#     file.write("-------------------------\n")
#     file.write("\n")
#     file.write(f"Total Votes: {total_votes}\n")
#     file.write("\n")
#     file.write("-------------------------\n")
#     file.write("\n")
#     for candidate, votes in candidate_votes.items():
#         percent = round(votes / total_votes * 100, 3)
#         file.write(f"{candidate}: {percent}% ({votes})\n")
#     file.write("\n")
#     file.write("-------------------------\n")
#     file.write(f"Winner: {winner}\n")


#OLDER STUPIDER CODE
# print("Total Votes: ",total_votes)
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