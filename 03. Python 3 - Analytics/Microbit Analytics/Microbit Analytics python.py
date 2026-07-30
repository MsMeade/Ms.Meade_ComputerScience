import statistics
import matplotlib.pyplot as plt

# Read in Data from CSV File
file=open("microbit.csv","r")

Data=file.read()

file.close()

#____________________________________________

# Making Lists from our data.
#print(Data)
myList=Data.split(",")
#print(myList)

#Cleaning Data.
cleanList = " ".join(myList).replace('\n', ' ').split()
#print(cleanList)


tempList=[]
lightList=[]
timeList=[]


#pick out every 3rd element in the list and add it to tempList.
for i in range(0,len(cleanList),3):
    tempList.append(cleanList[i])
#print(tempList)

for i in range(1,len(cleanList),3):
    lightList.append(cleanList[i])
#print(lightList)

for i in range(2,len(cleanList),3):
    timeList.append(cleanList[i])
#print(timeList)

#Remove incorrect data from lists.
timeList.remove(timeList[0])
#print(timeList)

lightList.remove(lightList[0])
lightList.remove(lightList[0])
#print(lightList)

tempList.remove(tempList[0])
tempList.remove(tempList[0])
#print(tempList)

#Convert the strings to numbers.
for i in range(len(timeList)):
    timeList[i]=float(timeList[i])
print(timeList)

for i in range(len(tempList)):
    tempList[i]=int(tempList[i])
print(tempList)

for i in range(len(lightList)):
    lightList[i]=int(lightList[i])
print(lightList)

#Analytics
#mean,median,mode, range, max,min, draw graphs.

# Mean temperature
meanTemp= statistics.mean(tempList)
print("The mean temperature is", meanTemp)

# Modal Light value
modeLight= statistics.mode(lightList)
print("The modal light value is", modeLight)

# Median temperature
medianTemp= statistics.median(tempList)
print("The median temperature is", medianTemp)

# Max & Min temp
maxTemp=max(tempList)
print("The maximum tempertaure is",maxTemp)

minTemp=min(tempList)
print("The minimum tempertaure is",minTemp)

# Max & Min light value
maxLight=max(lightList)
print("The maximum Light level is",maxLight)

minLight=min(lightList)
print("The minimum Light level is",minLight)

# Range of temperatures & light values
TempRange=maxTemp-minTemp
print(TempRange)

LightRange=maxLight-minLight
print(LightRange)

# Range of time
TimeRange=max(timeList)-min(timeList)
print(TimeRange)

# At what time did the microbit regester the maximum light level for the first time?
maxLIndex=lightList.index(maxLight)
print("The maximum light level was reached at", timeList[maxLIndex],"seconds")

# What was the light level when the microbit regestered 0oC for the first time?
minTIndex=tempList.index(minTemp)
print("The light level was", lightList[minTIndex]," when the temperature was 0oC for the first time")

# ___________________________________________________________________
# Graphing the Data

#Bar chart
plt.bar(timeList,tempList,color="blue")
#plt.bar(names,presents,color="skyblue")

plt.title("Temp vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (oC)")
plt.show()

#Line Plot
plt.plot(timeList,tempList,"y-.")
plt.plot(lightList,"k")
plt.title("Light & Temperature vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Light & Temp")
plt.show()










