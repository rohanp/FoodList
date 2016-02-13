import poplib
from twilio.rest import TwilioRestClient
import pprint; pp = pprint.PrettyPrinter(indent=4)
import email
# your passwords and stuff should go in here
import auth

account_sid = auth.account_sid
auth_token = auth.auth_token
twilio_number = auth.twilio_number

client = TwilioRestClient(account_sid, auth_token)

mail = poplib.POP3_SSL('pop.gmail.com', '995')
mail.user(auth.gmail_username)
mail.pass_(auth.gmail_pass)


numbers = ['7032209091',]# '7035010862']

def main():

	if mail.stat()[1] > 0: # is new mail
		numMessages = len(mail.list()[1])

		for i in range(numMessages):
			_, resp, _ = mail.retr(i+1)

			string = ' '.join(map(bytes.decode, resp))
			message = email.message_from_string(string)

			for part in message.walk():
				print(part)
				if part.get_content_type() == 'text/plain':
					print(part.get_payload())



def push(msg):
	for number in numbers:
		sent = client.messages.create(to='+1'+number, from_=twilio_number,
		                                 body=msg)
		pp.pprint(vars(sent))

main()
mail.quit()
