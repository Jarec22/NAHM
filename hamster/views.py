from django.shortcuts import render
from django.http import HttpResponse
from hamster.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

def about(request):
	context_dict = {}
	print(request.method)
	print(request.user)
	return render(request, 'hamster/about.html', context=context_dict)

def start(request):
	user_form = UserForm()
	registered = False
	if request.method == 'POST':
		if request.POST.get('submit') == 'register':
			registered = False
			user_form = UserForm(request.POST)
			if user_form.is_valid():
				user = user_form.save()
				user.save()
				registered = True
			else:
				print(user_form.errors)
				
				
		elif request.POST.get('submit') == 'login':
			print("did we get here")
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				print("The login was successful")
				return redirect('about')
				#add code to move them to the story selection or my account
			else:
				print(f"Invalid login details: {username}, {password}")
				return HttpResponse("Invalid login details supplied")
	else:
		user_form = UserForm()
		
		
	return render(request, 'hamster/start.html',
					context = {'user_form':user_form,
					'registered':registered})