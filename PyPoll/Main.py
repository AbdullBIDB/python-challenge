import os
import csv

data_csv = os.path.join ("Resources", "election_data.csv")


#determine the list of:
voteid = []
county = []
candidate = []


#read the file
with open(data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)


    #insert the column into the following list: voteid, county, candidate
    for row in csvreader:
        voteid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


print("Election Results")
print("------------------")
#total votes cast
total_vote = len(voteid)
print("Total Votes: " + str(total_vote))

print("------------------")

#identify the candidates in the data
k = "Khan"
c = "Correy"
l = "Li"
o = "O'Tooley"

#counting the number of votes each candidate got also the percentage
print("")
khanvote = candidate.count(k)
kpercentage = round((khanvote/total_vote)*100)
print("Khan: "+ str(kpercentage)+"%" + "  " + "("+str (khanvote)+")")


Correyvote = candidate.count(c)
cpercentage = round((Correyvote/total_vote)*100)
print("Correy: "+ str(cpercentage) + "  " + "("+str (Correyvote)+")")


livote = candidate.count(l)
lpercentage = round((livote/total_vote)*100)
print("Li: "+ str(lpercentage) +"%"+ "  " + "("+str (livote)+")")


tooleyvote = candidate.count(o)
tpercentage = round((tooleyvote/total_vote)*100)
print("O'Tooley: "+ str(tpercentage) +"%"+ "  " + "("+str (tooleyvote)+")")
print("")
print("------------------")

#creating a list of winning candidate
w_list = [khanvote , Correyvote, livote,tooleyvote]
winner = max(w_list)

if winner == khanvote:
    print("Winner is: " + k)
elif winner == Correyvote:
    print("Winner is: " + c)
elif winner == livote:
    print("Winner is: " + l)
else:
    print("Winner is: " + o)

distination = os.path.join('output','pypoll.txt')
with open(distination, "w") as file:
    file.writelines("Election Results"+"\n")
    file.writelines("------------------"+"\n")
    file.writelines("Total Votes: " + str(total_vote)+"\n")
    file.writelines("------------------"+"\n")
    file.writelines("Khan: "+ str(kpercentage)+"%" + "  " + "("+str (khanvote)+")"+"\n")
    file.writelines("Correy: "+ str(cpercentage) + "  " + "("+str (Correyvote)+")"+"\n")
    file.writelines("Li: "+ str(lpercentage) +"%"+ "  " + "("+str (livote)+")"+"\n")
    file.writelines("O'Tooley: "+ str(tpercentage) +"%"+ "  " + "("+str (tooleyvote)+")"+"\n")
    file.writelines(""+"\n")
    file.writelines("------------------"+"\n")
    if winner == khanvote:
        file.writelines("Winner is: " + k+"\n")
    elif winner == Correyvote:
        file.writelines("Winner is: " + c+"\n")
    elif winner == livote:
        file.writelines("Winner is: " + l+"\n")
    else:
        file.writelines("Winner is: " + o+"\n")    




    