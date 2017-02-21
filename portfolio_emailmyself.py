# based on python3 docs example
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Import local stuff
import portfolio_consts


def emailmyself(data):
	# filter the data
	fflag = False
	
	# for anything passing the filter add to message
	# then email
	if fflag == True:
		# Open a plain text file for reading.  For this example, assume that
		# the text file contains only ASCII characters.
		#with open(textfile) as fp:

		# Create a text/plain message
		msg = MIMEText("")

		# me == the sender's email address
		# you == the recipient's email address
		msg['Subject'] = "Your Price Alerts"
		msg['From'] = portfolio_consts.from_email
		msg['To'] = portfolio_consts.to_email

		# Send the message via our own SMTP server.
		s = smtplib.SMTP('localhost')
		s.send_message(msg)
		s.quit()
		return
	
	else:
		return