from django.core.mail import send_mail
from datetime import datetime

def loggedin_mail(request):
	send_mail(
		subject= 'yoursite.in, action needed: Sign-in',
		message= f'''{request.user.username.title()},
Someone signed-in to your account.

When:	{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
Device:	{request.META.get('HTTP_USER_AGENT', '')}	
IP:	{request.META.get('REMOTE_ADDR', '')}
If this was you, you can disregard this message. Otherwise, please let us know.''',
		from_email= 'account@yoursite.com',
		recipient_list= [request.user.email],
		fail_silently= False,
	)
	
def account_creation_mail(request):
	send_mail(
		subject= 'yoursite.in, Account Created',
		message= f'''Congratulations {request.user.username.title()},
Your account are successfully created.
Your username is {request.user.username}

When:	{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
Device:	{request.META.get('HTTP_USER_AGENT', '')}	
IP:	{request.META.get('REMOTE_ADDR', '')}


If this was not you, please let us know.''',
		from_email= 'account@yoursite.com',
		recipient_list= [request.user.email],
		fail_silently= False,
	)