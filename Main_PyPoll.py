# Import modules
import os
import csv

# Set the input/output path 
input_path = os.path.join(r"C:\Users\Chloe\OneDrive\Desktop\Bootcamp\Challenge_3\PyPoll\election_data.csv")
output_path = os.path.join(r"C:\Users\Chloe\OneDrive\Desktop\Bootcamp\Challenge_3\PyPoll\Election Results.txt")

# Set variables
total_count = 0 
Charles_count = 0
Diana_count = 0
Raymon_count = 0

# Open csv file
with open(input_path) as elections:

    csvreader = csv.reader(elections,delimiter=",") 
    header = next(csvreader)     

  # Loop through to count
    for row in csvreader: 

        total_count +=1

        if row[2] == "Charles Casper Stockham": 
            Charles_count+=1
        elif row[2] == "Diana DeGette":
            Diana_count+=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_count+=1

candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
counts = [Charles_count, Diana_count,Raymon_count]

# Calculate the winner
candidates_counts = {"Charles Casper Stockham":Charles_count, "Diana DeGette":Diana_count,"Raymon Anthony Doane":Raymon_count}
winner = max(candidates_counts.items(), key=lambda item:item[1])

Charles_percent = (Charles_count/total_count) *100
Diana_percent = (Diana_count/total_count) * 100
Raymon_percent = (Raymon_count/total_count)* 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_count}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_count})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_count})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_count})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

with open(output_path,"w") as file:
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_count}\n")
    file.write(f"----------------------------\n")
    file.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_count})\n")
    file.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_count})\n")
    file.write(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_count})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"----------------------------")