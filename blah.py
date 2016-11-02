import csv
import matplotlib.pyplot as pl
import numpy as np
myfile=open('most.csv','rt', encoding='latin-1')
reader=csv.reader(myfile)
mylist=[]
for row in reader:
    mylist.append(row)
myfile.close()

myarray=np.asarray(mylist)
print (myarray[0,:])