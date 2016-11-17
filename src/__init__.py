from yahoo_finance import Share
from datetime import datetime,timedelta,date
#import unicodedata
import copy

def getCurrPrice(tick,date):
	stock=Share(tick)
	try:
		stock.get_historical(date,date)
	except:
		return None
	
	stock_detail=stock.get_historical(date,date)
	#print stock_detail
	if len(stock_detail) is 0:
		return None
	else:
		return float(stock_detail[0]['Adj_Close'])

	
def getPrice(tick,days): #(yahoo tick,latest date, how many days look back)
	current_date=datetime.now()
	#print current_date
	#day_left=days
	#day_left-=1
	#day_left=days
	price_list=[]
	loop_times=0 # use to control the times of try
	#price=1
	
	while days>0 and loop_times<20: #if try times greater than 100
		#print day_left
		#price=0
		cur_str= current_date.strftime("%Y-%m-%d")
		#print cur_str
		#pirce=getCurrPrice(tick,cur_str)
		
		#print getCurrPrice(tick,cur_str)
		#print price
		if getCurrPrice(tick,cur_str) is None:
			current_date=current_date-timedelta(days=1)
			loop_times+=1
			#days-=1
			continue
		else:
			#print price
			price_list.append(getCurrPrice(tick,cur_str))
			current_date=current_date-timedelta(days=1)
			days-=1
	return price_list
	
	
	
	#print current_date.strftime("%Y-%m-%d")
	#$print (current_date-timedelta(days=1)).strftime("%Y-%m-%d")
	

#print getCurrPrice('YHOO','2016-11-14')
#print a
#print type(a)
#a= getPrice('YHOO',30)
#print a
#print len(a)

'''
def getWildPrice(tick,date):
	look_back_days=60
	begin_date=datetime.now()-timedelta(days=look_back_days)
	stock=Share(tick)
	raw_list=
'''
	
