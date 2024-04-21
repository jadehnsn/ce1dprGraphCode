import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib
import sys
import os
from uilib import *

# takes df and name of column in string and
# returns a list of every column entry 
def readDataFrameIntoList(df,columnName):
	lst = []
	for i in range(0,df.shape[0]):
		lst.append(df.loc[i,columnName])
	return lst

# reads data frame and then gives it back in indexed lists
def readData(file):
	df = pd.read_csv(file)
	dateLst = readDataFrameIntoList(df,"Date")
	timeLst = readDataFrameIntoList(df,"Time")
	dteTmeLst = formatTime(timeLst,dateLst)
	humid = readDataFrameIntoList(df,"Humidity")
	temp = readDataFrameIntoList(df,"Temperature")
	co2  = readDataFrameIntoList(df,"CO2")
	return dteTmeLst,humid,temp,co2

def formatTime(tlst,dlst):
	newLst = []
	for i in range(len(tlst)):
		tme = tlst[i].split(":")
		dte = dlst[i].split("/")
		newLst.append(datetime.datetime(int(dte[2]),int(dte[1]),int(dte[0]),int(tme[0]),int(tme[1]),int(tme[2])))
	return newLst
def plotXY(x,y,range1,fig,ax):


	dashed='dashed'

	newX,newY = [],[]
	for i in range(range1.start,range1.stop):
		newX.append(x[i])
	for i in range(range1.start,range1.stop):
		newY.append(y[i])

	plt.plot(newX,newY)

	# i hope the consequences of this code never reach me
	# i am sorry, i only needed the graphs :)

	# plt.plot([x[180],x[180]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door Shut',[x[180],0])
	# plt.plot([x[313],x[313]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door Cracked Open',[x[313],0])

	# plt.plot([x[876],x[876]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Tesco',[x[876],0])
	# plt.plot([x[883],x[883]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Outside',[x[883],0])

	# plt.plot([x[901],x[901]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door Open',[x[901],0])
	# plt.plot([x[923],x[923]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' p3 Leaves',[x[923],0])
	# plt.plot([x[966],x[966]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door Shut',[x[966],0])

	# plt.plot([x[994],x[994]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Campus',[x[994],0])

	# none

	# plt.plot([x[1057],x[1057]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Bus\n Stop',[x[1057],0])
	# plt.plot([x[1065],x[1065]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Bus',[x[1065],0])
	# plt.plot([x[1080],x[1080]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Shopping\n Centre',[x[1080],0])
	# plt.plot([x[1092],x[1092]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' BHF',[x[1092],0])
	# plt.plot([x[1102],x[1102]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' CR',[x[1102],0])
	# plt.plot([x[1109],x[1109]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' SR',[x[1109],0])
	# plt.plot([x[1115],x[1115]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Bus',[x[1115],0])

	# plt.plot([x[1166],x[1166]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' P3',[x[1166],0])
	# plt.plot([x[1191],x[1191]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' P3 \n leaves',[x[1191],0])
	# plt.plot([x[1258],x[1258]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door Open\n\n ',[x[1258],0])
	# plt.plot([x[1288],x[1288]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door shut',[x[1288],0])
	# plt.plot([x[1404],x[1404]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door Open\n\n ',[x[1404],0])
	# plt.plot([x[1423],x[1423]],[0,max(newY)],c='black',linestyle=dashed)
	# ax.annotate(' Door shut',[x[1423],0])

	plt.plot([x[873],x[873]],[0,max(newY)],c='black',linestyle=dashed)
	plt.plot([x[886],x[886]],[0,max(newY)],c='black',linestyle=dashed)
	plt.plot([x[980],x[980]],[0,max(newY)],c='black',linestyle=dashed)
	plt.plot([x[1006],x[1006]],[0,max(newY)],c='black',linestyle=dashed)
	plt.plot([x[1051],x[1051]],[0,max(newY)],c='black',linestyle=dashed)
	plt.plot([x[1131],x[1131]],[0,max(newY)],c='black',linestyle=dashed)
	



def main():

	# timeRange = inputTimeRange()
	file = 'fullReadout.csv'
	dteTmeLst,humid,temp,co2 = readData(file)

	# timeRange = range(150,873)
	# timeRange = range(874,886)
	# timeRange = range(886,980)
	# timeRange = range(980,1006)
	# timeRange = range(1006,1051)
	# timeRange = range(1051,1131)
	# timeRange = range(1132,1592)
	timeRange = range(150,1592)

	print(f'dttm: {dteTmeLst[:3]}-{dteTmeLst[len(dteTmeLst)-3:]}')
	print(f'humid: {humid[:3]}-{humid[len(humid)-3:]}')
	print(f'temp: {temp[:3]}-{temp[len(temp)-3:]}')
	print(f'co2: {co2[:3]}-{co2[len(co2)-3:]}')


	fig,ax = plt.subplots()
	#plt.plot(dteTmeLst,humid)
	#plt.plot(dteTmeLst,temp)
	#plt.plot(dteTmeLst,co2)
	
	plotXY(dteTmeLst,co2,timeRange,fig,ax)

	plt.xlabel("Time")
	plt.ylabel("co2")
	ax.xaxis.set_major_formatter(DateFormatter("%H:%M"))
	fig.set_size_inches(8, 6)
	plt.title('CO2 Against time')
 
	plt.show()


	return 0




if __name__ == "__main__":
	print(f'\nTerminating: {main()}')

# References
'''
Formatting dates with matplotlib: https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/customize-dates-matplotlib-plots-python/


'''