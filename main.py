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
    monthly_change = []
    previous_month_profit_loss = None

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
            #Now I need to create a function that calculates the the change from one month to the next. This requires that I
            #subtract the cell that comes after the current cell BY the current cell
            #First, I'll create a variable that identifies the integer that is in the current row, column 2, as the 
            #current integer 
            current_month_profit_loss = int(row[1])
            #Let me explain what is happening in the next 5 lines. We've just initialized current_month_profit and 
            #established that it is the integer within column B(or 1) and in the current row being parsed.
            #previous_month_profit_loss was initialized in row 16 as None, meaning that it does not equal anything. if 
            #previous_month_profit_loss is still equal to nothing when it reaches the if statement below, then it skips to
            #after the if statement, where the value of previous_month_profit_loss beceomes equal to current_month_profit_loss
            #this puts us back to the top of the for loop, where the next row is parsed. When we finally get back down to
            #the if statement, previous_month_profit_loss is no longer none, but still the value assigned to it in the previous
            #loop. Becasue previous_month_profit_loss is no longer None, we go into the if statement. Here, we initialize change, 
            #and set it to the sum of current_month_profit_loss - previous_month_profit_loss. This then gets appended to a list
            #which we will use later to calculate the avaerage.
            if previous_month_profit_loss is not None:
                change = current_month_profit_loss - previous_month_profit_loss
                monthly_change.append(change)
                
            previous_month_profit_loss = current_month_profit_loss
            
    average_change = sum(monthly_change)/ len(monthly_change)
    #Now I need to find the greatest increase and decrease, and I will do that by parsing through the list we created that contains the 
    #changes: monthly_change
    greatest_increase = 0
    greatest_decrease = 0
    for change in monthly_change:
        if change > greatest_increase:
            greatest_increase = change
        if change < greatest_decrease:
            greatest_decrease = change
        
    return num_of_months, prof_loss, average_change, monthly_change, greatest_increase, greatest_decrease

total_months, total_prof_loss, average_change, monthly_change, greatest_increase, greatest_decrease = budget_analysis(budget_data)
print("")
print("Financial Analysis")
print("")
print("----------------------------")
print("")
print("Total months: ", total_months)
print("")
print("Total: ", total_prof_loss)
print("")
print("Average change: ", average_change)
print("")
print("Greatest increase in profits: ", greatest_increase)
print("")
print("Greatest decrease in profits: ", greatest_decrease)
print("")
## I used this to double check my answers by cross referencing the returned list to Excel data
#print("Here's a list of monthly changes: ", monthly_change) 
