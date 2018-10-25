# sharing-jupyter


# coding: utf-8

# In[ ]:


#current method isn't working
#work on creating a separate list for each timestamp/value pair
#then merge lists with merge or union or join - research which will do what is needed.


# In[67]:


import csv
import sys
from datetime import datetime, timedelta
import time
import json


# In[68]:


#create dataframe with all time values for time period

#set time period start and end
periodstart = datetime.strptime("2018-09-19 00:00:00","%Y-%m-%d %H:%M:%S")
periodend = datetime.strptime("2018-10-20 00:00:00","%Y-%m-%d %H:%M:%S")
currenttime = periodstart
timelist = []
while currenttime < periodend:
    timelist.append(currenttime)
    currenttime = currenttime + timedelta(minutes = 1)
print(timelist)


# In[87]:


# all files to be converted and merged
filelist = ['ASH4CWHW2.csv']
ofile=open('pythonoutput.csv',"w")
writer1=csv.writer(ofile, delimiter=',',quotechar="\"",quoting=csv.QUOTE_ALL)
outrow = list()
result = list()
filecounter = 0
#loop through files
for csvfile in filelist:
    #define input files
    ifile=open(csvfile,"r")
    reader1=csv.reader(ifile)
    reader1RowNum=0
    
    #loop through contents of file
    for row in reader1:
#        numcolumns = row.len()
#        print(numcolumns)
        outrow.clear()
        if reader1RowNum==0:
            header=row
            colnum=0
            numrows=0
            for col in row:
                print (header[colnum])
                
#                datasetnum = colnum/2 - colnum%2
   #             result[datasetnum]
                colnum+=1
        else:
            colnum=0
            for col in row:
                if colnum % 2 == 0: #column is even then the data should be a date
                    outrow.clear()
                    if(row[colnum]==''):
                        outrowdt==''
                    else:
                        dt=datetime.strptime(row[colnum],"%b %d, %Y %I:%M:%S %p")
                        dt2=datetime.strptime(row[colnum],"%b %d, %Y %H:%M:%S %p")

                        print("Hour1:", dt.hour)
                        print("Hour2:", dt2.hour)    
                        #dt=datetime.utcfromtimestamp(row[0])
#                        print("dt",dt)
 #                       print("dt2",dt2)
                        dt3 = dt2.replace(second=0, microsecond=0)
                        print("dt3", dt3)
                        outrowdt=dt
                        
                else:
                    val=row[colnum]
                    print(val)
                    outcolnum=round(colnum/2+.5)
                    print(outcolnum)
                    outrow.insert(0,outrowdt)
                    outrow.insert(outcolnum,val)
                    writer1.writerow(outrow)
                colnum+=1            
            numrows +=1                    
        reader1RowNum+=1
        if reader1RowNum==5000:
            break
    print (numrows)
    ifile.close()
    filecounter +=1
#end loop through files

ofile.close()


# In[14]:

