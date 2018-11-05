import os
import csv
import statistics as s

data_csv = os.path.join ("Resources", "budget_data.csv")

#determine the list of 
date = []
pl = []

#read the file
with open(data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)



#insert the column into the list date and pl.
    for row in csvreader:
    
        date.append(row[0])
        pl.append(int(row[1]))

print(" ")
print("Financial Analysis")
print(" ")
print("--------------------------")
print(" ")
#Total Months
total_month = len(date)
print("Total Months: ",total_month)
#Total
total_pl = sum(pl)
print("Total: ", "$"+str(total_pl))

#deterning the average change, greatest increase, and greatest decrease
b_list = []
for i in range(85):
    z = (pl[i] - pl[i+1])*-1
    b_list.append(z)
    #print(b_list)
g = max(b_list)
d = min(b_list)
a = round(s.mean(b_list), 2)
print("Average  Change: ", "$"+str(a))
print("Greatest Increase in Profits: ",date[b_list.index(max(b_list))+1],":" , "("+"$"+str(g)+")")
print("Greatest Decrease in Profits: ",date[b_list.index(min(b_list))+1],":" , "("+"$"+str(d)+")")


#export the results to a txt file:
distination = os.path.join('output','pybank.txt')
with open(distination, "w") as file:
    file.writelines(" "+"\n")
    file.writelines("Financial Analysis"+"\n")
    file.writelines("--------------------------"+"\n")
    file.writelines("Total Months: " + str(total_month) +"\n")
    file.writelines("Total: " + "$"+str(total_pl)+"\n")
    file.writelines("Average  Change: " + "$"+str(a)+"\n")
    file.writelines("Greatest Increase in Profits: " + date[b_list.index(max(b_list))+1] + ":" + "("+"$"+str(g)+")"+"\n")
    file.writelines("Greatest Decrease in Profits: " + date[b_list.index(min(b_list))+1] + ":" + "("+"$"+str(d)+")"+"\n")