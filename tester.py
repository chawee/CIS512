import csv
import numpy as np
import matplotlib.pyplot as pl
myfile=open('Most.csv','rt')
reader=csv.reader(myfile)
mylist=[]
for row in reader:
    mylist.append(row)
myfile.close()

myarray=np.asarray(mylist)
bugsind= np.flatnonzero(myarray[0,:]=='bugs')
#print (myarray[0,:]=='bugs')
bugs = myarray[1:,bugsind].astype(np.float)
ladderind=np.flatnonzero(myarray[0,:]=='frog')
ladder=myarray[1:,ladderind].astype(np.float)
#print (bugs[:,0])
#print (ladder[:,0])
m,b,z,d,myfit=np.polyfit(bugs[:,0],ladder[:,0],1,None,True,None,True)

fig=pl.figure()
ax=fig.add_subplot(111)
ax.plot(bugs,ladder,'o',color='r',label='Original')
ax.plot(bugs,ladder,color='k',label='linear fit')
ax.grid(True)
ax.set_xlabel('bugs')
ax.set_ylabel('frog')
ax.set_title('bugs vs frogs')
ax.legend()
fig.savefig('graph.png')