import os
import csv


print("Election Results")
print("---------------------------")

Polldata = os.path.join('Polling_Data.csv')
PollResults = os.path.join('PollResults.txt')

Voters = []
Khan_total = 0
Correy_total = 0
li_total = 0
otooley_total = 0

with open(Polldata, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        votes = row [0]

        Voters.append(votes)

        TotalVoters = len(Voters)
    
        if row[2] == "Khan":
            Khan_total += 1
        elif row[2] == "Correy":
            Correy_total += 1
        elif row[2] == "Li":
            li_total += 1
        elif row[2] == "O'Tooley":
            otooley_total += 1

KP = (Khan_total/TotalVoters) *100
CP = (Correy_total/TotalVoters) *100
LP = (li_total/TotalVoters) *100
OP = (otooley_total/TotalVoters) *100


print("Total Votes: " + str(TotalVoters))
print("----------------------------------------")
print(f"Khan: {KP:.3f}% ({Khan_total})")
print(f"Correy:  {CP:.3f}% ({Correy_total})")
print(f"Li: {LP:.3f}% ({li_total})")
print(f"O'Tooley: {OP:.3f}% ({otooley_total})")
print("----------------------------------------")

if Khan_total > Correy_total and Khan_total > li_total and Khan_total > otooley_total:
    print("Winner: Khan")
elif Correy_total > Khan_total and Correy_total > li_total and Correy_total > otooley_total:
    print("Winner: Correy")
elif li_total > Khan_total and li_total > Correy_total and li_total > otooley_total:
    print ("Winner : Li")
elif otooley_total > Khan_total and otooley_total > li_total and otooley_total > Correy_total:
    print("Winner O'Tooley")
else:
    print("No one wins")


with open(PollResults,"w") as txt_file:

# Write methods to print to Elections_Results_Summary 
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(TotalVoters))
    txt_file.write("\n")
    txt_file.write("------------------------------")
    txt_file.write("\n")
    txt_file.write(f"Khan: {KP:.3f}% ({Khan_total})")
    txt_file.write("\n")
    txt_file.write(f"Correy: {CP:.3f}% ({Correy_total})")
    txt_file.write("\n")
    txt_file.write(f"Li: {LP:.3f}% ({li_total})")
    txt_file.write("\n")
    txt_file.write(f"O'Tooley: {OP:.3f}% ({otooley_total})")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: Khan ")
    txt_file.write("\n")
    txt_file.write("------------------------------")
