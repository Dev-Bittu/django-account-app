from django.shortcuts import (
	render,
	redirect
)
from django.contrib.auth import (
	authenticate,
	login,
	logout	
)
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import (
	UserCreationForm as RegistrationForm,
	AuthenticationForm as LoginForm
)
from .mail import (
	loggedin_mail,
	account_creation_mail
)

# Create your views here.
class Register(View):
	def get(self, request):
		if request.user.is_authenticated:
			messages.info(
				request,
				'You are already logged in.'
			)
			return redirect('/')
		return render(
			request,
			'account/register.html',
			{'form': RegistrationForm()}
		)
	
	def post(self, request):
		user = RegistrationForm(request.POST)
		if user.is_valid():
			user.save()
			messages.success(
				request,
				'Registration successfull.'
			)
			account_creation_mail(
				request
			)
			login(request, user)
			return redirect('profile')
		else:
			messages.warning(
				request,
				'Form is not valid.'
			)
		return redirect('register')
	
class Login(View):
	def get(self, request):
		if request.user.is_authenticated:
			messages.info(
				request,
				'You are already logged in.'
			)
			return redirect('/')
		return render(
			request,
			'account/login.html',
			{'form': LoginForm()}
		)
	
	def post(self, request):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		if username and password:
			user = authenticate(
				username = username,
				password = password
			)
			if user is not None:
				login(request, user)
				messages.success(
					request,
					'Logged in successully.'	
				)
				loggedin_mail(
					request
				)
				return redirect('profile')
			else:
				messages.warning(
					request,
					'Username or Password is incorrect.'	
				)
		else:
			messages.warning(
				request,
				'Username and Password required.'
			)
		return redirect('login')

class Logout(View):
	login_required = True
	def get(self, request):
		logout(request)
		messages.info(
			request,
			'Logged out.!!!'
		)
		return redirect('login')

class Profile(View):
	pass

class Setting(View):
	pass