from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
	if request.method == 'POST':

		# check passwords aren't the same
		if request.POST['password'] != request.POST['password-confirmation']:
			return render(request, 'accounts/signup.html', {'error': 'Your passwords must match'})

		# check if username already exists
		try:
			user = User.objects.get(username=request.POST['username'])
			return render(request, 'accounts/signup.html', {'error': 'Username already exists'})

		# create user if it doesn't work
		except User.DoesNotExist:
			print("seems to work ok so far5")
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
				print("trying to login")
				auth.login(request, user)
				return redirect('index')
			# if user enters empty string
			except ValueError:
				return render(request, 'accounts/signup.html', {'error': 'You must enter a reasonable username. No empty strings.'})

	# user wants to come to signup page
	else:
		return render(request, 'accounts/signup.html')


def login(request):
	return render(request, 'accounts/login.html')


def logout(request):
	return render(request, 'accounts/signup.html')