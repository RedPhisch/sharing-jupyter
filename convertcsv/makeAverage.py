import csv
import sys
from datetime import datetime, timedelta
import time
import json


# In[68]:


#create dataframe with all time values for time period



csvfile = 'pythonoutput.csv'
ofile=open('pythonoutput2.csv',"w")
writer1=csv.writer(ofile, delimiter=',',quotechar="\"",quoting=csv.QUOTE_ALL)
outrow = list()
result = list()
currentMinute = 0
countValuePerMinute = 0
averagePerMinute = 0

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
                    if row is 0:
                        previousRow = 0
                    else:
                        previousRow = row - 1
                    previousDateTime = datetime.strptime((previousRow)[colnum],"%b %d, %Y %H:%M:%S %p")
                    currentMinute = datetime.strptime(row[colnum], "%M")

                    if dt2 != previousDateTime:
                        if currentMinute == previousMinute:
                            sumTotalPerMinute += row[colnum + 1]
                            countValuePerMinute += 1
                            averagePerMinute = sumTotalPerMinute / countValuePerMinute
                            row[colnum + 1] = averagePerMinute
                        else:   
                            sumTotalPerMinute = 0
                            countValuePerMinute = 0
                            averagePerMinute = 0
                            sumTotalPerMinute += row[colnum + 1]
                            countValuePerMinute += 1
                            averagePerMinute = sumTotalPerMinute / countValuePerMinute
                            row[colnum + 1] = averagePerMinute
                        pass

                    dt3 = dt2.replace(second=0, microsecond=0)
                    print("dt3", dt3)
                    outrowdt=dt2                    
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

ifile.close()
ofile.close()


# In[14]:

