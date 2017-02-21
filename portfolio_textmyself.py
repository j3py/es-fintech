#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Import local stuff
import portfolio_consts

# Preset values:
accountSID = portfolio_consts.accountSID
authToken = portfolio_consts.authToken
myNumber = portfolio_consts.myNumber
twilioNumber = portfolio_consts.twilioNumber

from twilio.rest import TwilioRestClient

def textmyself(message):
	twilioCli = TwilioRestClient(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)