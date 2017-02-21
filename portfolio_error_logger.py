#!/usr/bin/env python3
import datetime


def error_logger(error):
	# get date
	dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-8)))
	
	# open log file
	errorfile = open('error_log.txt', 'w')
	
	# write error info to file
	errorfile.write('**** New error on ')
	errorfile.write(str(dt))
	errorfile.write('\n')
	errorfile.write(error)
	errorfile.write('\n')
	errorfile.write('\n')
	
	# close log file
	errorfile.close()