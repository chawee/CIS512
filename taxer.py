import csv
f=open('/home/briantorsey/CIS512/SFHFCLData.csv','r')
data=csv.reader(f)
states=[]

for i in data:
    if "****" not in i:
        splitline=i.split(',')
        if len(splitline[0]) < 20:
            states.append(splitline[1])
print (states)
