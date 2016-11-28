import csv
import pandas as pd
import tushare as ts
import numpy as np
from  datetime import datetime,timedelta


#Read stock code in to array
def getStockList():
	StockList=[]
	with open('../data/StockList.csv') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			StockList.append(row['code'])
			#print row['code']
	return StockList

#construct  DateList


def getDateList(start,end):
	DateList=[]
	StartDate=datetime.strptime(start,"%Y-%m-%d")
	EndDate=datetime.strptime(end,"%Y-%m-%d")
	CurrentDate=EndDate
	while CurrentDate>=StartDate:
		DateList.append(CurrentDate.strftime("%Y-%m-%d"))
		CurrentDate=CurrentDate-timedelta(days=1)

	return DateList

                                  
 


StockList=getStockList()
DateList=getDateList("2016-02-01","2016-02-29")
def getPriceTable(DateList,StockList):
	PriceTable=pd.DataFrame(columns=DateList,index=StockList)
	PriceTable=PriceTable.fillna(value=-1)

	for stock in PriceTable.index.values:	
		SinglePrice=ts.get_hist_data(stock,start=DateList[-1],end=DateList[0])
		for date in SinglePrice.index.values:
			PriceTable.loc[stock,date]=SinglePrice.loc[date,'close']
	HolidayList=[]
	for date1 in PriceTable.columns.values:
		CurrDateUniPrice=np.unique(PriceTable.loc[:,date1]).tolist()
	#	print CurrDateUniPrice
		if len(CurrDateUniPrice)==1 and CurrDateUniPrice[0]==-1:
			HolidayList.append(date1)
	TradingDateList=sorted(list(set(DateList)-set(HolidayList)),reverse=True)
	#print TradingDateList
	return PriceTable.loc[:,TradingDateList]

print getPriceTable(DateList,StockList)







