#!/usr/bin/env python3
#from portfolio_updater_ES.py import es_updater
#from portfolio_updater_DB.py import db_updater
import portfolio_error_logger
import portfolio_consts
import portfolio_riskmodel
import json
import requests

# python3 -m pip install <package name>

# get yahoo data
res = requests.get(portfolio_consts.url)

if res.status_code >= 400:
	# log error
	portfolio_error_logger.error_logger('line 11 of portfolio_main ' + str(res.raise_for_status()))
	return

# try decoding the json response
try:
	res_dict = res.json()
except ValueError as e:
	# log error
	portfolio_error_logger.error_logger('line 20 of portfolio_main ' + str(e))

# try accessing the relevant key of the dict
try:
	quote_list = res_dict['query']['results']['quote']
except JSONDecodeError as ee:
	# log error
	portfolio_error_logger.error_logger('line 27 of portfolio_main ' + str(ee))

# delete unused entries in quote dict
for stock in quote_list:
	for key in portfolio_consts.unused_keys:
		stock.pop(key, None)
			
# send quote lists to db and es methods
#db_updater(res_dict.query.results.quote)
#es_updater(res_dict.query.results.quote)

# now run some 

