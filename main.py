import os
import csv

budget_data = os.path.join('Pybank','Resources','budget_data.csv')
#election_data = os.path.join('PyPoll\Resources\election_data.csv')

#budget_data analysis

#Calculating the total number of months included in the dataset
#The months are located within the first column within the data set. They are structured such that each row contains the first three letters
#of the month followed by the year. Becasue the data is structured the way that it is, a count function can be used
def budget_analysis(budget_data):
    num_of_months = 0
    prof_loss = 0

    with open (budget_data, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #this is needed to skip the header row
        next(csvreader)

        for row in csvreader:
            #becasue each row represents a new month, all we need to do is create a counter that adds to the sum total.
            #what this is essentially doing is adding +1 for every tow parsed within the data set
            num_of_months += 1
            #profit losses and gains are specific data, and therefore require a specific reference. In this part of the 
            #function, we are adding every integer to the variable 'prof_loss' from each cell in column 2 that is parsed
            prof_loss += int(row[1]) 
           
    return num_of_months, prof_loss

total_months = budget_analysis(budget_data)
total_prof_loss = budget_analysis(budget_data)
print("Total number of months: ", total_months)
print("Total loss/profit: ", total_prof_loss)