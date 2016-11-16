from  __init__ import getPrice,getCurrPrice
from yahoo_finance import Share
import sys
import argparse
import csv
from datetime import datetime,timedelta,date

#print len(sys.argv)
#first agurment is yahoo finance instrument ticket

#now tyring agurement paser
#add share you wanna download here:
ticketlist=["AAPL","YHOO"]

if sys.argv[1]=="-f":  #this part is for loading mutiplule shares from list of csv file
	#file_path="../data/TicketList.csv"
	#with open(file_path) as csvfile:
	#	ticket
#	wih open(file_path) as ticketlist:
#		for line in ticketlist:
#			print line
	#ticketlist=open(file_path,'r')

	output_file=open("../data/Prices.csv","wb")
	#wr=csv.writer(output_file,dialect='excel')
	for ticket in ticketlist:
		print ticket
		#print type(ticket)
		tmp_list=getPrice(ticket,30)
		#ticket.extend(tmp_list)
		print tmp_list
		print ticket
		output_file.write(ticket+',')
		for e in tmp_list
		#output_line=[ticket].extend(tmp_list)
		#print output_line
		#wr.writerows(ls)

	#ticketlist.close()
	output_file.close()
			

if sys.argv[1]=="-d": #for single historical data load
	Tick=str(sys.argv[2])
	yahoo=Share(Tick)
	print "The historical price is as followed:"
	print yahoo.get_historical(str(sys.argv[3]),str(sys.argv[4]))
'''
if len(sys.argv)==2:
	Tick=str(sys.argv[1])
	yahoo=Share(Tick)
	#print "current price is :{}".format(yahoo.get_price())

'''
'''
else:
	print("the argument length is incorrect")
'''

#print yahoo.get_historical('2016-04-25','2016-05-05')

