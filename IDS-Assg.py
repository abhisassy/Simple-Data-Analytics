
# coding: utf-8

# # IDS ASSIGNMENT-1
Abhishek Saseendran 01FB16ECS018Akash Bhat 01FB16ECS038
# In[15]:

import csv



#create the file required 

file1=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/apy.csv")
file2=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/Dharwad.csv","w",newline="")
file3=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/Koppal.csv","w",newline="")
file4=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/KoppalSummer.csv","w",newline="")
file5=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/KoppalKharif.csv","w",newline="")
file6=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/DharwadSummer.csv","w",newline="")
file7=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/DharwadKharif.csv","w",newline="")
reader=csv.reader(file1)
next(reader)
w1=csv.writer(file2)
w2=csv.writer(file3)
w4=csv.writer(file4)
w5=csv.writer(file5)
w6=csv.writer(file6)
w7=csv.writer(file7)

for row in reader:
    if row[0]=="Karnataka":
        if row[4]=="Rice":
            if row[1]=="KOPPAL":
                w2.writerow(row)
                if row[3]=="Kharif     ":
                    w5.writerow(row)
                if row[3]=="Summer     ":
                    w4.writerow(row)
            if row[1]=="DHARWAD":
                w1.writerow(row)
                if row[3]=="Kharif     ":
                    w7.writerow(row)
                if row[3]=="Summer     ":
                    w6.writerow(row) 



file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()


# In[97]:

#start ploting graphs
#1 graph Produce v Year Stacked Bar Graph
#2 box and whisker graph
import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from collections import Counter
import pandas as pd
file1=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/Dharwad.csv")
file2=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/Koppal.csv")
production1=[]
production2=[]
year=[]
r1=csv.reader(file1)
r2=csv.reader(file2)

for row in r1:
    production1.append(float(row[6]))
    
for row in r2:
    production2.append(float(row[6]))
    year.append(row[2])
    


N = len(production1)


ind = np.arange(N)    # the x locations for the groups
width = 0.75


p1 = plt.bar(ind, production1, width, color='red',yerr=0)
p2 = plt.bar(ind, production2, width,
             bottom=production1,yerr=0)

plt.ylabel('Production (in kg)')
plt.title('Rice Production for both Cropping Seasons')
plt.xticks(ind, year,rotation=90)
plt.yticks(np.arange(0, 300001, 50000))
plt.legend((p1[0], p2[0]), ('Dharwad', 'Koppal'))
plt.xlabel("Year")
plt.show()

print("No. of years:(Sample size) ",len(year)/2)
print("----Dharwad Rice Production----")
print("Min production :",min(production1)," kg")
print("Max production : ",max(production1)," kg")
print("Mean production:",st.mean(production1)," kg")
print("Median production:",st.median(production1)," kg")
print("Quartiles :",np.percentile(production1, np.arange(0, 100, 25)))
df=pd.DataFrame(production1,columns=["Dharwad"])
df.plot.box()
plt.show()
print()
print("----Koppal Rice Production----")
print("Min production :",min(production2)," kg")
print("Max production : ",max(production2)," kg")
print("Mean production:",st.mean(production2)," kg")
print("Median production:",st.median(production2)," kg")
print("Quartiles :",np.percentile(production2, np.arange(0, 100, 25)))
df=pd.DataFrame(production2,columns=["Dharwad"])
df.plot.box()
plt.show()

#




# >Both these districts arelocated relatively towards the north-west side of   Karnataka, with a distance of 143km between them and receive more or less   the same climatic situations.
#   Looking into the Rice Production in these areas,from the above graph it is   very evident thta Koppal surmounts Dharwad in rice production. The margin   of difference in production is very high.
# 

# In[98]:

#Production density 
#Area graph and Bar graph
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


file1=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/DharwadSummer.csv")
file2=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/KoppalSummer.csv")
r1=csv.reader(file1)
r2=csv.reader(file2)
year=[]
pro_den1=[]
pro_den2=[]
for row in r1:
    pro_den1.append(float(row[6])/float(row[5]))
for row in r2:
    pro_den2.append(float(row[6])/float(row[5]))
    year.append(row[2])


#individual graphs 
#Area
file1=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/Dharwad.csv")
file2=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/Koppal.csv")
r1=csv.reader(file1)
r2=csv.reader(file2)
area1=[]
area2=[]
year=[]
for row in r1:
    area1.append(float(row[5]))
for row in r2:
    area2.append(float(row[5]))
    year.append(int(row[2]))
plt.ylabel("AREA(in ha)")
plt.xlabel("Year")
plt.title("Dharwad")
plt.bar(year,area1)
plt.xticks(year,list(year),rotation=45)
plt.show()

plt.ylabel("AREA(in ha)")
plt.xlabel("Year")
plt.title("Koppal")
plt.bar(year,area2)
plt.xticks(year,list(year),rotation=45)
plt.show()

#production density
x=range(len(pro_den1))
plt.ylabel("Yield/ha")
plt.xlabel("Year")
plt.title("Dharwad")
plt.bar(range(len(pro_den1)),pro_den1)
plt.xticks(x,list(year),rotation=45)
plt.yticks([0,1,2,3,4,5,6])
plt.show()



plt.ylabel("Yield/ha")
plt.xlabel("Year")
plt.title("Koppal")
plt.bar(x,pro_den2)
plt.xticks(x,list(year),rotation=45)
plt.yticks([0,1,2,3,4,5,6])
plt.show()




#comparison graph

plt.stackplot(np.arange(len(year)),
              pro_den2,color='red')
plt.stackplot(np.arange(len(year)),
              pro_den1,color='blue')

plt.yticks(np.arange(0,max(pro_den2)))
plt.xlim(0,17-1)



# creating the legend manually
plt.legend([mpatches.Patch(color='red'), 
            mpatches.Patch(color='blue')], 
           ['Koppal','Dharwad'])
plt.xticks(x,list(year),rotation=45)
plt.ylabel("Yield/ha")
plt.xlabel("Year")
plt.title("Dharwad v Koppal")
plt.show()


# >Looking at the production Density Distribution, the difference between the two districts reduce. Here the production density i.e. Yield per hectare of land under cultivation of Koppal is just a bit above that of Dharwad.
#> Since there are two predominant seasons affecting the yield in these areas, we compare the produce during these two seasons 
#                                                   Summer & Kharif
# In[75]:

#Variation with season 
#line graph
import csv
import numpy as np
import matplotlib.pyplot as plt
import pylab


file=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/Rain.csv")
r=csv.reader(file)
data1=[]
data2=[]
next(r)

for row in r:
    if row[1]=="Dharwad":
        data1.append(float(row[15]))
    if row[1]=="Koppal":
        data2.append(float(row[15]))

plt.title("Annual Rainfall")        
plt.scatter([2004,2005,2006,2007,2008,2009,2010],data1,color="red")
plt.scatter([2004,2005,2006,2007,2008,2009,2010],data2,color="blue")
plt.legend((p1[0], p2[0]), ('Dharwad', 'Koppal'))
plt.ylabel("Rainfall (in mm)")
plt.xlabel("Year")
plt.show()
file.close()

file1=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/DharwadSummer.csv")
file2=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/DharwadKharif.csv")
r1=csv.reader(file1)
r2=csv.reader(file2)
prod1=[]
prod2=[]
year=[]
for row in r1:
    prod1.append(float(row[6]))
for row in r2:
    prod2.append(float(row[6]))
    year.append(int(row[2]))
   
#print("---------------DHARWAD--------------")
x=np.arange(len(year))
plt.plot(x,prod1)
plt.plot(x,prod2,color="red")
plt.xticks(x,list(year),rotation=45)
plt.yticks([0,50000,100000,150000,200000])
plt.ylabel("Produce (in kg)")
plt.xlabel("Year")
plt.title("DHARWAD")
plt.legend((p1[0], p2[0]), ('Kharif', 'Summer'))
plt.show()


file1=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/KoppalSummer.csv")
file2=open("C:/Users/jedib/Desktop/3sem/IDS/PROJECT/KoppalKharif.csv")
r1=csv.reader(file1)
r2=csv.reader(file2)
prod1=[]
prod2=[]
year=[]
for row in r1:
    prod1.append(float(row[6]))
for row in r2:
    prod2.append(float(row[6]))
    year.append(int(row[2]))

#print("---------------Koppal--------------")

plt.plot(x,prod1)
plt.plot(x,prod2,color="red")
plt.ylabel("Produce (in kg)")
plt.xlabel("Year")
plt.title("KOPPAL")
plt.xticks(x,list(year),rotation=45)
plt.yticks([0,50000,100000,150000,200000])
plt.legend((p1[0], p2[0]), ('Kharif', 'Summer'))
plt.show()


# >Here we see a suprising fact that even though yeild in Dharwad is lesser, it recieves more annual rainfall than Koppal.
# 
# For both districts, Yield is obviously higher during Kharif. 
# Due to irrigation facilities the difference in yeild between the two seasons isn't drastic. However it is noticeable that around 2000-2001 these's a huge dip in yeild due to severe droughts in these areas. 
# Also Dharwad faces hasrsher summer terms with minimal production of rice.
#Bibilography: All Data used are taken from : www.data.gov.in